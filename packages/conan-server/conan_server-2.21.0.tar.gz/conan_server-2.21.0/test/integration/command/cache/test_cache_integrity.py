import os

import pytest

from conan.test.assets.genconanfile import GenConanfile
from conan.test.utils.tools import TestClient
from conan.internal.util.files import save


@pytest.mark.parametrize("use_pkglist", [True, False])
def test_cache_integrity(use_pkglist):
    t = TestClient()
    t.save({"conanfile.py": GenConanfile()})
    t.run("create . --name pkg1 --version 1.0")
    t.run("create . --name pkg2 --version=2.0")
    layout = t.created_layout()
    conaninfo = os.path.join(layout.package(), "conaninfo.txt")
    save(conaninfo, "[settings]")
    t.run("create . --name pkg3 --version=3.0")
    layout = t.created_layout()
    conaninfo = os.path.join(layout.package(), "conaninfo.txt")
    save(conaninfo, "[settings]")
    t.run("create . --name pkg4 --version=4.0")
    layout = t.created_layout()
    conaninfo = os.path.join(layout.package(), "conaninfo.txt")
    save(conaninfo, "[settings]")

    if use_pkglist:
        t.run("list *:*#* -f=json", redirect_stdout="pkglist.json")
    arg = "--list=pkglist.json" if use_pkglist else "*"

    t.run(f"cache check-integrity {arg}", assert_error=True)
    assert "pkg1/1.0#4d670581ccb765839f2239cc8dff8fbd: Integrity check: ok" in t.out
    assert "pkg1/1.0#4d670581ccb765839f2239cc8dff8fbd:da39a3ee5e6b4b0d3255bfef95601890afd80709" \
           "#0ba8627bd47edc3a501e8f0eb9a79e5e: Integrity check: ok" in t.out
    assert "pkg2/2.0#4d670581ccb765839f2239cc8dff8fbd:da39a3ee5e6b4b0d3255bfef95601890afd80709" \
           "#0ba8627bd47edc3a501e8f0eb9a79e5e: ERROR: \nManifest mismatch" in t.out
    assert "pkg3/3.0#4d670581ccb765839f2239cc8dff8fbd:da39a3ee5e6b4b0d3255bfef95601890afd80709" \
           "#0ba8627bd47edc3a501e8f0eb9a79e5e: ERROR: \nManifest mismatch" in t.out
    assert "pkg4/4.0#4d670581ccb765839f2239cc8dff8fbd:da39a3ee5e6b4b0d3255bfef95601890afd80709" \
           "#0ba8627bd47edc3a501e8f0eb9a79e5e: ERROR: \nManifest mismatch" in t.out

    t.run("remove pkg2/2.0:da39a3ee5e6b4b0d3255bfef95601890afd80709 -c")
    t.run("remove pkg3/3.0:da39a3ee5e6b4b0d3255bfef95601890afd80709 -c")
    t.run("remove pkg4/4.0:da39a3ee5e6b4b0d3255bfef95601890afd80709 -c")
    t.run("cache check-integrity *")
    assert "pkg1/1.0#4d670581ccb765839f2239cc8dff8fbd: Integrity check: ok" in t.out
    assert "pkg2/2.0#4d670581ccb765839f2239cc8dff8fbd: Integrity check: ok" in t.out
    assert "pkg3/3.0#4d670581ccb765839f2239cc8dff8fbd: Integrity check: ok" in t.out
    assert "pkg4/4.0#4d670581ccb765839f2239cc8dff8fbd: Integrity check: ok" in t.out


def test_cache_integrity_missing_recipe_manifest():
    t = TestClient()
    t.save({"conanfile.py": GenConanfile()})
    t.run("create . --name pkg1 --version 1.0")
    t.run("create . --name pkg2 --version=2.0")
    layout = t.exported_layout()
    manifest = os.path.join(layout.export(), "conanmanifest.txt")
    os.remove(manifest)
    t.run("create . --name pkg3 --version=3.0")

    t.run("cache check-integrity *", assert_error=True)
    assert "pkg1/1.0#4d670581ccb765839f2239cc8dff8fbd: Integrity check: ok" in t.out
    assert "pkg2/2.0#4d670581ccb765839f2239cc8dff8fbd: ERROR: Manifest missing" in t.out
    assert "pkg3/3.0#4d670581ccb765839f2239cc8dff8fbd: Integrity check: ok" in t.out
    assert "ERROR: There are corrupted artifacts, check the error logs" in t.out

    t.run("remove pkg2* -c")
    t.run("cache check-integrity *")
    assert "pkg1/1.0#4d670581ccb765839f2239cc8dff8fbd:da39a3ee5e6b4b0d3255bfef95601890afd80709" \
           "#0ba8627bd47edc3a501e8f0eb9a79e5e: Integrity check: ok" in t.out
    assert "pkg3/3.0#4d670581ccb765839f2239cc8dff8fbd: Integrity check: ok" in t.out
    assert "Integrity check: ok" in t.out


