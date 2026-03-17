import sys
from parser import parse_log
from analyzer import analyze_logs, find_top_errors
from reporter import (
    print_report,
    save_json_report,
    save_chart,
    save_top_errors_chart,
    save_timeline_chart
)


def main():
    if len(sys.argv) < 2:
        print("Usage: python src/logmind.py <logfile>")
        return

    log_file = sys.argv[1]

    lines = parse_log(log_file)

    error_count, warning_count, info_count = analyze_logs(lines)
    top_errors = find_top_errors(lines)

    print_report(error_count, warning_count, info_count, top_errors)

    save_json_report(error_count, warning_count, info_count, top_errors)

    save_chart(error_count, warning_count, info_count)

    save_top_errors_chart(top_errors)

    save_timeline_chart(lines)


if __name__ == "__main__":
    main()