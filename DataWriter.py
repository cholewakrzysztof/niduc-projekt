import csv
import datetime
import string
from common.Report import Report


class DataWriter:

    @staticmethod
    def save_to_file(report: Report, name: string):
        current_time = datetime.datetime.now()
        timestamp_str = current_time.strftime("%Y-%m-%d_%H%M%S")
        file_name = f'C:\\Users\\Admin\\Desktop\\NIDUC\\{name}_results_{timestamp_str}.csv'
        file_csv = open(file_name, 'w', newline='')
        writer = csv.writer(file_csv, delimiter=';')
        writer.writerow(['Coder', 'Channel', 'Packet Size', 'In', 'Out', 'Differences', 'Bit error rate'])

        coder = report.coder
        channel = report.channel
        sum_differences = 0
        packet_size = report.packet_size
        error_bit_rate = report.error_bit_rate
        print("Warning: hardcoded error_bit_rate")

        for result in report.test_results:
            in_packet = result.in_bits
            out_packet = result.out_bits
            differences = result.differences_count

            sum_differences += differences
            writer.writerow([coder,
                             channel,
                             packet_size,
                             in_packet,
                             out_packet,
                             differences,
                             ''])

        writer.writerow([coder, channel, packet_size, '', '', '', error_bit_rate])
        print(f"{coder};{channel};{packet_size};;;{error_bit_rate}")

        print("Date been written into csv file" + file_name)