def test_cache_integrity_missing_package_manifest():
    t = TestClient()
    t.save({"conanfile.py": GenConanfile()})
    t.run("create . --name pkg1 --version 1.0")
    t.run("create . --name pkg2 --version=2.0")
    layout = t.created_layout()
    manifest = os.path.join(layout.package(), "conanmanifest.txt")
    os.remove(manifest)
    t.run("create . --name pkg3 --version=3.0")

    t.run("cache check-integrity *", assert_error=True)
    assert "pkg1/1.0#4d670581ccb765839f2239cc8dff8fbd: Integrity check: ok" in t.out
    assert "pkg2/2.0#4d670581ccb765839f2239cc8dff8fbd:da39a3ee5e6b4b0d3255bfef95601890afd80709" \
           "#0ba8627bd47edc3a501e8f0eb9a79e5e: ERROR: Manifest missing" in t.out
    assert "pkg3/3.0#4d670581ccb765839f2239cc8dff8fbd: Integrity check: ok" in t.out
    assert "ERROR: There are corrupted artifacts, check the error logs" in t.out

    t.run("remove pkg2* -c")
    t.run("cache check-integrity *")
    assert "pkg1/1.0#4d670581ccb765839f2239cc8dff8fbd:da39a3ee5e6b4b0d3255bfef95601890afd80709" \
           "#0ba8627bd47edc3a501e8f0eb9a79e5e: Integrity check: ok" in t.out
    assert "pkg3/3.0#4d670581ccb765839f2239cc8dff8fbd: Integrity check: ok" in t.out
    assert "Integrity check: ok" in t.out


def test_cache_integrity_missing_package_conaninfo():
    t = TestClient()
    t.save({"conanfile.py": GenConanfile()})
    t.run("create . --name pkg1 --version 1.0")
    t.run("create . --name pkg2 --version=2.0")
    layout = t.created_layout()
    conaninfo = os.path.join(layout.package(), "conaninfo.txt")
    os.remove(conaninfo)

    t.run("cache check-integrity *", assert_error=True)
    assert "pkg1/1.0#4d670581ccb765839f2239cc8dff8fbd: Integrity check: ok" in t.out
    assert "pkg2/2.0#4d670581ccb765839f2239cc8dff8fbd:da39a3ee5e6b4b0d3255bfef95601890afd80709" \
           "#0ba8627bd47edc3a501e8f0eb9a79e5e: ERROR: \nManifest mismatch" in t.out

    t.run("remove pkg2* -c")
    t.run("cache check-integrity *")
    assert "pkg1/1.0#4d670581ccb765839f2239cc8dff8fbd:da39a3ee5e6b4b0d3255bfef95601890afd80709" \
           "#0ba8627bd47edc3a501e8f0eb9a79e5e: Integrity check: ok" in t.out


def test_cache_integrity_missing_package_file():
    t = TestClient()
    t.save({"conanfile.py": GenConanfile().with_package_file("myfile", "mycontents!")})
    t.run("create . --name pkg --version 1.0")
    layout = t.created_layout()
    os.remove(os.path.join(layout.package(), "myfile"))

    t.run("cache check-integrity *", assert_error=True)
    assert "pkg/1.0#2f2609c8e5c87bf836c3fdaa6096b55d:da39a3ee5e6b4b0d3255bfef95601890afd80709" \
           "#d950d0cd76f6bba62c8add9c68d1aeb3: ERROR: \nManifest mismatch" in t.out


def test_cache_integrity_export_sources():
    # https://github.com/conan-io/conan/issues/14840
    t = TestClient(default_server_user=True)
    t.save({"conanfile.py": GenConanfile("pkg", "0.1").with_exports_sources("src/*"),
            "src/mysource.cpp": ""})
    t.run("create .")
    t.run("cache check-integrity *")
    assert "pkg/0.1#ae07161b81ab07f7f1f746391668df0e: Integrity check: ok" in t.out

    # If we download, integrity should be ok
    # (it failed before, because the manifest is not complete)
    t.run("upload * -r=default -c")
    t.run("remove * -c")
    t.run("install --requires=pkg/0.1")
    t.run("cache check-integrity *")
    assert "pkg/0.1#ae07161b81ab07f7f1f746391668df0e: Integrity check: ok" in t.out
