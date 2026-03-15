from parser import read_log
from analyzer import analyze_lines, most_common_error
from reporter import print_report, save_report
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python src/logmind.py <logfile> [LOGLEVEL]")
        return

    log_file = sys.argv[1]

    log_level = None
    if len(sys.argv) > 2:
        log_level = sys.argv[2]

    try:
        lines = read_log(log_file)
    except FileNotFoundError:
        print("Error: Log file not found.")
        return

    if log_level:
        lines = [line for line in lines if log_level in line]

    error_count, warning_count, info_count = analyze_lines(lines)
    common_error = most_common_error(lines)

    print_report(error_count, warning_count, info_count, common_error)
    save_report(error_count, warning_count, info_count, common_error)


if __name__ == "__main__":
    main()