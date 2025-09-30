import tempfile
from collections import namedtuple

import pytest

from conan.internal.rest.file_uploader import FileUploader
from conan.internal.errors import InternalErrorException, AuthenticationException, ForbiddenException
from conan.internal.util.files import save


class _ConfigMock:
    def get(self, name, default=None, check_type=None):
        return default


class MockRequester:
    retry = 0
    retry_wait = 0

    def __init__(self, response):
        self._response = response

    def put(self, *args, **kwargs):
        return namedtuple("response", "status_code content")(self._response, "tururu")


class TestUploaderUnit:
    @pytest.fixture(autouse=True)
    def setup(self):
        _, self.f = tempfile.mkstemp()
        save(self.f, "some contents")

    def test_401_raises_unauthoirzed_exception(self):
        uploader = FileUploader(MockRequester(401), verify=False, config=_ConfigMock())
        with pytest.raises(AuthenticationException, match="tururu"):
            uploader.upload("fake_url", self.f)

    def test_403_raises_unauthoirzed_exception_if_no_token(self):
        auth = namedtuple("auth", "bearer")(None)
        uploader = FileUploader(MockRequester(403), verify=False, config=_ConfigMock())
        with pytest.raises(AuthenticationException, match="tururu"):
            uploader.upload("fake_url", self.f, auth=auth)

    def test_403_raises_unauthorized_exception_if_no_auth(self):
        uploader = FileUploader(MockRequester(403), verify=False, config=_ConfigMock())
        with pytest.raises(AuthenticationException, match="tururu"):
            uploader.upload("fake_url", self.f)

    def test_403_raises_forbidden_exception_if_token(self):
        auth = namedtuple("auth", "bearer")("SOMETOKEN")
        uploader = FileUploader(MockRequester(403), verify=False, config=_ConfigMock())
        with pytest.raises(ForbiddenException, match="tururu"):
            uploader.upload("fake_url", self.f, auth=auth)

    def test_500_raises_internal_error(self):
        uploader = FileUploader(MockRequester(500), verify=False, config=_ConfigMock())
        _, f = tempfile.mkstemp()
        save(f, "some contents")
        with pytest.raises(InternalErrorException, match="tururu"):
            uploader.upload("fake_url", self.f, dedup=True)
