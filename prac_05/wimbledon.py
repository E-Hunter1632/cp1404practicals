"""
Wimbledon game matches
Estimated Completion Time: 30-40 minutes
Actual Completion Time:
"""


def main():
    data = get_data()
    print(data)


def get_data():
    """Read the file and prepare contents for processing"""
    data = []
    in_file = open("wimbledon.csv", 'r', encoding="utf-8-sig")
    in_file.readline()  # reads and skips the first line.
    for line in in_file:
        parts = line.strip().split(',')  # removes the \n and puts into parts
        data.append(parts)  # adds parts to list for later processing
    in_file.close()
    return data


main()
