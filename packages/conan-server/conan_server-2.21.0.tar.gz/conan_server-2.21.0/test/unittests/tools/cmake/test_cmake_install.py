import pytest

from conan.internal.default_settings import default_settings_yml
from conan.tools.cmake import CMake
from conan.tools.cmake.presets import write_cmake_presets
from conan.internal.model.conf import Conf
from conan.internal.model.settings import Settings
from conan.test.utils.mocks import ConanFileMock, RedirectedTestOutput
from conan.test.utils.test_files import temp_folder
from conan.test.utils.tools import redirect_output



def test_run_install_component():
    """
    Testing that the proper component is installed.
    Issue related: https://github.com/conan-io/conan/issues/10359
    """
    # Load some generic windows settings
    settings = Settings.loads(default_settings_yml)
    settings.os = "Windows"
    settings.arch = "x86"
    settings.build_type = "Release"
    settings.compiler = "msvc"
    settings.compiler.runtime = "dynamic"
    settings.compiler.version = "190"

    conanfile = ConanFileMock()
    conanfile.conf = Conf()
    conanfile.folders.generators = "."
    conanfile.folders.set_base_generators(temp_folder())
    conanfile.settings = settings
    conanfile.folders.set_base_package(temp_folder())

    # Choose generator to match generic settings
    write_cmake_presets(conanfile, "toolchain", "Visual Studio 14 2015", {})
    cmake = CMake(conanfile)
    cmake.install(component="foo")

    assert "--component foo" in conanfile.command


@pytest.mark.parametrize("config, deprecated",
                         [("tools.cmake:install_strip", True),
                          ("tools.build:install_strip", False),])
def test_run_install_strip(config, deprecated):
    """
    Testing that the install/strip rule is called
    Issue related: https://github.com/conan-io/conan/issues/14166
    """

    settings = Settings.loads(default_settings_yml)
    settings.os = "Linux"
    settings.arch = "x86_64"
    settings.build_type = "Release"
    settings.compiler = "gcc"
    settings.compiler.version = "11"

    conanfile = ConanFileMock()

    conanfile.conf = Conf()
    conanfile.conf.define(config, True)

    conanfile.folders.generators = "."
    conanfile.folders.set_base_generators(temp_folder())
    conanfile.settings = settings
    conanfile.folders.set_base_package(temp_folder())

    write_cmake_presets(conanfile, "toolchain", "Unix Makefiles", {})
    cmake = CMake(conanfile)
    stdout = RedirectedTestOutput()  # Initialize each command
    stderr = RedirectedTestOutput()
    with redirect_output(stderr, stdout):
        cmake.install(stdout=stdout, stderr=stderr)

    if deprecated:
        assert "WARN: deprecated: The 'tools.cmake:install_strip' configuration is deprecated, use"\
               " 'tools.build:install_strip' instead" in stderr
    else:
        assert "tools.cmake:install_strip" not in stderr
    assert "--strip" in conanfile.command

def test_run_install_cli_args():
    """
    Testing that the passing cli_args to install works
    Issue related: https://github.com/conan-io/conan/issues/14235
    """

    settings = Settings.loads(default_settings_yml)
    settings.os = "Linux"
    settings.arch = "x86_64"
    settings.build_type = "Release"
    settings.compiler = "gcc"
    settings.compiler.version = "11"

    conanfile = ConanFileMock()

    conanfile.conf = Conf()

    conanfile.folders.generators = "."
    conanfile.folders.set_base_generators(temp_folder())
    conanfile.settings = settings
    conanfile.folders.set_base_package(temp_folder())

    write_cmake_presets(conanfile, "toolchain", "Unix Makefiles", {})
    cmake = CMake(conanfile)
    cmake.install(cli_args=["--prefix=/tmp"])
    assert "--prefix=/tmp" in conanfile.command


def test_run_install_cli_args_strip():
    """
    Testing that the install/strip rule is called when using cli_args
    Issue related: https://github.com/conan-io/conan/issues/14235
    """

    settings = Settings.loads(default_settings_yml)
    settings.os = "Linux"
    settings.arch = "x86_64"
    settings.build_type = "Release"
    settings.compiler = "gcc"
    settings.compiler.version = "11"

    conanfile = ConanFileMock()

    conanfile.conf = Conf()

    conanfile.folders.generators = "."
    conanfile.folders.set_base_generators(temp_folder())
    conanfile.settings = settings
    conanfile.folders.set_base_package(temp_folder())

    write_cmake_presets(conanfile, "toolchain", "Unix Makefiles", {})
    cmake = CMake(conanfile)
    cmake.install(cli_args=["--strip"])
    assert "--strip" in conanfile.command
