import json
import os
import platform
import stat
import textwrap
from collections import OrderedDict

import pytest
from mock import patch
from requests import Response

from conan.errors import ConanException
from conan.api.model import PkgReference
from conan.internal.api.uploader import gzopen_without_timestamps
from conan.internal.paths import EXPORT_SOURCES_TGZ_NAME, PACKAGE_TGZ_NAME
from conan.test.utils.tools import NO_SETTINGS_PACKAGE_ID, TestClient, TestServer, \
    GenConanfile, TestRequester, TestingResponse
from conan.internal.util.files import is_dirty, save, set_dirty, sha1sum

conanfile = """from conan import ConanFile
from conan.tools.files import copy
class MyPkg(ConanFile):
    name = "hello0"
    version = "1.2.1"
    exports_sources = "*"

    def package(self):
        copy(self, "*.cpp", self.source_folder, self.package_folder)
        copy(self, "*.h", self.source_folder, self.package_folder)
"""


class TestUpload:

    @pytest.mark.artifactory_ready
    def test_upload_dirty(self):
        client = TestClient(default_server_user=True, light=True)
        client.save({"conanfile.py": GenConanfile("hello", "0.1")})
        client.run("create .")

        pkg_folder = client.created_layout().package()
        set_dirty(pkg_folder)

        client.run("upload * -r=default -c", assert_error=True)
        assert "ERROR: Package hello/0.1:da39a3ee5e6b4b0d3255bfef95601890afd80709 i" \
               "s corrupted, aborting upload." in client.out
        assert "Remove it with 'conan remove hello/0.1:da39a3ee5e6b4b0d3255bfef95601890afd80709" \
               in client.out

        # Test that removeing the binary allows moving forward
        client.run("remove hello/0.1:da39a3ee5e6b4b0d3255bfef95601890afd80709 -c")
        client.run("upload * -r=default --confirm")

    @pytest.mark.artifactory_ready
    def test_upload_force(self):
        client = TestClient(default_server_user=True, light=True)
        conanfile_ = textwrap.dedent("""
            from conan import ConanFile
            from conan.tools.files import copy
            class MyPkg(ConanFile):
                name = "hello"
                version = "0.1"
                def package(self):
                    copy(self, "myfile.sh", src=self.source_folder, dst=self.package_folder)
            """)
        client.save({"conanfile.py": conanfile_,
                    "myfile.sh": "foo"})

        client.run("export-pkg .")
        client.run("upload * --confirm -r default")
        assert "Uploading package 'hello" in client.out
        client.run("upload * --confirm -r default")
        assert "Uploading package" not in client.out

        if platform.system() == "Linux":
            package_file_path = os.path.join(client.current_folder, "myfile.sh")
            os.system('chmod +x "{}"'.format(package_file_path))
            assert os.stat(package_file_path).st_mode & stat.S_IXUSR
            client.run("export-pkg .")

            client.run("upload * --confirm -r default")
            # Doesn't change revision, doesn't reupload
            assert "conan_package.tgz" not in client.out
            assert "skipping upload" in client.out
            assert "Compressing package..." not in client.out

        # with --force it really re-uploads it
        client.run("upload * --confirm --force -r default")
        assert "Uploading recipe 'hello" in client.out
        assert "Uploading package 'hello" in client.out

        if platform.system() == "Linux":
            client.run("remove '*' -c")
            client.run("install --requires=hello/0.1 --deployer=full_deploy")
            package_file_path = os.path.join(client.current_folder, "full_deploy", "host", "hello",
                                             "0.1", "myfile.sh")
            # Owner with execute permissions
            assert os.stat(package_file_path).st_mode & stat.S_IXUSR

    @pytest.mark.artifactory_ready
    def test_pattern_upload(self):
        client = TestClient(default_server_user=True, light=True)
        client.save({"conanfile.py": conanfile})
        client.run("create . --user=user --channel=testing")
        client.run("upload hello0/*@user/testing --confirm -r default")
        assert "Uploading recipe 'hello0/1.2.1@" in client.out
        assert "Uploading package 'hello0/1.2.1@" in client.out

    def test_pattern_upload_no_recipes(self):
        client = TestClient(default_server_user=True, light=True)
        client.save({"conanfile.py": conanfile})
        client.run("upload bogus/*@dummy/testing --confirm -r default", assert_error=True)
        assert "No recipes found matching pattern 'bogus/*@dummy/testing'" in client.out

    def test_broken_sources_tgz(self):
        # https://github.com/conan-io/conan/issues/2854
        client = TestClient(default_server_user=True, light=True)
        client.save({"conanfile.py": conanfile,
                     "source.h": "my source"})
        client.run("create . --user=user --channel=testing")
        layout = client.exported_layout()

        def gzopen_patched(name, mode="r", fileobj=None, **kwargs):  # noqa
            raise ConanException("Error gzopen %s" % name)
        with patch('conan.internal.api.uploader.gzopen_without_timestamps', new=gzopen_patched):
            client.run("upload * --confirm -r default --only-recipe",
                       assert_error=True)
            assert "Error gzopen conan_sources.tgz" in client.out

            export_download_folder = layout.download_export()

            tgz = os.path.join(export_download_folder, EXPORT_SOURCES_TGZ_NAME)
            assert os.path.exists(tgz)
            assert is_dirty(tgz)

        client.run("upload * --confirm -r default --only-recipe")
        assert "Removing conan_sources.tgz, marked as dirty" in client.out
        assert os.path.exists(tgz)
        assert not is_dirty(tgz)

    def test_broken_package_tgz(self):
        # https://github.com/conan-io/conan/issues/2854
        client = TestClient(default_server_user=True, light=True)
        client.save({"conanfile.py": conanfile,
                     "source.h": "my source"})
        client.run("create . --user=user --channel=testing")
        pref = client.created_layout().reference

        def gzopen_patched(name, fileobj, compresslevel=None):  # noqa
            if name == PACKAGE_TGZ_NAME:
                raise ConanException("Error gzopen %s" % name)
            return gzopen_without_timestamps(name, fileobj)
        with patch('conan.internal.api.uploader.gzopen_without_timestamps', new=gzopen_patched):
            client.run("upload * --confirm -r default", assert_error=True)
            assert "Error gzopen conan_package.tgz" in client.out

            download_folder = client.get_latest_pkg_layout(pref).download_package()
            tgz = os.path.join(download_folder, PACKAGE_TGZ_NAME)
            assert os.path.exists(tgz)
            assert is_dirty(tgz)

        client.run("upload * --confirm -r default")
        assert "WARN: Removing conan_package.tgz, marked as dirty" in client.out
        assert os.path.exists(tgz)
        assert not is_dirty(tgz)

    def test_corrupt_upload(self):
        c = TestClient(default_server_user=True, light=True)

        c.save({"conanfile.py": conanfile,
                "include/hello.h": ""})
        c.run("create . --user=frodo --channel=stable")
        package_folder = c.created_layout().package()
        save(os.path.join(package_folder, "added.txt"), "")
        os.remove(os.path.join(package_folder, "include/hello.h"))
        c.run("upload hello0/1.2.1@frodo/stable --check -r default", assert_error=True)
        assert ("hello0/1.2.1@frodo/stable#3afd661184b94bdac7fb2057e7bd9baa"
                ":da39a3ee5e6b4b0d3255bfef95601890afd80709"
                "#e70e86439dec07a0d5d3414648b0b16c: ERROR") in c.out
        assert "include/hello.h (manifest: d41d8cd98f00b204e9800998ecf8427e, file: None)" in c.out
        assert "added.txt (manifest: None, file: d41d8cd98f00b204e9800998ecf8427e)" in c.out
        assert "ERROR: There are corrupted artifacts, check the error logs" in c.out

    @pytest.mark.artifactory_ready
    def test_upload_modified_recipe(self):
        client = TestClient(default_server_user=True, light=True)

        client.save({"conanfile.py": conanfile,
                     "hello.cpp": "int i=0"})
        client.run("export . --user=frodo --channel=stable")
        rrev = client.exported_recipe_revision()
        client.run("upload hello0/1.2.1@frodo/stable -r default")
        assert "Uploading recipe 'hello0/1.2.1@frodo/stable#" in client.out

        client2 = TestClient(servers=client.servers, inputs=["admin", "password"])
        client2.save({"conanfile.py": conanfile + "\r\n#end",
                      "hello.cpp": "int i=1"})
        client2.run("export . --user=frodo --channel=stable")
        layout = client2.exported_layout()
        manifest, _ = layout.recipe_manifests()
        manifest.time += 10
        manifest.save(layout.export())
        client2.run("upload hello0/1.2.1@frodo/stable -r default")
        assert "Uploading recipe 'hello0/1.2.1@frodo/stable#" in client2.out

        # first client tries to upload again
        # The client tries to upload exactly the same revision already uploaded, so no changes
        client.run("upload hello0/1.2.1@frodo/stable -r default")
        assert f"'hello0/1.2.1@frodo/stable#{rrev}' already in server, skipping upload" in client.out

    @pytest.mark.artifactory_ready
    def test_upload_unmodified_recipe(self):
        client = TestClient(default_server_user=True, light=True)
        files = {"conanfile.py": GenConanfile("hello0", "1.2.1")}
        client.save(files)
        client.run("export . --user=frodo --channel=stable")
        rrev = client.exported_recipe_revision()
        client.run("upload hello0/1.2.1@frodo/stable -r default")
        assert "Uploading recipe 'hello0/1.2.1@frodo/stable#" in client.out

        client2 = TestClient(servers=client.servers, inputs=["admin", "password"])
        client2.save(files)
        client2.run("export . --user=frodo --channel=stable")
        layout = client2.exported_layout()
        manifest, _ = layout.recipe_manifests()
        manifest.time += 10
        manifest.save(layout.export())
        client2.run("upload hello0/1.2.1@frodo/stable -r default")
        assert (f"Recipe 'hello0/1.2.1@frodo/stable#761f54e34d59deb172d6078add7050a7' already "
                f"in server, skipping upload") in client2.out

        # first client tries to upload again
        client.run("upload hello0/1.2.1@frodo/stable -r default")
        assert (f"Recipe 'hello0/1.2.1@frodo/stable#{rrev}' "
                f"already in server, skipping upload") in client.out

    @pytest.mark.artifactory_ready
    def test_upload_unmodified_package(self):
        client = TestClient(default_server_user=True, light=True)

        client.save({"conanfile.py": conanfile,
                     "hello.cpp": ""})
        client.run("create . --user=frodo --channel=stable")
        prev1 = client.created_layout().reference
        client.run("upload hello0/1.2.1@frodo/stable -r default")

        client2 = TestClient(servers=client.servers, inputs=["admin", "password"])
        client2.save({"conanfile.py": conanfile,
                      "hello.cpp": ""})
        client2.run("create . --user=frodo --channel=stable")
        prev2 = client2.created_layout().reference
        client2.run("upload hello0/1.2.1@frodo/stable -r default")
        assert f"'{repr(prev2.ref)}' already in server, skipping upload" in client2.out
        assert "Uploaded conan recipe 'hello0/1.2.1@frodo/stable' to 'default'" not in client2.out
        assert f"'{prev2.repr_notime()}' already in server, skipping upload" in client2.out

        # first client tries to upload again
        client.run("upload hello0/1.2.1@frodo/stable -r default")
        assert f"'{repr(prev1.ref)}' already in server, skipping upload" in client.out
        assert "Uploaded conan recipe 'hello0/1.2.1@frodo/stable' to 'default'" not in client.out
        assert f"'{prev1.repr_notime()}' already in server, skipping upload" in client2.out

    def test_upload_no_overwrite_all(self):
        conanfile_new = GenConanfile("hello", "1.0").\
            with_import("from conan.tools.files import copy").\
            with_exports_sources(["*"]).\
            with_package('copy(self, "*", self.source_folder, self.package_folder)')

        client = TestClient(default_server_user=True, light=True)
        client.save({"conanfile.py": conanfile_new,
                     "hello.h": ""})
        client.run("create . --user=frodo --channel=stable")
        prev1 = client.created_layout().reference
        # First time upload
        client.run("upload hello/1.0@frodo/stable -r default")
        assert "Forbidden overwrite" not in client.out
        assert "Uploading recipe 'hello/1.0@frodo/stable" in client.out

        # CASE: Upload again
        client.run("upload hello/1.0@frodo/stable -r default")
        assert f"'{repr(prev1.ref)}' already in server, skipping upload" in client.out
        assert f"'{prev1.repr_notime()}' already in server, skipping upload" in client.out

    def test_skip_upload(self):
        """ Check that the option --skip does not upload anything
        """
        client = TestClient(default_server_user=True, light=True)
        client.save({"conanfile.py": GenConanfile("hello0", "1.2.1").with_exports("*"),
                     "file.txt": ""})
        client.run("create .")

        client.run("upload * --dry-run -r default -c")
        assert "Compressing" in client.out
        client.run("search * -r default")
        # after dry run nothing should be on the server
        assert "hello" not in client.out

        # now upload, the stuff should NOT be recompressed
        client.run("upload * -c -r default")
        # check if compressed files are re-used
        assert "Compressing" not in client.out
        # now it should be on the server
        client.run("search * -r default")
        assert "hello0/1.2.1" in client.out

    def test_upload_without_sources(self):
        client = TestClient(default_server_user=True, light=True)
        client.save({"conanfile.py": GenConanfile()})
        client.run("create . --name=pkg --version=0.1 --user=user --channel=testing")
        client.run("upload * --confirm -r default")
        client2 = TestClient(servers=client.servers, inputs=["admin", "password",
                                                             "lasote", "mypass"])

        client2.run("install --requires=pkg/0.1@user/testing")
        client2.run("remote remove default")
        server2 = TestServer([("*/*@*/*", "*")], [("*/*@*/*", "*")],
                             users={"lasote": "mypass"})
        client2.servers = {"server2": server2}
        client2.update_servers()
        client2.run("upload * --confirm -r=server2")

        assert "Uploading recipe 'pkg" in client.out
        assert "Uploading package 'pkg" in client.out

    def test_upload_login_prompt_disabled_no_user(self):
        """ Without user info, uploads should fail when login prompt has been disabled.
        """
        files = {"conanfile.py": GenConanfile("hello0", "1.2.1")}
        client = TestClient(default_server_user=True, light=True)
        client.save(files)
        conan_conf = "core:non_interactive=True"
        client.save_home({"global.conf": conan_conf})

        client.run("create . --user=user --channel=testing")
        client.run("remote logout '*'")
        client.run("upload hello0/1.2.1@user/testing -r default", assert_error=True)

        assert "Conan interactive mode disabled" in client.out
        assert "-> conanmanifest.txt" not in client.out
        assert "-> conanfile.py" not in client.out
        assert "-> conan_export.tgz" not in client.out

    def test_upload_login_prompt_disabled_user_not_authenticated(self):
        # When a user is not authenticated, uploads should fail when login prompt has been disabled.
        files = {"conanfile.py": GenConanfile("hello0", "1.2.1")}
        client = TestClient(default_server_user=True, light=True)
        client.save(files)
        conan_conf = "core:non_interactive=True"
        client.save_home({"global.conf": conan_conf})
        client.run("create . --user=user --channel=testing")
        client.run("remote logout '*'")
        client.run("remote set-user default lasote")
        client.run("upload hello0/1.2.1@user/testing -r default", assert_error=True)
        assert "Conan interactive mode disabled" in client.out
        assert "-> conanmanifest.txt" not in client.out
        assert "-> conanfile.py" not in client.out
        assert "-> conan_export.tgz" not in client.out
        assert "Please enter a password for" not in client.out

    def test_upload_login_prompt_disabled_user_authenticated(self):
        #  When user is authenticated, uploads should work even when login prompt has been disabled.
        client = TestClient(default_server_user=True, light=True)
        client.save({"conanfile.py": GenConanfile("hello0", "1.2.1")})
        conan_conf = "core:non_interactive=True"
        client.save_home({"global.conf": conan_conf})
        client.run("create . --user=user --channel=testing")
        client.run("remote logout '*'")
        client.run("remote login default admin -p password")
        client.run("upload hello0/1.2.1@user/testing -r default")

        assert "Uploading recipe 'hello0/1.2.1@" in client.out
        assert "Uploading package 'hello0/1.2.1@" in client.out

    def test_upload_key_error(self):
        files = {"conanfile.py": GenConanfile("hello0", "1.2.1")}
        server1 = TestServer([("*/*@*/*", "*")], [("*/*@*/*", "*")], users={"lasote": "mypass"})
        server2 = TestServer([("*/*@*/*", "*")], [("*/*@*/*", "*")], users={"lasote": "mypass"})
        servers = OrderedDict()
        servers["server1"] = server1
        servers["server2"] = server2
        client = TestClient(servers=servers)
        client.save(files)
        client.run("create . --user=user --channel=testing")
        client.run("remote login server1 lasote -p mypass")
        client.run("remote login server2 lasote -p mypass")
        client.run("upload hello0/1.2.1@user/testing -r server1")
        client.run("remove * --confirm")
        client.run("install --requires=hello0/1.2.1@user/testing -r server1")
        client.run("remote remove server1")
        client.run("upload hello0/1.2.1@user/testing -r server2")
        assert "ERROR: 'server1'" not in client.out

    def test_upload_without_user_channel(self):
        server = TestServer(users={"user": "password"}, write_permissions=[("*/*@*/*", "*")])
        servers = {"default": server}
        client = TestClient(servers=servers, inputs=["user", "password"])

        client.save({"conanfile.py": GenConanfile()})

        client.run('create . --name=lib --version=1.0')
        assert "lib/1.0: Package '{}' created".format(NO_SETTINGS_PACKAGE_ID) in client.out
        client.run('upload lib/1.0 -c -r default')
        assert "Uploading recipe 'lib/1.0" in client.out

        # Verify that in the remote it is stored as "_"
        pref = PkgReference.loads("lib/1.0@#0:{}#0".format(NO_SETTINGS_PACKAGE_ID))
        path = server.server_store.export(pref.ref)
        assert "/lib/1.0/_/_/0/export" in path.replace("\\", "/")

        path = server.server_store.package(pref)
        assert "/lib/1.0/_/_/0/package" in path.replace("\\", "/")

        # Should be possible with explicit package
        client.run(f'upload lib/1.0#*:{NO_SETTINGS_PACKAGE_ID} -c -r default --force')
        assert "Uploading artifacts" in client.out

    def test_upload_without_cleaned_user(self):
        """ When a user is not authenticated, uploads failed first time
        https://github.com/conan-io/conan/issues/5878
        """

        class EmptyCapabilitiesResponse(object):
            def __init__(self):
                self.ok = False
                self.headers = {"X-Conan-Server-Capabilities": "",
                                "Content-Type": "application/json"}
                self.status_code = 401
                self.content = b''

        class ServerCapabilitiesRequester(TestRequester):
            def __init__(self, *args, **kwargs):
                self._first_ping = True
                super(ServerCapabilitiesRequester, self).__init__(*args, **kwargs)

            def get(self, url, **kwargs):
                app, url = self._prepare_call(url, kwargs)
                assert app
                assert ("/v1/" in url and url.endswith("ping")) or "/v2" in url
                if url.endswith("ping") and self._first_ping:
                    self._first_ping = False
                    return EmptyCapabilitiesResponse()
                else:
                    response = app.get(url, **kwargs)
                    return TestingResponse(response)

        server = TestServer(users={"user": "password"}, write_permissions=[("*/*@*/*", "*")])
        servers = {"default": server}
        client = TestClient(requester_class=ServerCapabilitiesRequester, servers=servers,
                            inputs=["user", "password"])
        files = {"conanfile.py": GenConanfile("hello0", "1.2.1")}
        client.save(files)
        client.run("create . --user=user --channel=testing")
        client.run("remote logout '*'")
        client.run("upload hello0/1.2.1@user/testing -r default")
        assert "Uploading recipe 'hello0/1.2.1@user/testing" in client.out

    def test_server_returns_200_ok(self):
        # https://github.com/conan-io/conan/issues/16104
        # If server returns 200 ok, without headers, it raises an error
        class MyHttpRequester(TestRequester):
            def get(self, _, **kwargs):
                resp = Response()
                resp.status_code = 200
                return resp

        client = TestClient(requester_class=MyHttpRequester, servers={"default": TestServer()})
        client.save({"conanfile.py": GenConanfile("hello0", "1.2.1")})
        client.run("create . ")
        client.run("upload * -c -r default", assert_error=True)
        assert "doesn't seem like a valid Conan remote" in client.out


