import json
import os
import platform
import sys
from contextlib import contextmanager

import pytest
from mock.mock import patch, MagicMock

from conan.test.assets.genconanfile import GenConanfile
from conan.test.utils.env import environment_update
from conan.test.utils.tools import TestClient

_sbom_zlib_1_2_11 = """
{
  "components" : [ {
    "author" : "<Put your name here> <And your email here>",
    "bom-ref" : "pkg:conan/zlib@1.2.11?rref=6754320047c5dd54830baaaf9fc733c4",
    "description" : "<Description of zlib package here>",
    "licenses" : [ {
      "license" : {
        "name" : "<Put the package license here>"
      }
    } ],
    "name" : "zlib",
    "purl" : "pkg:conan/zlib@1.2.11",
    "type" : "library",
    "version" : "1.2.11"
  } ],
  "dependencies" : [ {
    "ref" : "pkg:conan/zlib@1.2.11?rref=6754320047c5dd54830baaaf9fc733c4"
  } ],
  "metadata" : {
    "component" : {
      "author" : "<Put your name here> <And your email here>",
      "bom-ref" : "pkg:conan/zlib@1.2.11?rref=6754320047c5dd54830baaaf9fc733c4",
      "name" : "zlib/1.2.11",
      "type" : "library"
    },
    "timestamp" : "2025-06-10T08:13:11Z",
    "tools" : [ {
      "externalReferences" : [ {
        "type" : "website",
        "url" : "https://github.com/conan-io/conan"
      } ],
      "name" : "Conan-io"
    } ]
  },
  "serialNumber" : "urn:uuid:4f7ce240-4c6d-4a87-bfb6-78d0fbc839e3",
  "bomFormat" : "CycloneDX",
  "specVersion" : "1.4",
  "version" : 1
}
"""


@contextmanager
def proxy_response(status, data, retry_after=60):
    with patch("conan.api.conan_api.ConanAPI._ApiHelpers.requester") as conanRequesterMock:
        return_status = MagicMock()
        return_status.status_code = status
        return_status.json = MagicMock(return_value=data)
        return_status.headers = {"retry-after": retry_after}
        conanRequesterMock.post = MagicMock(return_value=return_status)

        yield conanRequesterMock, return_status


