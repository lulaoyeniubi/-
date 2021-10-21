import pytest
from common.utils import *

date = read_csv(data_path + '/test_logins.csv')


@pytest.mark.skipif(date[5][1] != "Y", reason="此版本不测试")
@pytest.mark.parametrize("case", date[7:])
def test_login(case):
    url = date[1][1]
    method = date[2][1]
    d = get_test_data(case[1])
    r = request(url=url, method=method, data=d)
    # print(r.json())
    assert int(case[2]) == r.json()["code"]
    assert case[3] == r.json()["message"]


if __name__ == '__main__':
    pytest.main(['-s', __file__])
