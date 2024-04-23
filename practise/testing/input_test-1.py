import unittest
from test_01 import formated_name

name = 'alok'
last_name = 'kavilkar'

forms = formated_name(name, last_name)
# print(f'formated name is {forms}')

test_case_first_name = ['Robin', 'mahesh', 'harsh', 'ram', 'krish']

test_case_last_name = ['sharma', 'manu', 'patel', 'hari', 'uttam']


class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):

        for first, last in zip(test_case_first_name, test_case_last_name):

            result = formated_name(first, last)
            print(result)

            self.assertEqual(result, first.title() + ' ' + last.title())

    def test_robin_sharma(self):
        result = formated_name('Robin', 'Sharma')
        self.assertEqual(result, 'Robin Sharma')

    def test_mahesh_manu(self):
        result = formated_name('mahesh', 'manu')
        self.assertEqual(result, 'Mahesh Manu')

if __name__ == '__main__':
    unittest.main()