def test_upload_only_without_user_channel():
    """
    check that we can upload only the packages without user and channel
    https://github.com/conan-io/conan/issues/10579
    """
    c = TestClient(default_server_user=True, light=True)

    c.save({"conanfile.py": GenConanfile("lib", "1.0")})
    c.run('create .')
    c.run("create . --user=user --channel=channel")
    c.run("list *")
    assert "lib/1.0@user/channel" in c.out

    c.run('upload */*@ -c -r=default')
    assert "Uploading recipe 'lib/1.0" in c.out  # FAILS!
    assert "lib/1.0@user/channel" not in c.out
    c.run("search * -r=default")
    assert "lib/1.0" in c.out
    assert "lib/1.0@user/channel" not in c.out

    c.run('upload */*@user/channel -c -r=default')
    assert "Uploading recipe 'lib/1.0@user/channel" in c.out
    c.run("search * -r=default")
    assert "lib/1.0@user/channel" in c.out
    assert "lib/1.0" in c.out


def test_upload_with_python_requires():
    # https://github.com/conan-io/conan/issues/14503
    c = TestClient(default_server_user=True, light=True)
    c.save({"tool/conanfile.py": GenConanfile("tool", "0.1"),
            "dep/conanfile.py": GenConanfile("dep", "0.1").with_python_requires("tool/[>=0.1]")})
    c.run("create tool")
    c.run("create dep")
    c.run("upload tool* -c -r=default")
    c.run("remove tool* -c")
    c.run("upload dep* -c -r=default")
    # This used to fail, but adding the enabled remotes to python_requires resolution, it works
    assert "tool/0.1: Downloaded recipe" in c.out