def test_conan_audit_proxy():
    successful_response = {
        "data": {
            "query": {
                "vulnerabilities": {
                    "totalCount": 1,
                    "edges": [
                        {
                            "node": {
                                "name": "CVE-2023-45853",
                                "description": "Zip vulnerability",
                                "severity": "Critical",
                                "cvss": {
                                    "preferredBaseScore": 8.9
                                },
                                "aliases": [
                                    "CVE-2023-45853",
                                    "JFSA-2023-000272529"
                                ],
                                "advisories": [
                                    {
                                        "name": "CVE-2023-45853"
                                    },
                                    {
                                        "name": "JFSA-2023-000272529"
                                    }
                                ],
                                "references": [
                                    "https://pypi.org/project/pyminizip/#history",
                                ]
                            }
                        }
                    ]
                }
            }
        },
        "error": None
    }

    tc = TestClient(light=True, default_server_user=True)

    tc.save({"conanfile.py": GenConanfile("zlib", "1.2.11"),
             "sbom.cdx.json": _sbom_zlib_1_2_11})
    tc.run("create . --lockfile-out=conan.lock")
    tc.run("upload * -c -r=default")

    tc.run("list * -r=default -f=json", redirect_stdout="pkglist_remote.json")

    tc.run("list '*' -f=json", redirect_stdout="pkglist.json")

    tc.run("audit list zlib/1.2.11", assert_error=True)
    assert "Authentication required for the CVE provider: 'conancenter" in tc.out

    tc.run("audit provider auth conancenter --token=valid_token")

    with proxy_response(200, successful_response):
        tc.run("audit list zlib/1.2.11")
        assert "zlib/1.2.11 1 vulnerability found" in tc.out

        tc.run("audit list -l=pkglist.json")
        assert "zlib/1.2.11 1 vulnerability found" in tc.out

        tc.run("audit list -l=pkglist_remote.json -r=default")
        assert "zlib/1.2.11 1 vulnerability found" in tc.out

        tc.run("audit list --lockfile=conan.lock")
        assert "zlib/1.2.11 1 vulnerability found" in tc.out

        tc.run("audit list --sbom=sbom.cdx.json")
        assert "zlib/1.2.11 1 vulnerability found" in tc.out

        tc.run("audit scan --requires=zlib/1.2.11")
        assert "zlib/1.2.11 1 vulnerability found" in tc.out

        tc.save({"conanfile.txt": "[requires]\nzlib/1.2.11\n"}, clean_first=True)
        tc.run("audit scan")
        assert "zlib/1.2.11 1 vulnerability found" in tc.out

        tc.run("audit scan . --requires=zlib/1.2.11", assert_error=True)
        assert "--requires and --tool-requires arguments are incompatible with [path] '.' argument" in tc.out

    # Now some common errors, like rate limited or missing lib, but it should not fail!
    with proxy_response(429, {"error": "Rate limit exceeded"}):
        tc.run("audit list zlib/1.2.11", assert_error=True)
        assert "You have exceeded the number of allowed requests" in tc.out
        assert "The limit will reset in 1 minute" in tc.out

    with proxy_response(429, {"error": "Rate limit exceeded"}, retry_after=2 * 3600):
        tc.run("audit list zlib/1.2.11", assert_error=True)
        assert "You have exceeded the number of allowed requests" in tc.out
        assert "The limit will reset in 2 hours and 0 minute" in tc.out

    with proxy_response(400, {"error": "Not found"}):
        # Not finding a package should not be an error
        tc.run("audit list zlib/1.2.11")
        assert "Package 'zlib/1.2.11' not scanned: Not found." in tc.stdout

    with proxy_response(403, {"error": "Error not shown"}):
        tc.run("audit list zlib/1.2.11", assert_error=True)
        assert "ERROR: Authentication error (403)" in tc.out
        assert "Error not shown" not in tc.out

    with proxy_response(500, {"error": "Internal error"}):
        tc.run("audit list zlib/1.2.11", assert_error=True)
        assert "Internal server error (500)" in tc.out

    with proxy_response(405, {"error": "Method not allowed"}):
        tc.run("audit list zlib/1.2.11", assert_error=True)
        assert "Error in zlib/1.2.11 (405)" in tc.out

    tc.run("audit provider add myprivate --url=foo --type=private --token=valid_token")

    tc.run("audit provider list")
    assert "(type: conan-center-proxy)" in tc.out
    assert "(type: private)" in tc.out

    tc.run("audit provider remove conancenter")
    tc.run("audit list zlib/1.2.11", assert_error=True)
    assert ("ERROR: Provider 'conancenter' not found. Please specify a valid provider name or add "
            "it using: 'conan audit provider add conancenter --url=https://audit.conan.io/ "
            "--type=conan-center-proxy --token=<token>'") in tc.out
    assert "If you don't have a valid token, register at: https://audit.conan.io/register." in tc.out

    if platform.system() != "Windows":
        providers_stat = os.stat(os.path.join(tc.cache_folder, "audit_providers.json"))
        # Assert that only the current user can read/write the file
        assert providers_stat.st_uid == os.getuid()
        assert providers_stat.st_gid == os.getgid()
        assert providers_stat.st_mode & 0o777 == 0o600


