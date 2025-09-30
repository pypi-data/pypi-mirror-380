import os
import platform
import textwrap
import re

import pytest

from conan.test.assets.genconanfile import GenConanfile
from conan.test.utils.tools import TestClient
from conan.internal.util.files import save, load


@pytest.mark.parametrize("os_", ["Macos", "Linux", "Windows"])
def test_extra_flags_via_conf(os_):
    os_sdk = "tools.apple:sdk_path=/my/sdk/path" if os_ == "Macos" else ""
    profile = textwrap.dedent(f"""
        [settings]
        os={os_}
        compiler=gcc
        compiler.version=6
        compiler.libcxx=libstdc++11
        arch=armv8
        build_type=Release

        [conf]
        tools.build:cxxflags=["--flag1", "--flag2"]
        tools.build:cflags+=["--flag3", "--flag4"]
        tools.build:sharedlinkflags+=["--flag5"]
        tools.build:exelinkflags+=["--flag6"]
        tools.build:defines+=["DEF1", "DEF2"]
        {os_sdk}
        """)
    client = TestClient()
    conanfile = GenConanfile().with_settings("os", "arch", "compiler", "build_type") \
        .with_generator("GnuToolchain")
    client.save({"conanfile.py": conanfile,
                 "profile": profile})
    client.run("install . --profile:build=profile --profile:host=profile")
    toolchain = client.load(
        "conangnutoolchain{}".format('.bat' if os_ == "Windows" else '.sh'))
    if os_ == "Windows":
        assert 'set "CPPFLAGS=%CPPFLAGS% -DNDEBUG -DDEF1 -DDEF2"' in toolchain
        assert 'set "CXXFLAGS=%CXXFLAGS% -O3 --flag1 --flag2"' in toolchain
        assert 'set "CFLAGS=%CFLAGS% -O3 --flag3 --flag4"' in toolchain
        assert 'set "LDFLAGS=%LDFLAGS% --flag5 --flag6"' in toolchain
        assert f'set "PKG_CONFIG_PATH={client.current_folder};%PKG_CONFIG_PATH%"' in toolchain
    elif os_ == "Linux":
        assert 'export CPPFLAGS="$CPPFLAGS -DNDEBUG -DDEF1 -DDEF2"' in toolchain
        assert 'export CXXFLAGS="$CXXFLAGS -O3 --flag1 --flag2"' in toolchain
        assert 'export CFLAGS="$CFLAGS -O3 --flag3 --flag4"' in toolchain
        assert 'export LDFLAGS="$LDFLAGS --flag5 --flag6"' in toolchain
        assert f'export PKG_CONFIG_PATH="{client.current_folder}:$PKG_CONFIG_PATH"' in toolchain
    else:  # macOS
        assert 'export CPPFLAGS="$CPPFLAGS -DNDEBUG -DDEF1 -DDEF2"' in toolchain
        assert 'export CXXFLAGS="$CXXFLAGS -O3 --flag1 --flag2"' in toolchain
        assert 'export CFLAGS="$CFLAGS -O3 --flag3 --flag4"' in toolchain
        assert 'export LDFLAGS="$LDFLAGS --flag5 --flag6"' in toolchain
        assert f'export PKG_CONFIG_PATH="{client.current_folder}:$PKG_CONFIG_PATH"' in toolchain


def test_extra_flags_order():
    client = TestClient()
    conanfile = textwrap.dedent("""
        from conan import ConanFile
        from conan.tools.gnu import GnuToolchain

        class Conan(ConanFile):
            name = "pkg"
            version = "0.1"
            settings = "os", "arch", "build_type"
            def generate(self):
                at = GnuToolchain(self)
                at.extra_cxxflags = ["extra_cxxflags"]
                at.extra_cflags = ["extra_cflags"]
                at.extra_ldflags = ["extra_ldflags"]
                at.extra_defines = ["extra_defines"]
                at.generate()
        """)
    profile = textwrap.dedent("""
        include(default)
        [conf]
        tools.build:cxxflags+=['cxxflags']
        tools.build:cflags+=['cflags']
        tools.build:sharedlinkflags+=['sharedlinkflags']
        tools.build:exelinkflags+=['exelinkflags']
        tools.build:defines+=['defines']
        """)
    client.save({"conanfile.py": conanfile, "profile": profile})
    client.run('install . -pr=./profile')
    toolchain = client.load(
        "conangnutoolchain{}".format('.bat' if platform.system() == "Windows" else '.sh'))

    assert '-Dextra_defines -Ddefines' in toolchain
    assert 'extra_cxxflags cxxflags' in toolchain
    assert 'extra_cflags cflags' in toolchain
    assert 'extra_ldflags sharedlinkflags exelinkflags' in toolchain


