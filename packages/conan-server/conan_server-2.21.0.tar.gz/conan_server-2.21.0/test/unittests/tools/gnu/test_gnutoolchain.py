import os
from unittest.mock import patch, MagicMock

import pytest

from conan.errors import ConanException
from conan.internal.model.conf import Conf
from conan.test.utils.mocks import ConanFileMock, MockSettings
from conan.test.utils.test_files import temp_folder
from conan.tools.build import cmd_args_to_string
from conan.tools.files import save
from conan.tools.gnu import GnuToolchain


@pytest.fixture()
def cross_building_conanfile():
    settings_build = MockSettings({"os": "Linux",
                                   "arch": "x86_64",
                                   "compiler": "gcc",
                                   "compiler.version": "11",
                                   "compiler.libcxx": "libstdc++",
                                   "build_type": "Release"})
    settings_target = MockSettings({"os": "Android", "arch": "armv8"})
    settings = MockSettings({"os": "Emscripten", "arch": "wasm"})
    conanfile = ConanFileMock()
    conanfile.settings = settings
    conanfile.settings_build = settings_build
    conanfile.settings_target = settings_target
    return conanfile


def test_get_gnu_triplet_for_cross_building():
    """
    Testing AutotoolsToolchainX and _get_gnu_triplet() function in case of
    having os=Windows and cross compiling
    """
    # Issue: https://github.com/conan-io/conan/issues/10139
    settings = MockSettings({"build_type": "Release",
                             "compiler": "gcc",
                             "compiler.version": "10.2",
                             "os": "Windows",
                             "arch": "x86_64"})
    conanfile = ConanFileMock()
    conanfile.settings = settings
    conanfile.settings_build = MockSettings({"os": "Solaris", "arch": "x86"})
    at = GnuToolchain(conanfile)
    assert at.configure_args["--host"] == "x86_64-w64-mingw32"
    assert at.configure_args["--build"] == "i686-solaris"


def test_get_toolchain_cppstd():
    settings = MockSettings({"build_type": "Release",
                             "compiler": "gcc",
                             "compiler.version": "9",
                             "compiler.cppstd": "20",
                             "os": "Linux",
                             "arch": "x86_64"})
    conanfile = ConanFileMock()
    conanfile.settings = settings
    conanfile.settings_build = settings
    at = GnuToolchain(conanfile)
    assert at.cppstd == "-std=c++2a"
    settings.values["compiler.version"] = "10"
    at = GnuToolchain(conanfile)
    assert at.cppstd == "-std=c++20"


@pytest.mark.parametrize("runtime, runtime_type, expected",
                         [("static", "Debug", "MTd"),
                          ("static", "Release", "MT"),
                          ("dynamic", "Debug", "MDd"),
                          ("dynamic", "Release", "MD")])
def test_msvc_runtime(runtime, runtime_type, expected):
    """
    Testing AutotoolsToolchainX with the msvc compiler adjust the runtime
    """
    # Issue: https://github.com/conan-io/conan/issues/10139
    settings = MockSettings({"build_type": "Release",
                             "compiler": "msvc",
                             "compiler.runtime": runtime,
                             "compiler.runtime_type": runtime_type,
                             "os": "Windows",
                             "arch": "x86_64"})
    conanfile = ConanFileMock()
    conanfile.settings = settings
    conanfile.settings_build = settings
    at = GnuToolchain(conanfile)
    expected_flag = "-{}".format(expected)
    assert at.msvc_runtime_flag == expected_flag
    env = at._environment.vars(conanfile)
    assert expected_flag in env["CFLAGS"]
    assert expected_flag in env["CXXFLAGS"]


@pytest.mark.parametrize("runtime", ["MTd", "MT", "MDd", "MD"])
def test_visual_runtime(runtime):
    """
    Testing AutotoolsToolchainX with the msvc compiler adjust the runtime
    """
    # Issue: https://github.com/conan-io/conan/issues/10139
    settings = MockSettings({"build_type": "Release" if "d" not in runtime else "Debug",
                             "compiler": "msvc",
                             "compiler.runtime": "static" if "MT" in runtime else "dynamic",
                             "compiler.runtime_type": "Release" if "d" not in runtime else "Debug",
                             "os": "Windows",
                             "arch": "x86_64"})
    conanfile = ConanFileMock()
    conanfile.settings = settings
    conanfile.settings_build = settings
    at = GnuToolchain(conanfile)
    expected_flag = "-{}".format(runtime)
    assert at.msvc_runtime_flag == expected_flag
    env = at._environment.vars(conanfile)
    assert expected_flag in env["CFLAGS"]
    assert expected_flag in env["CXXFLAGS"]


def test_get_gnu_triplet_for_cross_building_raise_error():
    """
    Testing AutotoolsToolchainX and _get_gnu_triplet() function raises an error in case of
    having os=Windows, cross compiling and not defined any compiler
    """
    # Issue: https://github.com/conan-io/conan/issues/10139
    settings = MockSettings({"build_type": "Release",
                             "os": "Windows",
                             "arch": "x86_64"})
    conanfile = ConanFileMock()
    conanfile.settings = settings
    conanfile.settings_build = MockSettings({"os": "Solaris", "arch": "x86"})
    with pytest.raises(ConanException) as conan_error:
        GnuToolchain(conanfile)
    msg = "'compiler' parameter for 'get_gnu_triplet()' is not specified and needed for os=Windows"
    assert msg == str(conan_error.value)


