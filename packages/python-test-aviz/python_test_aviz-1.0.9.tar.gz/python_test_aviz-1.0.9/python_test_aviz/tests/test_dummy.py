import pytest


class TestDummy:
    @staticmethod
    @pytest.mark.dummy
    def test_dummy() -> None:
        assert True

    @staticmethod
    @pytest.mark.dummy
    @pytest.mark.dummy2
    def test_true() -> None:
        assert True


@pytest.mark.dummy
def test_true() -> None:
    assert True