def test_autotools_custom_environment():
    client = TestClient()
    conanfile = textwrap.dedent("""
            from conan import ConanFile
            from conan.tools.gnu import GnuToolchain

            class Conan(ConanFile):
                settings = "os"
                def generate(self):
                    at = GnuToolchain(self)
                    env = at.extra_env
                    env.define("FOO", "BAR")
                    at.generate()
            """)

    client.save({"conanfile.py": conanfile})
    client.run("install . -s:b os=Linux -s:h os=Linux")
    content = load(os.path.join(client.current_folder, "conangnutoolchain.sh"))
    assert 'export FOO="BAR"' in content


@pytest.mark.parametrize("os_", ["Linux", "Windows"])
def test_linker_scripts_via_conf(os_):
    profile = textwrap.dedent("""
        [settings]
        os=%s
        compiler=gcc
        compiler.version=6
        compiler.libcxx=libstdc++11
        arch=armv8
        build_type=Release

        [conf]

        tools.build:sharedlinkflags+=["--flag5"]
        tools.build:exelinkflags+=["--flag6"]
        tools.build:linker_scripts+=["/linker/scripts/flash.ld", "/linker/scripts/extra_data.ld"]
        """ % os_)
    client = TestClient()
    conanfile = GenConanfile().with_settings("os", "arch", "compiler", "build_type") \
        .with_generator("GnuToolchain")
    client.save({"conanfile.py": conanfile,
                 "profile": profile})
    client.run("install . --profile:build=profile --profile:host=profile")
    toolchain = client.load(
        "conangnutoolchain{}".format('.bat' if os_ == "Windows" else '.sh'))
    if os_ == "Windows":
        assert 'set "LDFLAGS=%LDFLAGS% --flag5 --flag6 -T\'/linker/scripts/flash.ld\' -T\'/linker/scripts/extra_data.ld\'"' in toolchain
    else:
        assert 'export LDFLAGS="$LDFLAGS --flag5 --flag6 -T\'/linker/scripts/flash.ld\' -T\'/linker/scripts/extra_data.ld\'"' in toolchain


def test_not_none_values():
    conanfile = textwrap.dedent("""
        from conan import ConanFile
        from conan.tools.gnu import GnuToolchain

        class Foo(ConanFile):
            name = "foo"
            version = "1.0"

            def generate(self):
                tc = GnuToolchain(self)
                assert None not in tc.defines
                assert None not in tc.cxxflags
                assert None not in tc.cflags
                assert None not in tc.ldflags

    """)

    client = TestClient()
    client.save({"conanfile.py": conanfile})
    client.run("install .")


def test_set_prefix():
    conanfile = textwrap.dedent("""
        from conan import ConanFile
        from conan.tools.gnu import GnuToolchain
        from conan.tools.layout import basic_layout


        class Foo(ConanFile):
            name = "foo"
            version = "1.0"
            def layout(self):
                basic_layout(self)
            def generate(self):
                at_toolchain = GnuToolchain(self, prefix="/somefolder")
                at_toolchain.generate()
    """)

    client = TestClient()
    client.save({"conanfile.py": conanfile})
    client.run("install .")
    conanbuild = client.load(
        os.path.join(client.current_folder, "build", "conan", "conanbuild.conf"))
    assert "--prefix=/somefolder" in conanbuild
    assert conanbuild.count("--prefix") == 1


