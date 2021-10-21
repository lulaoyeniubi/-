import pytest
from common.utils import case_path, report_path, get_time

t = get_time()
pytest.main(['-v', f'--html={report_path}/{t}.html', case_path])

