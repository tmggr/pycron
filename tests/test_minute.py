from datetime import datetime
import mock


def test_parser():
    now = datetime(2015, 6, 18, 0, 9)
    assert mock.is_now(now, '* * * * *')
    assert mock.is_now(now, '9 * * * *')
    assert mock.is_now(now, '*/1 * * * *')
    assert mock.is_now(now, '*/3 * * * *')
    assert mock.is_now(now, '*/9 * * * *')
    assert mock.is_now(now, '3,9,25,16 * * * *')
    assert mock.is_now(now, '*/2 * * * *') is False
    assert mock.is_now(now, '*/4 * * * *') is False
    assert mock.is_now(now, '*/5 * * * *') is False
    assert mock.is_now(now, '*/12 * * * *') is False
    assert mock.is_now(now, '3,25,16 * * * *') is False