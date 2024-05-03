import csv
import time

def read_from_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            return int(file.read())
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None
    except Exception as e:
        print(f"Error reading from {file_path}: {e}")
        return None

def write_to_csv(data, file_path):
    try:
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error writing to {file_path}: {e}")

def monitor_ksm_files(file_paths, csv_file_path, interval=5):
    while True:
        data = [read_from_csv(file) for file in file_paths]
        write_to_csv(data, csv_file_path)
        time.sleep(interval)

if __name__ == "__main__":
    ksm_file_paths = [
        "/sys/kernel/mm/ksm/pages_shared",
        "/sys/kernel/mm/ksm/pages_sharing",
        "/sys/kernel/mm/ksm/full_scans",
        "/sys/kernel/mm/ksm/max_page_sharing",
        "/sys/kernel/mm/ksm/pages_unshared",
        "/sys/kernel/mm/ksm/pages_to_scan"
    ]
    csv_file_path = "ksm_data.csv"
    header = ["pages_shared", "pages_sharing", "full_scans", "max_page_sharing", "pages_unshared", "pages_to_scan"]
    
    # Writing header to the CSV file
    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

    monitor_ksm_files(ksm_file_paths, csv_file_path)