def test_unknown_compiler():
    client = TestClient()
    save(client.paths.settings_path_user, "compiler:\n  xlc:\n")
    client.save({"conanfile.py": GenConanfile().with_settings("compiler", "build_type")
                .with_generator("GnuToolchain")
                 })
    # this used to crash, because of build_type_flags in GnuToolchain returning empty string
    client.run("install . -s compiler=xlc")
    assert "conanfile.py: Generator 'GnuToolchain' calling 'generate()'" in client.out


def test_toolchain_and_compilers_build_context():
    """
    Tests how GnuToolchain manages the build context profile if the build profile is
    specifying another compiler path (using conf)

    Issue related: https://github.com/conan-io/conan/issues/15878
    """
    host = textwrap.dedent("""
    [settings]
    arch=armv8
    build_type=Release
    compiler=gcc
    compiler.cppstd=gnu17
    compiler.libcxx=libstdc++11
    compiler.version=11
    os=Linux

    [conf]
    tools.build:compiler_executables={"c": "gcc", "cpp": "g++", "rc": "windres"}
    """)
    build = textwrap.dedent("""
    [settings]
    os=Linux
    arch=x86_64
    compiler=clang
    compiler.version=12
    compiler.libcxx=libc++
    compiler.cppstd=11

    [conf]
    tools.build:compiler_executables={"c": "clang", "cpp": "clang++"}
    """)
    tool = textwrap.dedent("""
    import os
    from conan import ConanFile
    from conan.tools.files import load

    class toolRecipe(ConanFile):
        name = "tool"
        version = "1.0"
        # Binary configuration
        settings = "os", "compiler", "build_type", "arch"
        generators = "GnuToolchain"

        def build(self):
            toolchain = os.path.join(self.generators_folder, "conangnutoolchain.sh")
            content = load(self, toolchain)
            assert 'export CC="clang"' in content
            assert 'export CXX="clang++"' in content
    """)
    consumer = textwrap.dedent("""
    import os
    from conan import ConanFile
    from conan.tools.files import load

    class consumerRecipe(ConanFile):
        name = "consumer"
        version = "1.0"
        # Binary configuration
        settings = "os", "compiler", "build_type", "arch"
        generators = "GnuToolchain"
        tool_requires = "tool/1.0"

        def build(self):
            toolchain = os.path.join(self.generators_folder, "conangnutoolchain.sh")
            content = load(self, toolchain)
            assert 'export CC="gcc"' in content
            assert 'export CXX="g++"' in content
            assert 'export RC="windres"' in content
            # Issue: https://github.com/conan-io/conan/issues/15486
            assert 'export CC_FOR_BUILD="clang"' in content
            assert 'export CXX_FOR_BUILD="clang++"' in content
    """)
    client = TestClient()
    client.save({
        "host": host,
        "build": build,
        "tool/conanfile.py": tool,
        "consumer/conanfile.py": consumer
    })
    client.run("export tool")
    client.run("create consumer -pr:h host -pr:b build --build=missing")


def test_autotools_crossbuild_ux():
    client = TestClient()
    profile_build = textwrap.dedent("""
        [settings]
        os = Macos
        os.version=10.11
        arch = armv7
        compiler = apple-clang
        compiler.version = 12.0
        compiler.libcxx = libc++
        """)
    profile_host = textwrap.dedent("""
        [settings]
        arch=x86_64
        build_type=Release
        compiler=apple-clang
        compiler.cppstd=gnu17
        compiler.libcxx=libc++
        compiler.version=15
        os=Macos
        [conf]
        tools.apple:sdk_path=/my/sdk/path
        """)
    conanfile = textwrap.dedent("""
    from conan import ConanFile
    from conan.tools.gnu import GnuToolchain
    from conan.tools.build import cross_building
    class Pkg(ConanFile):
        settings = "os", "arch", "compiler", "build_type"
        def generate(self):
            tc = GnuToolchain(self)
            if cross_building(self):
                host_arch = tc.triplets_info["host"]["machine"]
                build_arch = tc.triplets_info["build"]["machine"]
                if host_arch and build_arch:
                    tc.configure_args["--host"] = f"{host_arch}-my-triplet-host"
                    tc.configure_args["--build"] = f"{build_arch}-my-triplet-build"
            tc.generate()
            """)

    client.save({"conanfile.py": conanfile,
                 "profile_build": profile_build,
                 "profile_host": profile_host})
    client.run("install . --profile:build=profile_build --profile:host=profile_host")
    conanbuild = client.load("conanbuild.conf")
    host_flags = re.findall(r"--host=[\w-]*\b", conanbuild)
    build_flags = re.findall(r"--build=[\w-]*\b", conanbuild)
    assert len(host_flags) == 1
    assert len(build_flags) == 1
    assert host_flags[0] == '--host=x86_64-my-triplet-host'
    assert build_flags[0] == '--build=arm-my-triplet-build'


