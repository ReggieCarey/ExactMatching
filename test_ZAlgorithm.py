from unittest import TestCase

from ExactMatching.Z_Algorithm.Z_Algorithm import ZAlgorithm


class TestZAlgorithm(TestCase):
    def test_z(self):
        print()

        alg = ZAlgorithm("ATTCACTATTCGGCTAT")
        print(alg.z())
        self.fail()
