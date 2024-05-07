from common.TestResult import TestResult


class Report:
    test_results: list[TestResult]

    def __init__(self, test_results: list[TestResult]):
        self.test_results = test_results




