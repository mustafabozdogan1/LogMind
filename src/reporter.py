import json
import os
import matplotlib.pyplot as plt


def print_report(error_count, warning_count, info_count, top_errors):
    print("------------------")
    print(f"ERROR: {error_count}")
    print(f"WARNING: {warning_count}")
    print(f"INFO: {info_count}")
    print()

    print("Top Errors")

    if not top_errors:
        print("No errors found.")
        return

    for i, (message, count) in enumerate(top_errors, start=1):
        print(f"{i}. {message} ({count})")


def save_json_report(error_count, warning_count, info_count, top_errors):
    os.makedirs("reports", exist_ok=True)

    data = {
        "errors": error_count,
        "warnings": warning_count,
        "info": info_count,
        "top_errors": []
    }

    for message, count in top_errors:
        data["top_errors"].append({
            "message": message,
            "count": count
        })

    with open("reports/analysis_report.json", "w") as file:
        json.dump(data, file, indent=4)


def save_chart(error_count, warning_count, info_count):
    labels = ["ERROR", "WARNING", "INFO"]
    values = [error_count, warning_count, info_count]

    os.makedirs("charts", exist_ok=True)

    plt.figure(figsize=(6, 4))
    plt.bar(labels, values)
    plt.title("Error Distribution")
    plt.ylabel("Count")

    plt.tight_layout()
    plt.savefig("charts/error_distribution.png")
    plt.close()


def save_top_errors_chart(top_errors):
    if not top_errors:
        return

    labels = [message for message, count in top_errors]
    values = [count for message, count in top_errors]

    os.makedirs("charts", exist_ok=True)

    plt.figure(figsize=(8, 4))
    plt.bar(labels, values)

    plt.title("Top Errors")
    plt.ylabel("Count")
    plt.xticks(rotation=20)

    plt.tight_layout()
    plt.savefig("charts/top_errors.png")
    plt.close()


def save_timeline_chart(lines):
    times = []
    values = []

    count = 0

    for i, line in enumerate(lines):
        if "ERROR" in line or "WARNING" in line or "INFO" in line:
            count += 1
            times.append(i)
            values.append(count)

    if not times:
        return

    os.makedirs("charts", exist_ok=True)

    plt.figure(figsize=(8, 4))
    plt.plot(times, values)

    plt.title("Log Timeline")
    plt.xlabel("Log Line")
    plt.ylabel("Events")

    plt.tight_layout()
    plt.savefig("charts/log_timeline.png")
    plt.close()