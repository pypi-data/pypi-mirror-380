import textwrap

import pytest

from conan.test.utils.tools import TestClient, GenConanfile


PKG_ID_1 = "47b42eaf657374a3d040394f03961b66c53bda5e"
PKG_ID_2 = "8b7006bf91e5b52cc1ac24a7a4d9c326ee954bb2"


class TestPythonRequiresPackageID:

    @pytest.fixture(autouse=True)
    def set_up(self):
        client = TestClient()
        client.save({"conanfile.py": GenConanfile()})
        client.run("export . --name=tool --version=1.1.1")
        conanfile = textwrap.dedent("""
            from conan import ConanFile
            class Pkg(ConanFile):
                python_requires ="tool/[*]"
            """)
        client2 = TestClient(cache_folder=client.cache_folder)
        client2.save({"conanfile.py": conanfile})
        self.client = client
        self.client2 = client2

    def test_default(self):
        self.client2.run("create . --name=pkg --version=0.1")
        assert "tool/1.1.1" in self.client2.out
        pkg_id = "170e82ef3a6bf0bbcda5033467ab9d7805b11d0b"
        self.client2.assert_listed_binary({"pkg/0.1": (pkg_id, "Build")})

        self.client.run("export . --name=tool --version=1.1.2")
        self.client2.run("create . --name=pkg --version=0.1")
        assert "tool/1.1.2" in self.client2.out
        self.client2.assert_listed_binary({"pkg/0.1": (pkg_id,
                                                       "Build")})

        # With a minor change, it fires a rebuild
        self.client.run("export . --name=tool --version=1.2.0")
        self.client2.run("create . --name=pkg --version=0.1")
        assert "tool/1.2.0" in self.client2.out
        self.client2.assert_listed_binary({"pkg/0.1": ("5eb1e7ea93fdd67fe3c3b166d240844648ba2b7a",
                                                       "Build")})

    def test_change_mode_conf(self):
        # change the policy in conan.conf
        self.client2.save_home({"global.conf": "core.package_id:default_python_mode=patch_mode"})
        self.client2.run("create . --name=pkg --version=0.1")
        assert "tool/1.1.1" in self.client2.out
        self.client2.assert_listed_binary({"pkg/0.1": (PKG_ID_1, "Build")})

        # with a patch change, new ID
        self.client.run("export . --name=tool --version=1.1.2")
        self.client2.run("create . --name=pkg --version=0.1")
        assert "tool/1.1.2" in self.client2.out
        self.client2.assert_listed_binary({"pkg/0.1": (PKG_ID_2,"Build")})

    def test_unrelated_conf(self):
        # change the policy in conan.conf
        self.client2.save_home({"global.conf": "core.package_id:default_python_mode=unrelated_mode"})
        self.client2.run("create . --name=pkg --version=0.1")
        assert "tool/1.1.1" in self.client2.out
        pkg_id = "da39a3ee5e6b4b0d3255bfef95601890afd80709"
        self.client2.assert_listed_binary({"pkg/0.1": (pkg_id, "Build")})

        # with any change the package id doesn't change
        self.client.run("export . --name=tool --version=1.1.2")
        self.client2.run("create . --name=pkg --version=0.1 --build missing")
        assert "tool/1.1.2" in self.client2.out
        self.client2.assert_listed_binary({"pkg/0.1": (pkg_id, "Cache")})

    def test_change_mode_package_id(self):
        # change the policy in package_id
        conanfile = textwrap.dedent("""
            from conan import ConanFile
            class Pkg(ConanFile):
                python_requires ="tool/[*]"
                def package_id(self):
                    self.info.python_requires.patch_mode()
            """)
        self.client2.save({"conanfile.py": conanfile})
        self.client2.run("create . --name=pkg --version=0.1")
        assert "tool/1.1.1" in self.client2.out
        self.client2.assert_listed_binary({"pkg/0.1": (PKG_ID_1, "Build")})

        # with a patch change, new ID
        self.client.run("export . --name=tool --version=1.1.2")
        self.client2.run("create . --name=pkg --version=0.1")
        assert "tool/1.1.2" in self.client2.out
        self.client2.assert_listed_binary({"pkg/0.1": (PKG_ID_2, "Build")})


