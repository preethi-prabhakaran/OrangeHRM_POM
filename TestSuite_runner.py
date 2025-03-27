import unittest
from tests import Buzz, PIM, Recruitment


if __name__ == '__main__':

    def suites():
        # add tests to the test suite
        suite_pim = unittest.TestLoader().loadTestsFromTestCase(PIM.PIMTestCases)
        suite_recruitment = unittest.TestLoader().loadTestsFromTestCase(Recruitment.RecruitmentTestCases)
        suite_buzz = unittest.TestLoader().loadTestsFromTestCase(Buzz.BuzzTestCases)
        all_tests = unittest.TestSuite([suite_pim, suite_recruitment, suite_buzz])
        return all_tests

    # initialize a runner, pass it to your suite and run it
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suites())





