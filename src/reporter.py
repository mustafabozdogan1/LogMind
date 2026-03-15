def print_report(error_count, warning_count, info_count, common_error):
    print("LogMind Analysis")
    print("----------------")
    print("ERROR:", error_count)
    print("WARNING:", warning_count)
    print("INFO:", info_count)

    if common_error:
        print("Most common error:", common_error)


def save_report(error_count, warning_count, info_count, common_error):
    with open("analysis_report.txt", "w") as file:
        file.write("LogMind Analysis\n")
        file.write("----------------\n")
        file.write(f"ERROR: {error_count}\n")
        file.write(f"WARNING: {warning_count}\n")
        file.write(f"INFO: {info_count}\n")

        if common_error:
            file.write(f"Most common error: {common_error}\n")