from deeprs.utils import check_version


def test_check_version():
    check_version('0.1.0')
    check_version(124214)
