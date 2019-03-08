from unittest import TestCase

from ExactMatching.NaiveApproach.Match import Match


class TestMatch(TestCase):
    def test_match(self):
        m = Match()
        t = "AAAAAAAAAAAAAAAAAAAAAAAAAATAAAAAAAAAAAAAAAATAAAAAG"
        p = "AAAAAT"
        positions = m.match(t, p)
        print("positions", positions)
        self.assertIn(21, positions)
        self.assertIn(38, positions)
