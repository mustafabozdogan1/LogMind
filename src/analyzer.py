def analyze_logs(lines):
    error_count = 0
    warning_count = 0
    info_count = 0

    for line in lines:
        if "ERROR" in line:
            error_count += 1
        elif "WARNING" in line:
            warning_count += 1
        elif "INFO" in line:
            info_count += 1

    return error_count, warning_count, info_count


def find_top_errors(lines):
    error_messages = {}

    for line in lines:
        if "ERROR" in line:
            parts = line.split("ERROR", 1)
            message = parts[1].strip() if len(parts) > 1 else "UNKNOWN"

            if message in error_messages:
                error_messages[message] += 1
            else:
                error_messages[message] = 1

    if not error_messages:
        return []

    sorted_errors = sorted(
        error_messages.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return sorted_errors[:3]