def test_conan_audit_private():
    successful_response = {
        "data": {
            "query": {
                "vulnerabilities": {
                    "totalCount": 1,
                    "edges": [
                        {
                            "node": {
                                "name": "CVE-2023-45853",
                                "description": "Zip vulnerability",
                                "severity": "Critical",
                                "cvss": {
                                    "preferredBaseScore": 8.9
                                },
                                "aliases": [
                                    "CVE-2023-45853",
                                    "JFSA-2023-000272529"
                                ],
                                "advisories": [
                                    {
                                        "name": "CVE-2023-45853"
                                    },
                                    {
                                        "name": "JFSA-2023-000272529"
                                    }
                                ],
                                "references": [
                                    "https://pypi.org/project/pyminizip/#history",
                                ]
                            }
                        }
                    ]
                }
            }
        }
    }

    tc = TestClient(light=True)

    tc.save({"conanfile.py": GenConanfile("zlib", "1.2.11"),
             "sbom.cdx.json": _sbom_zlib_1_2_11})
    tc.run("create . --lockfile-out=conan.lock")

    tc.run("list '*' -f=json", redirect_stdout="pkglist.json")

    # TODO: If the CLI does not allow tokenless provider, should this case not be handled?
    tc.run("audit provider add myprivate --url=foo --type=private --token=f")
    # Now, remove the token as if the user didn't set it manually in the json
    providers = json.loads(tc.load_home("audit_providers.json"))
    providers["myprivate"].pop("token", None)
    tc.save_home({"audit_providers.json": json.dumps(providers)})

    tc.run("audit list zlib/1.2.11 -p=myprivate", assert_error=True)
    assert "Missing authentication token for 'myprivate' provider" in tc.out

    tc.run("audit provider auth myprivate --token=valid_token")

    with proxy_response(200, successful_response):
        tc.run("audit list zlib/1.2.11 -p=myprivate")
        assert "zlib/1.2.11 1 vulnerability found" in tc.out

        tc.run("audit list -l=pkglist.json -p=myprivate")
        assert "zlib/1.2.11 1 vulnerability found" in tc.out

        tc.run("audit list --lockfile=conan.lock -p=myprivate")
        assert "zlib/1.2.11 1 vulnerability found" in tc.out

        tc.run("audit list --sbom=sbom.cdx.json -p=myprivate")
        assert "zlib/1.2.11 1 vulnerability found" in tc.out

        tc.run("audit scan --requires=zlib/1.2.11  -p=myprivate")
        assert "zlib/1.2.11 1 vulnerability found" in tc.out

    # Now some common errors, like rate limited or missing lib, but it should not fail!
    with proxy_response(400, {"errors": [{"message": "Ref not found"}]}):
        # Not finding a package should not be an error
        tc.run("audit list zlib/1.2.11 -p=myprivate")
        assert "Package 'zlib/1.2.11' not scanned: Not found." in tc.stdout

    with proxy_response(403, {"errors": [{"message": "Authentication error"}]}):
        tc.run("audit list zlib/1.2.11 -p=myprivate")
        assert "Unknown error" in tc.out

    with proxy_response(500, {"errors": [{"message": "Internal error"}]}):
        tc.run("audit list zlib/1.2.11 -p=myprivate")
        assert "Unknown error" in tc.out

    with proxy_response(405, {"errors": [{"message": "Method not allowed"}]}):
        tc.run("audit list zlib/1.2.11 -p=myprivate")
        assert "Unknown error" in tc.out

    with proxy_response(404, {"errors": [{"message": "Not found"}]}):
        tc.run("audit list zlib/1.2.11 -p=myprivate")
        assert "An error occurred while connecting to the 'myprivate' provider" in tc.out



@pytest.mark.skipif(sys.version_info < (3, 10),
                    reason="Strict Base64 validation introduced in Python 3.10")
def test_conan_audit_corrupted_token():
    tc = TestClient(light=True)

    json_path = os.path.join(tc.cache_folder, "audit_providers.json")
    with open(json_path, "r") as f:
        data = json.load(f)

    # this is not a valid base64 string and will raise an exception
    data["conancenter"]["token"] = "corrupted_token"

    with open(json_path, "w") as f:
        json.dump(data, f)
    tc.run("audit list zlib/1.2.11", assert_error=True)
    assert "Invalid token format for provider 'conancenter'. The token might be corrupt." in tc.out


def test_audit_list_conflicting_args():
    tc = TestClient(light=True)
    tc.save({"pkglist.json": '{"Local Cache": {"zlib/1.2.11": {}}}'})
    tc.run("audit list zlib/1.2.11 -l=pkglist.json", assert_error=True)
    assert "argument -l/--list: not allowed with argument reference" in tc.out


def test_audit_provider_add_missing_url():
    tc = TestClient(light=True)
    tc.run("audit provider add myprivate --type=private --token=valid_token", assert_error=True)
    assert "Name, URL and type are required to add a provider" in tc.out


def test_audit_provider_remove_nonexistent():
    tc = TestClient(light=True)
    tc.run("audit provider remove nonexistingprovider", assert_error=True)
    assert "Provider 'nonexistingprovider' not found" in tc.out


def test_audit_list_missing_arguments():
    tc = TestClient(light=True)
    tc.run("audit list", assert_error=True)
    assert "one of the arguments reference" in tc.out


def test_audit_provider_env_credentials_with_proxy(monkeypatch):
    tc = TestClient(light=True)
    # Authenticate the provider with an old token to verify that the env variable overrides it
    tc.run("audit provider auth conancenter --token=old_token")

    captured_headers = {}

    def fake_post(url, headers, json):  # noqa
        # Capture the headers used in the request
        captured_headers.update(headers)
        response = MagicMock()
        response.status_code = 200
        response.json.return_value = {
            "data": {"query": {"vulnerabilities": {"totalCount": 0, "edges": []}}}
        }
        response.headers = {"retry-after": 60}
        return response

    with environment_update({"CONAN_AUDIT_PROVIDER_TOKEN_CONANCENTER": "env_token_value"}):
        with patch("conan.api.conan_api.ConanAPI._ApiHelpers.requester",
                   new_callable=MagicMock) as requester_mock:
            requester_mock.post = fake_post
            tc.run("audit list zlib/1.2.11")

    # Verify that the Authorization header uses the token from the environment variable
    assert captured_headers.get("Authorization") == "Bearer env_token_value"


