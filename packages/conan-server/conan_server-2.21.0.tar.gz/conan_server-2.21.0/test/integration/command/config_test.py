import json
import os
import textwrap

import pytest

from conan.api.conan_api import ConanAPI
from conan.test.assets.genconanfile import GenConanfile
from conan.internal.model.conf import BUILT_IN_CONFS
from conan.test.utils.test_files import temp_folder
from conan.test.utils.tools import TestClient
from conan.test.utils.env import environment_update


def test_missing_subarguments():
    """ config MUST run  with a subcommand. Otherwise, it MUST exits with error.
    """
    client = TestClient()
    client.run("config", assert_error=True)
    assert "ERROR: Exiting with code: 2" in client.out


class TestConfigHome:
    """ The test framework cannot test the CONAN_HOME env-var because it is not using it
    (it will break tests for maintainers that have the env-var defined)
    """
    def test_config_home_default(self):
        client = TestClient()
        client.run("config home")
        assert f"{client.cache_folder}\n" == client.stdout

        client.run("config home --format=text", assert_error=True)
        # It is not possible to use --format=text explicitly
        assert "--format=text" in client.out

    def test_api_uses_env_var_home(self):
        cache_folder = os.path.join(temp_folder(), "custom")
        with environment_update({"CONAN_HOME": cache_folder}):
            api = ConanAPI()
            assert api.cache_folder == cache_folder


def test_config_list():
    """
    'conan config list' shows all the built-in Conan configurations
    """
    client = TestClient()
    client.run("config list")
    for k, v in BUILT_IN_CONFS.items():
        assert f"{k}: {v}" in client.out
    client.run("config list --format=json")
    assert f"{json.dumps(BUILT_IN_CONFS, indent=4)}\n" == client.stdout

    client.run("config list cmake")
    assert "tools.cmake:cmake_program: Path to CMake executable" in client.out
    assert "core.download:parallel" not in client.out
    assert "tools.build:verbosity" not in client.out


def test_config_install():
    tc = TestClient()
    tc.save({'config/foo': ''})
    # This should not fail (insecure flag exists)
    tc.run("config install config --insecure")
    assert "foo" in os.listdir(tc.cache_folder)
    # Negative test, ensure we would be catching a missing arg if it did not exist
    tc.run("config install config --superinsecure", assert_error=True)


def test_config_install_conanignore():
    tc = TestClient()
    conanignore = textwrap.dedent("""
    a/*  # This is a tests
    b/c/*
    d/*
    tests/*
    # Next line is commented out, so it should be ignored
    # other_tests/*
    !b/c/important_file
    !b/c/important_folder/*
    """)
    tc.save({
        'config_folder/.conanignore': conanignore,
        'config_folder/a/test': '',
        'config_folder/abracadabra': '',
        'config_folder/b/bison': '',
        'config_folder/b/a/test2': '',
        'config_folder/b/c/helmet': '',
        'config_folder/b/c/important_file': '',
        'config_folder/b/c/important_folder/contents': '',
        'config_folder/d/prix': '',
        'config_folder/d/foo/bar': '',
        'config_folder/foo': '',
        'config_folder/tests/tester': '',
        'config_folder/other_tests/tester2': ''
    })

    def _assert_config_exists(path):
        assert os.path.exists(os.path.join(tc.cache_folder, path))

    def _assert_config_not_exists(path):
        assert not os.path.exists(os.path.join(tc.cache_folder, path))

    tc.run('config install config_folder')

    _assert_config_not_exists(".conanignore")

    _assert_config_not_exists("a")
    _assert_config_not_exists("a/test")

    _assert_config_exists("abracadabra")

    _assert_config_exists("b")
    _assert_config_exists("b/bison")
    _assert_config_exists("b/a/test2")
    _assert_config_not_exists("b/c/helmet")

    _assert_config_exists("b/c")
    _assert_config_exists("b/c/important_file")
    _assert_config_exists("b/c/important_folder/contents")

    _assert_config_not_exists("d/prix")
    _assert_config_not_exists("d/foo/bar")
    _assert_config_not_exists("d")

    _assert_config_exists("foo")

    _assert_config_not_exists("tests/tester")
    _assert_config_exists("other_tests/tester2")


def test_config_install_conanignore_ignore_all_allow_specific_workflow():
    tc = TestClient()
    conanignore = textwrap.dedent("""
    *
    !important_folder/*
    !important_file
    # We can even include the conanignore that we skip by default!
    !.conanignore
    """)
    tc.save({
        'config_folder/.conanignore': conanignore,
        'config_folder/a/test': '',
        'config_folder/abracadabra': '',
        'config_folder/important_folder/contents': '',
        'config_folder/important_file': '',
    })

    def _assert_config_exists(path):
        assert os.path.exists(os.path.join(tc.cache_folder, path))

    def _assert_config_not_exists(path):
        assert not os.path.exists(os.path.join(tc.cache_folder, path))

    tc.run('config install config_folder')

    _assert_config_exists(".conanignore")

    _assert_config_not_exists("a")
    _assert_config_not_exists("abracadabra")

    _assert_config_exists("important_folder/contents")
    _assert_config_exists("important_file")