def test_msvc_profile_defaults():
    """
    Tests how GnuToolchain manages MSVC profile and its default env variables.
    """
    profile = textwrap.dedent("""\
    [settings]
    os=Windows
    arch=x86_64
    compiler=msvc
    compiler.version=191
    compiler.runtime=dynamic
    build_type=Release

    [conf]
    tools.build:compiler_executables={"c": "clang", "cpp": "clang++"}
    # Fake installation path
    tools.microsoft.msbuild:installation_path={{os.getcwd()}}
    """)
    # Consumer with default values
    consumer = textwrap.dedent("""\
    import os
    from conan import ConanFile
    from conan.tools.files import load

    class consumerRecipe(ConanFile):
        name = "consumer"
        version = "1.0"
        # Binary configuration
        settings = "os", "compiler", "build_type", "arch"
        generators = "GnuToolchain"

        def build(self):
            toolchain = os.path.join(self.generators_folder, "conangnutoolchain.bat")
            content = load(self, toolchain)
            # Default values and conf ones
            assert r'set "CC=clang"' in content  # conf value has precedence
            assert r'set "CXX=clang++"' in content  # conf value has precedence
            assert 'set "NM=dumpbin -symbols"' in content
            assert 'set "OBJDUMP=:"' in content
            assert 'set "RANLIB=:"' in content
            assert 'set "STRIP=:"' in content
    """)
    client = TestClient()
    client.save({
        "profile": profile,
        "consumer/conanfile.py": consumer
    })
    client.run("create consumer -pr:a profile --build=missing")
    # Consumer changing default values
    consumer = textwrap.dedent("""\
    import os
    from conan import ConanFile
    from conan.tools.files import load
    from conan.tools.gnu import GnuToolchain

    class consumerRecipe(ConanFile):
        name = "consumer"
        version = "1.0"
        # Binary configuration
        settings = "os", "compiler", "build_type", "arch"

        def generate(self):
            tc = GnuToolchain(self)
            # Prepending compiler wrappers
            tc.extra_env.prepend("CC", "compile")
            tc.extra_env.prepend("CXX", "compile")
            tc.extra_env.define("OBJDUMP", "other-value")
            tc.extra_env.unset("RANLIB")
            tc.generate()

        def build(self):
            toolchain = os.path.join(self.generators_folder, "conangnutoolchain.bat")
            content = load(self, toolchain)
            # Default values
            assert r'set "CC=compile clang"' in content
            assert r'set "CXX=compile clang++"' in content
            assert 'set "NM=dumpbin -symbols"' in content
            assert 'set "OBJDUMP=other-value"' in content  # redefined
            assert 'set "RANLIB=:"' not in content  # removed
            assert 'set "STRIP=:"' in content
    """)
    client.save({
        "consumer/conanfile.py": consumer
    })
    client.run("create consumer -pr:a profile --build=missing")


