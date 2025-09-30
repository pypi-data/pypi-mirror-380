
from conan.api.output import ConanOutput
from conan.internal.model.manifest import FileTreeManifest
from conan.test.utils.mocks import RedirectedTestOutput
from conan.test.utils.tools import redirect_output


class TestReportCopiedFiles:

    def test_output_string(self):
        manifest = FileTreeManifest(0,
                                    file_sums={'/abs/path/to/file.pdf': "",
                                               '../rel/path/to/file2.pdf': "",
                                               '../rel/path/to/file3.pdf': "",
                                               '../rel/path/to/file4.pdf': "",
                                               '../rel/path/to/file5.pdf': "",
                                               '../rel/path/to/file6.pdf': "",
                                               '../rel/path/to/file7.pdf': "",
                                               '/without/ext/no_ext1': "",
                                               'no_ext2': "",
                                               'a/other.txt': ""})
        output = RedirectedTestOutput()
        with redirect_output(output):
            manifest.report_summary(ConanOutput())
            lines = sorted(str(output).splitlines())
            assert "Copied 7 '.pdf' files" == lines[2]
            assert "Copied 2 files: no_ext1, no_ext2" == lines[1]
            assert "Copied 1 '.txt' file: other.txt" == lines[0]
