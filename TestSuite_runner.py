import os
import unittest

import xmlrunner

from tests import Buzz, PIM, Recruitment


if __name__ == '__main__':

    def suites():
        # add tests to the test suite
        suite_pim = unittest.TestLoader().loadTestsFromTestCase(PIM.PIMTestCases)
        suite_recruitment = unittest.TestLoader().loadTestsFromTestCase(Recruitment.RecruitmentTestCases)
        suite_buzz = unittest.TestLoader().loadTestsFromTestCase(Buzz.BuzzTestCases)
        all_tests = unittest.TestSuite([suite_pim, suite_recruitment, suite_buzz])
        return all_tests


    # create a directory for storing results
    os.makedirs(os.path.join(os.getcwd(), "test_results"), exist_ok=True)

    # initialize a runner XMLRunner to get output as xml, pass it to your suite and run it
    # output the test results to an xml file
    runner = xmlrunner.XMLTestRunner(output="test_results", verbosity=3)
    runner.run(suites())