def test_conf_build_does_not_exist():
    host = textwrap.dedent("""
    [settings]
    arch=x86_64
    os=Linux
    [conf]
    tools.build:compiler_executables={'c': '/usr/bin/gcc', 'cpp': '/usr/bin/g++'}
    """)
    build = textwrap.dedent("""
    [settings]
    arch=armv8
    os=Linux
    [conf]
    tools.build:compiler_executables={'c': 'x86_64-linux-gnu-gcc', 'cpp': 'x86_64-linux-gnu-g++'}
    """)
    c = TestClient()
    c.save({"conanfile.py": GenConanfile("pkg", "0.1"),
            "host": host,
            "build": build})
    c.run("export .")
    c.run("install --requires=pkg/0.1 --build=pkg/0.1 -g GnuToolchain -pr:h host -pr:b build")
    tc = c.load("conangnutoolchain.sh")
    assert 'export CC_FOR_BUILD="x86_64-linux-gnu-gcc"' in tc
    assert 'export CXX_FOR_BUILD="x86_64-linux-gnu-g++"' in tc


@pytest.mark.parametrize("toolchain", ["GnuToolchain", "AutotoolsToolchain"])
def test_conf_extra_apple_flags(toolchain):
    host = textwrap.dedent("""
    [settings]
    arch=x86_64
    os=Macos
    [conf]
    tools.apple:enable_bitcode = True
    tools.apple:enable_arc = True
    tools.apple:enable_visibility = True
    """)

    c = TestClient()
    c.save({"conanfile.txt": f"[generators]\n{toolchain}",
            "host": host})
    c.run("install . -pr:a host")
    f = "conanautotoolstoolchain.sh" if toolchain == "AutotoolsToolchain" else "conangnutoolchain.sh"
    tc = c.load(f)
    assert 'export CXXFLAGS="$CXXFLAGS -fembed-bitcode -fvisibility=default"' in tc
    assert 'export CFLAGS="$CFLAGS -fembed-bitcode -fvisibility=default"' in tc
    assert 'export LDFLAGS="$LDFLAGS -fembed-bitcode -fvisibility=default"' in tc
    assert 'export OBJCFLAGS="$OBJCFLAGS -fobjc-arc"' in tc
    assert 'export OBJCXXFLAGS="$OBJCXXFLAGS -fobjc-arc"' in tc

    c.run("install . -pr:a host -s build_type=Debug")
    tc = c.load(f)
    assert 'export CXXFLAGS="$CXXFLAGS -fembed-bitcode-marker -fvisibility=default"' in tc
    assert 'export CFLAGS="$CFLAGS -fembed-bitcode-marker -fvisibility=default"' in tc
    assert 'export LDFLAGS="$LDFLAGS -fembed-bitcode-marker -fvisibility=default"' in tc
    assert 'export OBJCFLAGS="$OBJCFLAGS -fobjc-arc"' in tc
    assert 'export OBJCXXFLAGS="$OBJCXXFLAGS -fobjc-arc"' in tc

    host = textwrap.dedent("""
        [settings]
        arch=x86_64
        os=Macos
        [conf]
        tools.apple:enable_bitcode = False
        tools.apple:enable_arc = False
        tools.apple:enable_visibility = False
        """)

    c.save({"host": host})
    c.run("install . -pr:a host")
    tc = c.load(f)
    assert 'CXXFLAGS="$CXXFLAGS -fvisibility=hidden -fvisibility-inlines-hidden"' in tc
    assert 'CFLAGS="$CFLAGS -fvisibility=hidden -fvisibility-inlines-hidden"' in tc
    assert 'LDFLAGS="$LDFLAGS -fvisibility=hidden -fvisibility-inlines-hidden"' in tc
    assert 'export OBJCFLAGS="$OBJCFLAGS -fno-objc-arc"' in tc
    assert 'export OBJCXXFLAGS="$OBJCXXFLAGS -fno-objc-arc"' in tc


