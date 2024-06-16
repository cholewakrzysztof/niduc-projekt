import csv
import datetime
import string
from common.Report import Report


class DataWriter:
    writer = None
    file_name = None
    file_csv = None

    @staticmethod
    def open(name: string, path: string):
        current_time = datetime.datetime.now()
        timestamp_str = current_time.strftime("%Y-%m-%d_%H%M%S")
        DataWriter.file_name = f'{path}\\{name}_{timestamp_str}.csv'
        DataWriter.file_csv = open(DataWriter.file_name, 'w', newline='')
        DataWriter.writer = csv.writer(DataWriter.file_csv, delimiter=';')
        DataWriter.writer.writerow(['Coder',
                         'Iteration',
                         'Channel',
                         'Packet Size',
                         'In',
                         'Out',
                         'Differences',
                         'Redundancy bit count',
                         'Bit error rate'])

    @staticmethod
    def close():
        DataWriter.file_csv.close()
        print("Results been successfully written into csv file" + DataWriter.file_name)


    @staticmethod
    def writeReport(iteration: int, report: Report):
        coder = report.coder
        channel = report.channel
        packet_size = report.packet_size
        error_bit_rate = report.error_bit_rate
        redundancy_sum = report.redundancy

        for result in report.test_results:
            in_packet = result.in_bits
            out_packet = result.out_bits
            differences = result.differences_count
            redundancy = result.redundancy_bits_count

            DataWriter.writer.writerow([coder,
                             iteration,
                             channel,
                             packet_size,
                             in_packet,
                             out_packet,
                             differences,
                             redundancy,
                             '0'])

        DataWriter.writer.writerow([coder, iteration, channel, packet_size, '0', '0', '0', redundancy_sum, '\t'+str(error_bit_rate)])

    @staticmethod
    def writeSummary(report: Report, avg_redundancy_sum: int, avg_error_bit_rate: float):
        DataWriter.writer.writerow([report.coder, -1, report.channel, report.packet_size, '0', '0', '0', avg_redundancy_sum, '\t'+str(avg_error_bit_rate)])



