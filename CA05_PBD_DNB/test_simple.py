
import unittest

from simple import get_commits, read_file

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.data = read_file('changes_python.log')

    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))

    def test_number_of_commits(self):
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))

    def test_first_commit(self):
        commits = get_commits(self.data)
        self.assertEqual('Thomas', commits[0]['author'])
        self.assertEqual('r1551925', commits[0]['revision'])
 # Added two more tests to the fist_commit function       
        self.assertEqual('2015-11-27 16:57:44 +0000 (Fri, 27 Nov 2015)', commits[0]['date'])
        self.assertEqual('line', commits[0]['number_of_lines'])

if __name__ == '__main__':
    unittest.main()
