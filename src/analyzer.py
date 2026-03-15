def analyze_lines(lines):
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
def most_common_error(lines):
    error_messages = {}

    for line in lines:
        if "ERROR" in line:
            message = line.split("ERROR")[1].strip()

            if message in error_messages:
                error_messages[message] += 1
            else:
                error_messages[message] = 1

    if not error_messages:
        return None

    return max(error_messages.items(), key=lambda x: x[1])[0]