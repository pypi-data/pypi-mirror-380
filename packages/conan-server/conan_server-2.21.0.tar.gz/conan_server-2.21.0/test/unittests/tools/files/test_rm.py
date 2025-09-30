import os
import pytest

# Check it is importable from tools
from conan.tools.files import rm, chdir
from conan.test.utils.test_files import temp_folder
from conan.internal.util.files import save_files


def test_remove_files_by_mask_recursively():
    temp_dir = temp_folder()

    with chdir(None, temp_dir):
        os.makedirs("subdir")
        os.makedirs("dir.pdb")
        os.makedirs(os.path.join("subdir", "deepdir"))

    save_files(temp_dir, {"1.txt": "",
                        "1.pdb": "",
                        "1.pdb1": "",
                        os.path.join("subdir", "2.txt"): "",
                        os.path.join("subdir", "2.pdb"): "",
                        os.path.join("subdir", "2.pdb1"): "",
                        os.path.join("subdir", "deepdir", "3.txt"): "",
                        os.path.join("subdir", "deepdir", "3.pdb"): "",
                        os.path.join("subdir", "deepdir", "3.pdb1"): ""})

    rm(None, "*.sh", temp_dir, recursive=True)

    rm(None, "*.pdb", temp_dir, recursive=True)

    assert os.path.isdir(os.path.join(temp_dir, "dir.pdb"))

    assert os.path.isfile(os.path.join(temp_dir, "1.txt"))
    assert not os.path.isfile(os.path.join(temp_dir, "1.pdb"))
    assert os.path.isfile(os.path.join(temp_dir, "1.pdb1"))

    assert os.path.isfile(os.path.join(temp_dir, "subdir", "2.txt"))
    assert not os.path.isfile(os.path.join(temp_dir, "subdir", "2.pdb"))
    assert os.path.isfile(os.path.join(temp_dir, "subdir", "2.pdb1"))

    assert os.path.isfile(os.path.join(temp_dir, "subdir", "deepdir", "3.txt"))
    assert not os.path.isfile(os.path.join(temp_dir, "subdir", "deepdir", "3.pdb"))
    assert os.path.isfile(os.path.join(temp_dir, "subdir", "deepdir", "3.pdb1"))

    rm(None, "*.pdb", temp_dir, recursive=True)


def test_remove_files_by_mask_non_recursively():
    temp_dir = temp_folder()
    with chdir(None, temp_dir):
        os.makedirs("subdir")

    save_files(temp_dir, {"1.txt": "",
                        "1.pdb": "",
                        "1.pdb1": "",
                        os.path.join("subdir", "2.txt"): "",
                        os.path.join("subdir", "2.pdb"): "",
                        os.path.join("subdir", "2.pdb1"): ""})

    rm(None, "*.pdb", temp_dir)
    assert not os.path.exists(os.path.join(temp_dir, "1.pdb"))
    assert os.path.exists(os.path.join(temp_dir, "subdir", "2.pdb"))

    assert os.path.exists(os.path.join(temp_dir, "1.txt"))
    assert os.path.exists(os.path.join(temp_dir, "subdir", "2.txt"))


@pytest.mark.parametrize("recursive", [False, True])
@pytest.mark.parametrize("results", [
    ["*.dll", ("foo.dll",)],
    [("*.dll",), ("foo.dll",)],
    [["*.dll"], ("foo.dll",)],
    [("*.dll", "*.lib"), ("foo.dll", "foo.dll.lib")],
])
def test_exclude_pattern_from_remove_list(recursive, results):
    """ conan.tools.files.rm should not remove files that match the pattern but are excluded
        by the excludes parameter.
        It should obey the recursive parameter, only excluding the files in the root folder in case
        it is False.
    """
    excludes, expected_files = results
    temporary_folder = temp_folder()
    with chdir(None, temporary_folder):
        os.makedirs("subdir")

    save_files(temporary_folder, {
        "1.txt": "",
        "1.pdb": "",
        "1.pdb1": "",
        "foo.dll": "",
        "foo.dll.lib": "",
        os.path.join("subdir", "2.txt"): "",
        os.path.join("subdir", "2.pdb"): "",
        os.path.join("subdir", "foo.dll"): "",
        os.path.join("subdir", "foo.dll.lib"): "",
        os.path.join("subdir", "2.pdb1"): ""})

    rm(None, "*", temporary_folder, excludes=excludes, recursive=recursive)

    for it in expected_files:
        assert os.path.exists(os.path.join(temporary_folder, it))
    assert not os.path.exists(os.path.join(temporary_folder, "1.pdb"))

    # Check the recursive parameter and subfolder
    condition = (lambda x: not x) if recursive else (lambda x: x)
    assert condition(os.path.exists(os.path.join(temporary_folder, "subdir", "2.pdb")))
    for it in expected_files:
        assert os.path.exists(os.path.join(temporary_folder, "subdir", it))