def test_toolchain_crossbuild_to_android():
    """
    Issue related: https://github.com/conan-io/conan/issues/17441
    """
    build = textwrap.dedent("""
    [settings]
    arch=armv8
    build_type=Release
    compiler=gcc
    compiler.cppstd=gnu17
    compiler.libcxx=libstdc++11
    compiler.version=11
    os=Linux
    """)
    host = textwrap.dedent("""
    [settings]
    os = Android
    os.api_level = 21
    arch=x86_64
    compiler=clang
    compiler.version=12
    compiler.libcxx=libc++
    compiler.cppstd=11

    [buildenv]
    CC=clang
    CXX=clang++

    [conf]
    tools.android:ndk_path=/path/to/ndk
    """)
    consumer = textwrap.dedent("""
    import os
    from conan import ConanFile
    from conan.tools.files import load

    class consumerRecipe(ConanFile):
        name = "consumer"
        version = "1.0"
        settings = "os", "compiler", "build_type", "arch"
        generators = "GnuToolchain"

        def build(self):
            toolchain = os.path.join(self.generators_folder, "conangnutoolchain.sh")
            content = load(self, toolchain)
            assert 'export CC="clang"' not in content
            assert 'export CXX="clang++"' not in content
            assert 'export LD="/path/to/ndk' in content
            assert 'export STRIP="/path/to/ndk' in content
            assert 'export RANLIB="/path/to/ndk' in content
            assert 'export AS="/path/to/ndk' in content
            assert 'export AR="/path/to/ndk' in content
            assert 'export ADDR2LINE="/path/to/ndk' in content
            assert 'export NM="/path/to/ndk' in content
            assert 'export OBJCOPY="/path/to/ndk' in content
            assert 'export OBJDUMP="/path/to/ndk' in content
            assert 'export READELF="/path/to/ndk' in content
            assert 'export ELFEDIT="/path/to/ndk' in content

            build_env = os.path.join(self.generators_folder, "conanbuildenv-x86_64.sh")
            content = load(self, build_env)
            assert 'export CC="clang"' in content
            assert 'export CXX="clang++"' in content
            assert 'export LD=' not in content
            assert 'export STRIP="/path/to/ndk' not in content
            assert 'export RANLIB="/path/to/ndk' not in content
            assert 'export AS="/path/to/ndk' not in content
            assert 'export AR="/path/to/ndk' not in content
            assert 'export ADDR2LINE="/path/to/ndk' not in content
            assert 'export NM="/path/to/ndk' not in content
            assert 'export OBJCOPY="/path/to/ndk' not in content
            assert 'export OBJDUMP="/path/to/ndk' not in content
            assert 'export READELF="/path/to/ndk' not in content
            assert 'export ELFEDIT="/path/to/ndk' not in content
    """)
    client = TestClient()
    client.save({
        "host": host,
        "build": build,
        "conanfile.py": consumer
    })
    client.run("create . -pr:h host -pr:b build")


@pytest.mark.parametrize(
    "threads, flags",
    [("posix", "-pthread"), ("wasm_workers", "-sWASM_WORKERS=1")],
)
def test_thread_flags(threads, flags):
    client = TestClient()
    profile = textwrap.dedent(f"""
        [settings]
        arch=wasm
        build_type=Release
        compiler=emcc
        compiler.cppstd=17
        compiler.threads={threads}
        compiler.libcxx=libc++
        compiler.version=4.0.10
        os=Emscripten
        """)
    client.save(
        {
            "conanfile.py": GenConanfile("pkg", "1.0")
            .with_settings("os", "arch", "compiler", "build_type")
            .with_generator("GnuToolchain"),
            "profile": profile,
        }
    )
    client.run("install . -pr=./profile")
    os = platform.system()
    toolchain = client.load(
        "conangnutoolchain{}".format('.bat' if os == "Windows" else '.sh'))

    if os == "Windows":
        assert f'set "CXXFLAGS=%CXXFLAGS% -stdlib=libc++ {flags}"' in toolchain
        assert f'set "CFLAGS=%CFLAGS% {flags}"' in toolchain
        assert f'set "LDFLAGS=%LDFLAGS% {flags}' in toolchain
    else:
        assert f'export CXXFLAGS="$CXXFLAGS -stdlib=libc++ {flags}"' in toolchain
        assert f'export CFLAGS="$CFLAGS {flags}"' in toolchain
        assert f'export LDFLAGS="$LDFLAGS {flags}"' in toolchain