def test_python_requires_for_build_requires():
    client = TestClient()
    client.save_home({"global.conf": "core.package_id:default_python_mode=full_version_mode"})
    client.save({"conanfile.py": GenConanfile()})
    client.run("create . --name=tool --version=1.1.1")

    client2 = TestClient(cache_folder=client.cache_folder)
    client2.save({"conanfile.py": GenConanfile().with_python_requires("tool/[>=0.0]"),
                 "myprofile": "[tool_requires]\ntool/[>=0.0]\n"})

    client2.run("create . --name=pkg --version=0.1 -pr=myprofile")
    assert "tool/1.1.1" in client2.out
    assert f"pkg/0.1: Package '{PKG_ID_1}' created" in client2.out

    client.run("create . --name=tool --version=1.1.2")
    client2.run("install --requires=pkg/0.1@ -pr=myprofile", assert_error=True)
    assert f"ERROR: Missing binary: pkg/0.1:{PKG_ID_2}" in client2.out
    assert "tool/1.1.2" in client2.out
    assert "tool/1.1.1" not in client2.out

    client2.run("create . --name=pkg --version=0.1 -pr=myprofile")
    # assert "pkg/0.1: Applying build-requirement: tool/1.1.2", client2.out)
    assert f"pkg/0.1: Package '{PKG_ID_2}' created" in client2.out


class TestPythonRequiresHeaderOnly:
    def test_header_only(self):
        c = TestClient(light=True)
        pkg = textwrap.dedent("""\
            from conan import ConanFile
            class Pkg(ConanFile):
                name = "pkg"
                version = "0.1"
                python_requires = "tool/[*]"
                def package_id(self):
                    self.info.clear()
                """)
        c.save({"tool/conanfile.py": GenConanfile("tool"),
                "pkg/conanfile.py": pkg})
        c.run("create tool --version=1.0")
        c.run("create pkg")
        pkgid = c.created_package_id("pkg/0.1")
        c.run("create tool --version=1.2")
        c.run("install --requires=pkg/0.1")
        c.assert_listed_binary({"pkg/0.1": (pkgid, "Cache")})

    def test_header_only_implements(self):
        c = TestClient(light=True)
        pkg = textwrap.dedent("""\
            from conan import ConanFile
            class Pkg(ConanFile):
                name = "pkg"
                version = "0.1"
                python_requires = "tool/[*]"
                package_type = "header-library"
                implements = ["auto_header_only"]
                """)
        c.save({"tool/conanfile.py": GenConanfile("tool"),
                "pkg/conanfile.py": pkg})
        c.run("create tool --version=1.0")
        c.run("create pkg")
        pkgid = c.created_package_id("pkg/0.1")
        c.run("create tool --version=1.2")
        c.run("install --requires=pkg/0.1")
        c.assert_listed_binary({"pkg/0.1": (pkgid, "Cache")})


@pytest.mark.parametrize("mode, pkg_id",
                         [("unrelated_mode", "da39a3ee5e6b4b0d3255bfef95601890afd80709"),
                          ("semver_mode", "1f0070b00ccebfec93dc90854a163c7af229f587"),
                          ("patch_mode", "b9ca872dfd5b48f5f1f69d66f0950fc35469d0cd"),
                          ("minor_mode", "c53bd9e48dd09ceeaa1bb425830490d8b243e39c"),
                          ("major_mode", "331c17383dcdf37f79bc2b86fa55ac56afdc6fec"),
                          ("full_version_mode", "1f0070b00ccebfec93dc90854a163c7af229f587"),
                          ("revision_mode", "0071dd0296afa0db533e21f924273485c87f0d32"),
                          ("full_mode", "0071dd0296afa0db533e21f924273485c87f0d32")])
def test_modes(mode, pkg_id):
    c = TestClient(light=True)
    c.save_home({"global.conf": f"core.package_id:default_python_mode={mode}"})
    c.save({"dep/conanfile.py": GenConanfile("dep", "0.1.1.1"),
            "pkg/conanfile.py": GenConanfile("pkg", "0.1").with_python_requires("dep/[*]")})
    c.run("create dep")
    c.run("create pkg")
    pkgid = c.created_package_id("pkg/0.1")
    assert pkgid == pkg_id
