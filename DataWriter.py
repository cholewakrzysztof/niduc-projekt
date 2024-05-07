import csv
import string

from common.Report import Report


class DataWriter:

    @staticmethod
    def save_to_file(report: Report, file_name: string):
        with open(file_name, 'w', newline='') as file_csv:
            writer = csv.writer(file_csv)
            writer.writerow(['In bits', 'Out bits', 'Length', 'Redundancy bits count', 'Error type', 'Error appeared'])
            for test_result in report.test_results:
                writer.writerow(test_result.as_list())

        print("Date been written into csv file" + file_name)