@pytest.mark.parametrize("has_conanignore", [True, False])
@pytest.mark.parametrize("folder", [None, "myfolder", "myfolder/subfolder"])
def test_config_install_conanignore_walk_directories(has_conanignore, folder):
    tc = TestClient(light=True)
    if has_conanignore:
        conanignore = "*"
        tc.save({"config_folder/.conanignore": conanignore})
    tc.save({"config_folder/myfolder/subfolder/item.py": ""})

    folder_arg = f"-sf {folder} -tf {folder}" if folder else ""

    tc.run(f"config install config_folder {folder_arg}")
    if has_conanignore:
        assert not os.path.exists(os.path.join(tc.cache_folder, "myfolder", "subfolder", "item.py"))
    else:
        assert os.path.exists(os.path.join(tc.cache_folder, "myfolder", "subfolder", "item.py"))


def test_config_show():
    globalconf = textwrap.dedent("""
    tools.build:jobs=42
    tools.files.download:retry_wait=10
    tools.files.download:retry=7
    core.net.http:timeout=30
    core.net.http:max_retries=5
    zlib/*:user.mycategory:retry=True
    zlib/*:user.mycategory:foo=0
    zlib/*:user.myothercategory:foo=0
    """)
    tc = TestClient()
    tc.save_home({"global.conf": globalconf})
    tc.run("config show tools.build:jobs")
    assert "42" in tc.out

    tc.run("config show core*")
    assert "core.net.http:timeout" in tc.out
    assert "30" in tc.out
    assert "core.net.http:max_retries" in tc.out
    assert "5" in tc.out

    tc.run("config show *retr*")
    assert "tools.files.download:retry_wait" in tc.out
    assert "tools.files.download:retry" in tc.out
    assert "core.net.http:max_retries" in tc.out
    assert "zlib/*:user.mycategory:retry" in tc.out

    tc.run("config show zlib*")
    assert "zlib/*:user.mycategory:retry" in tc.out
    assert "zlib/*:user.mycategory:foo" in tc.out
    assert "zlib/*:user.myothercategory:foo" in tc.out

    tc.run("config show zlib/*")
    assert "zlib/*:user.mycategory:retry" in tc.out
    assert "zlib/*:user.mycategory:foo" in tc.out
    assert "zlib/*:user.myothercategory:foo" in tc.out

    tc.run("config show zlib/*:foo")
    assert "zlib/*:user.mycategory:foo" in tc.out
    assert "zlib/*:user.myothercategory:foo" in tc.out


@pytest.mark.parametrize("storage_path", [None, "p", "../foo"])
def test_config_clean(storage_path):
    tc = TestClient(light=True)
    absolut_storage_path = os.path.abspath(os.path.join(tc.current_folder, storage_path)) if storage_path else os.path.join(tc.cache_folder, "p")

    storage = f"core.cache:storage_path={storage_path}" if storage_path else ""
    tc.save_home({"global.conf": f"core.upload:retry=7\n{storage}",
                  "extensions/compatibility/mycomp.py": "",
                  "extensions/commands/cmd_foo.py": "",
                  })

    tc.run("profile detect --name=foo")
    tc.run("remote add bar http://fakeurl")

    tc.save({"conanfile.py": GenConanfile("pkg", "0.1")})
    tc.run("create .")

    assert os.path.exists(absolut_storage_path)

    tc.run("config clean")
    tc.run("profile list")
    assert "foo" not in tc.out
    tc.run("remote list")
    assert "bar" not in tc.out
    tc.run("config show core.upload:retry")
    assert "7" not in tc.out
    assert os.path.exists(os.path.join(tc.cache_folder, "extensions"))
    assert not os.path.exists(os.path.join(tc.cache_folder, "extensions", "compatibility", "mycomp.py"))
    assert os.path.exists(absolut_storage_path)
    # This will error because the call to clean will remove the profiles
    tc.run("create .", assert_error=True)
    # Works after regenerating them!
    tc.run("profile detect")
    tc.run("create .")


def test_config_reinit():
    custom_global_conf = "core.upload:retry=7"
    global_conf_folder = temp_folder()
    with open(os.path.join(global_conf_folder, "global.conf"), "w") as f:
        f.write(custom_global_conf)

    cache_folder = temp_folder()
    conan_api = ConanAPI(cache_folder=cache_folder)
    assert conan_api._api_helpers.global_conf.get("core.upload:retry", check_type=int) != 7

    conan_api.config.install(global_conf_folder, verify_ssl=False)
    # Already has an effect, the config installation reinitializes the config
    assert conan_api._api_helpers.global_conf.get("core.upload:retry", check_type=int) == 7


def test_config_reinit_core_conf():
    tc = TestClient(light=True)
    tc.save_home({"extensions/commands/cmd_foo.py": textwrap.dedent("""
        from conan.cli.command import conan_command
        from conan.api.output import ConanOutput

        @conan_command()
        def foo(conan_api, parser, *args, **kwargs):
            ''' Foo '''
            parser.parse_args(*args)
            ConanOutput().info(f"Retry: {conan_api.config.get('core.upload:retry', check_type=int)}")
    """)})
    tc.run("foo -cc core.upload:retry=7")
    assert "Retry: 7" in tc.out