def test_compilers_mapping():
    autotools_mapping = {"c": "CC", "cpp": "CXX", "cuda": "NVCC", "fortran": "FC"}
    compilers = {"c": "path_to_c", "cpp": "path_to_cpp", "cuda": "path_to_cuda",
                 "fortran": "path_to_fortran"}
    settings = MockSettings({"build_type": "Release",
                             "os": "Windows",
                             "arch": "x86_64",
                             "compiler": "gcc"})
    conanfile = ConanFileMock()
    conanfile.conf = Conf()
    conanfile.conf.define("tools.build:compiler_executables", compilers)
    conanfile.settings = settings
    at = GnuToolchain(conanfile)
    env = at._environment.vars(conanfile)
    for compiler, env_var in autotools_mapping.items():
        assert env[env_var] == f"path_to_{compiler}"


def test_linker_scripts():
    conanfile = ConanFileMock()
    conanfile.conf = Conf()
    conanfile.conf.define("tools.build:linker_scripts", ["path_to_first_linker_script", "path_to_second_linker_script"])
    settings = MockSettings({"build_type": "Release",
                             "os": "Windows",
                             "compiler": "gcc",
                             "arch": "x86_64"})
    conanfile.settings = settings
    at = GnuToolchain(conanfile)
    env = at._environment.vars(conanfile)
    assert "-T'path_to_first_linker_script'" in env["LDFLAGS"]
    assert "-T'path_to_second_linker_script'" in env["LDFLAGS"]


def test_update_or_prune_any_args(cross_building_conanfile):
    # Issue: https://github.com/conan-io/conan/issues/12642
    at = GnuToolchain(cross_building_conanfile)
    at.configure_args.update({
        "--with-cross-build": "my_path",
        "--something-host": "my_host",
        "--prefix": "/my/other/prefix"
    })
    new_configure_args = cmd_args_to_string(GnuToolchain._dict_to_list(at.configure_args))
    assert "--build=x86_64-linux-gnu" in new_configure_args
    assert "--host=wasm32-local-emscripten" in new_configure_args
    assert "--with-cross-build=my_path" in new_configure_args
    assert "--something-host=my_host" in new_configure_args
    assert "--prefix=/my/other/prefix" in new_configure_args
    # https://github.com/conan-io/conan/issues/12431
    at.configure_args.pop("--build")
    at.configure_args.pop("--host")
    new_configure_args = cmd_args_to_string(GnuToolchain._dict_to_list(at.configure_args))
    assert "--build=x86_64-linux-gnu" not in new_configure_args  # removed
    assert "--host=wasm32-local-emscripten" not in new_configure_args  # removed
    assert "--with-cross-build=my_path" in new_configure_args
    assert "--something-host=my_host" in new_configure_args
    # Update autoreconf_args
    at.autoreconf_args.pop("--force")
    new_autoreconf_args = cmd_args_to_string(GnuToolchain._dict_to_list(at.autoreconf_args))
    assert "'--force" not in new_autoreconf_args
    # Add new value to make_args
    at.make_args.update({"--new-complex-flag": "new-value"})
    at.make_args.update({"--new-empty-flag": ""})
    at.make_args.update({"--new-no-value-flag": None})
    new_make_args = cmd_args_to_string(GnuToolchain._dict_to_list(at.make_args))
    assert "--new-complex-flag=new-value" in new_make_args
    assert "--new-empty-flag=" in new_make_args
    assert "--new-no-value-flag" in new_make_args and "--new-no-value-flag=" not in new_make_args


@patch("conan.tools.gnu.gnutoolchain.VirtualBuildEnv")
def test_crossbuild_to_android(build_env_mock):
    """
    Issue related: https://github.com/conan-io/conan/issues/17441
    """
    buildvars = MagicMock()
    # VirtualBuildEnv defines these variables
    buildvars.vars.return_value = {"CC": "my-clang", "CXX": "my-clang++"}
    build_env_mock.return_value = buildvars

    conanfile = ConanFileMock()
    conanfile.settings = MockSettings({"os": "Android", "arch": "armv8", "os.api_level": "26r"})
    conanfile.settings_build = MockSettings({"os": "Macos", "arch": "armv8"})
    gnutc = GnuToolchain(conanfile)
    env_vars = gnutc.extra_env.vars(conanfile)
    assert env_vars.get("CC") is None
    assert env_vars.get("CXX") is None
    assert gnutc.triplets_info["host"]["triplet"] == "aarch64-linux-android"
    assert env_vars.get("LD") is None
    assert env_vars.get("STRIP") is None

    # Defining the ndk_path too
    ndk_path = temp_folder()
    ndk_bin = os.path.join(ndk_path, "toolchains", "llvm", "prebuilt", "darwin-x86_64", "bin")
    save(conanfile, os.path.join(ndk_bin, "ld"), "")
    conanfile.conf.define("tools.android:ndk_path", ndk_path)
    gnutc = GnuToolchain(conanfile)
    env_vars = gnutc.extra_env.vars(conanfile)
    assert env_vars.get("CC") is None
    assert env_vars.get("CXX") is None
    assert gnutc.triplets_info["host"]["triplet"] == "aarch64-linux-android"
    assert env_vars["LD"] == os.path.join(ndk_bin, "ld")  # exists
    assert env_vars["STRIP"] == os.path.join(ndk_bin, "llvm-strip")  # does not exist but appears


def test_gnu_toolchain_conf_extra_configure_args():
    """ Validate that tools.gnu:extra_configure_args are passed to the configure_args when
        building with GnuToolchain.
        The configure args should be passed as a list-like object.
    """
    conanfile = ConanFileMock()
    conanfile.settings = MockSettings({"os": "Linux", "arch": "x86_64"})
    conanfile.conf = Conf()
    conanfile.conf.define("tools.gnu:extra_configure_args", ["--foo", "--bar"])

    tc = GnuToolchain(conanfile)
    assert tc.configure_args["--foo"] is None
    assert tc.configure_args["--bar"] is None