def test_upload_list_only_recipe():
    c = TestClient(default_server_user=True, light=True)
    c.save({"conanfile.py": GenConanfile("liba", "0.1")})
    c.run("create .")
    c.run("install --requires=liba/0.1 --format=json", redirect_stdout="graph.json")
    c.run("list --graph=graph.json --format=json", redirect_stdout="installed.json")
    c.run("upload --list=installed.json --only-recipe -r=default -c")
    assert "conan_package.tgz" not in c.out


@pytest.mark.parametrize("dry_run", [True, False])
def test_upload_json_output(dry_run):
    c = TestClient(default_server_user=True, light=True)
    c.save({"conanfile.py": GenConanfile("liba", "0.1").with_settings("os")
                                                       .with_shared_option(False)})
    c.run("create . -s os=Linux")
    dry_run_arg = "--dry-run" if dry_run else ""
    c.run(f"upload * -r=default {dry_run_arg} -c --format=json")
    list_pkgs = json.loads(c.stdout)
    revs = list_pkgs["default"]["liba/0.1"]["revisions"]["a565bd5defd3a99e157698fcc6e23b25"]
    pkg = revs["packages"]["9e0f8140f0fe6b967392f8d5da9881e232e05ff8"]
    prev = pkg["revisions"]["f50f552c6e04b1f241e5f7864bc3957f"]
    assert pkg["info"] == {"settings": {"os": "Linux"}, "options": {"shared": "False"}}
    base_url = "v2/conans/liba/0.1/_/_/revisions/a565bd5defd3a99e157698fcc6e23b25"
    assert revs["upload-urls"] == {
        "conanfile.py": {
            "url": f"{c.servers['default']}/{base_url}/files/conanfile.py",
            "checksum": sha1sum(revs["files"]["conanfile.py"])
        },
        "conanmanifest.txt": {
            "url": f"{c.servers['default']}/{base_url}/files/conanmanifest.txt",
            "checksum": sha1sum(revs["files"]["conanmanifest.txt"])
        }
    }
    pkg_url = "9e0f8140f0fe6b967392f8d5da9881e232e05ff8/revisions/f50f552c6e04b1f241e5f7864bc3957f"
    assert prev["upload-urls"] == {
        "conan_package.tgz": {
            "url": f"{c.servers['default']}/{base_url}/packages/{pkg_url}/files/conan_package.tgz",
            "checksum": sha1sum(prev["files"]["conan_package.tgz"])
        },
        "conaninfo.txt": {
            "url": f"{c.servers['default']}/{base_url}/packages/{pkg_url}/files/conaninfo.txt",
            "checksum": sha1sum(prev["files"]["conaninfo.txt"])
        },
        "conanmanifest.txt": {
            "url": f"{c.servers['default']}/{base_url}/packages/{pkg_url}/files/conanmanifest.txt",
            "checksum": sha1sum(prev["files"]["conanmanifest.txt"])
        }
    }

    if dry_run:
        # check we don't have anything about the upload-urls in the text formatter
        c.run("upload * -r=default -c --dry-run")
        assert "upload-urls" not in c.out
        assert "url:" not in c.out
        assert "checksum:" not in c.out