def test_audit_global_error_exception():
    """
    Test that a global error returned by the provider results in ConanException
    raised by the formatter, using the 'details' field.
    """
    tc = TestClient(light=True)
    tc.run("audit provider auth conancenter --token=valid_token")

    mock_provider_result = {
        "data": {},
        "conan_error": "Fatal error."
    }

    with patch("conan.api.conan_api.AuditAPI.list", return_value=mock_provider_result):
        tc.run("audit list zlib/1.2.11", assert_error=True)
        assert "ERROR: Fatal error." in tc.out

        tc.run("audit list zlib/1.2.11 -f json", assert_error=True)
        assert "ERROR: Fatal error." in tc.out

        tc.run("audit list zlib/1.2.11 -f html", assert_error=True)
        assert "ERROR: Fatal error." in tc.out


@pytest.mark.parametrize("severity_level, threshold, should_fail", [
    (1.0, None, False),
    (8.9, None, False),
    (9.0, None, True),
    (9.1, None, True),
    (5.0, 5.1, False),
    (5.1, 5.1, True),
    (5.2, 5.1, True),
    (9.0, 11.0, False),
])
def test_audit_scan_threshold_error(severity_level, threshold, should_fail):
    """In case the severity level is equal or higher than the found for a CVE,
       the command should output the information as usual, and exit with non-success code error.
    """
    successful_response = {
        "data": {
            "query": {
                "vulnerabilities": {
                    "totalCount": 1,
                    "edges": [
                        {
                            "node": {
                                "name": "CVE-2023-45853",
                                "description": "Zip vulnerability",
                                "severity": "Critical",
                                "cvss": {
                                    "preferredBaseScore": severity_level
                                },
                                "aliases": [
                                    "CVE-2023-45853",
                                    "JFSA-2023-000272529"
                                ],
                                "advisories": [
                                    {
                                        "name": "CVE-2023-45853"
                                    },
                                    {
                                        "name": "JFSA-2023-000272529"
                                    }
                                ],
                                "references": [
                                    "https://pypi.org/project/pyminizip/#history",
                                ]
                            }
                        }
                    ]
                }
            }
        }
    }

    tc = TestClient(light=True)

    tc.save({"conanfile.py": GenConanfile("foobar", "0.1.0")})
    tc.run("export .")
    tc.run("audit provider auth conancenter --token=valid_token")

    with proxy_response(200, successful_response):
        severity_param = "" if threshold is None else f"-sl {threshold}"
        tc.run(f"audit scan --requires=foobar/0.1.0 {severity_param}", assert_error=should_fail)
        assert "foobar/0.1.0 1 vulnerability found" in tc.out
        assert f"CVSS: {severity_level}" in tc.out
        if should_fail:
            if threshold is None:
                threshold = "9.0"
            assert f"ERROR: The package foobar/0.1.0 has a CVSS score {severity_level} and exceeded the threshold severity level {threshold}" in tc.out

def test_parse_error_crash_when_no_edges():
    from conan.cli.commands.audit import _parse_error_threshold

    scan_result = {
        "data": {
            # this used to crash because dav1d not having vulnerabilities field
            "dav1d/1.4.3": {"error": {"details": "Package 'dav1d/1.4.3' not scanned: Not found."}},
            "zlib/1.2.11": {
                "vulnerabilities": {
                    "totalCount": 1,
                    "edges": [
                        {"node": {"cvss": {"preferredBaseScore": 7.0}}}
                    ]
                }
            }
        }
    }

    _parse_error_threshold(scan_result, error_level=5.0)
    assert "conan_error" in scan_result
    assert "zlib/1.2.11" in scan_result["conan_error"]
    assert "7.0" in scan_result["conan_error"]


@pytest.mark.parametrize("package_context", ["build", "host"])
@pytest.mark.parametrize("filter_context", ["build", "host", None])
def test_audit_scan_context_filter(package_context, filter_context):
    tc = TestClient(light=True)

    tc.save({"conanfile.py": GenConanfile("zlib", "1.2.11")})
    tc.run("export .")
    tc.run("audit provider auth conancenter --token=valid_token")

    requires = "requires" if package_context == "host" else "tool-requires"
    context = "" if filter_context is None else f"--context={filter_context}"

    with proxy_response(200, {}):
        tc.run(f"audit scan --{requires}=zlib/1.2.11 {context}")
        if filter_context is None or filter_context == package_context:
            assert "Requesting vulnerability info for: zlib/1.2.11" in tc.out
        else:
            assert "Requesting vulnerability info for: zlib/1.2.11" not in tc.out
