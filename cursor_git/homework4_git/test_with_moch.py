import unittest
import requests_mock

from employee import Employee

"""pytest mock"""


def test_last(requests_mock):
    requests_mock.get('http://company.com/Savchuk/june', text='data', status_code=200)
    classsss = Employee('Mykhailo', 'Savchuk', 200)
    assert classsss.monthly_schedule('june') == 'data'


class TestEmployee(unittest.TestCase):
    def setUp(self) -> None:
        self.filled_employee = Employee('Mykhailo', 'Savchuk', 200)

    def test_email(self):
        self.filled_employee.email
        self.assertTrue(self.filled_employee.email == 'Mykhailo.Savchuk@email.com')

    def test_fullname(self):
        self.filled_employee.fullname
        self.assertTrue(self.filled_employee.fullname == 'Mykhailo Savchuk')

    def test_applyriese(self):
        self.filled_employee.apply_raise()
        self.assertTrue(self.filled_employee.pay == 210)

    """unittest mock"""

    @requests_mock.mock()
    def test_mothly_shedule(self, requestsmock):
        requestsmock.get('http://company.com/Savchuk/june', text='data', status_code=404)
        self.assertTrue(self.filled_employee.monthly_schedule('june') == 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
