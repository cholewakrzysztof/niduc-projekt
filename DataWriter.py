import csv
import datetime
import string
from common.Report import Report


class DataWriter:

    @staticmethod
    def save_to_file(report: Report, name: string, path: string):
        current_time = datetime.datetime.now()
        timestamp_str = current_time.strftime("%Y-%m-%d_%H%M%S")
        file_name = f'{path}\\{name}_{timestamp_str}.csv'
        file_csv = open(file_name, 'w', newline='')
        writer = csv.writer(file_csv, delimiter=';')
        writer.writerow(['Coder',
                         'Channel',
                         'Packet Size',
                         'In',
                         'Out',
                         'Differences',
                         'Redundancy bit count',
                         'Bit error rate'])

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

            writer.writerow([coder,
                             channel,
                             packet_size,
                             in_packet,
                             out_packet,
                             differences,
                             redundancy,
                             ''])

        writer.writerow([coder, channel, packet_size, '', '', '', redundancy_sum, error_bit_rate])

        print("Date been written into csv file" + file_name)
