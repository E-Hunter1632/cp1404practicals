"""
Wimbledon game matches
Estimated Completion Time: 30-40 minutes
Actual Completion Time:
"""


def main():
    data = get_data()
    champion_to_count, countries = process_data(data)
    display_data(champion_to_count, countries)


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


def process_data(data):
    """Process the data to prepare to be displayed nicely"""
    champion_to_count = {}
    countries = set()
    for entry in data:
        countries.add(entry[1])
        try:
            champion_to_count[entry[2]] += 1
        except KeyError:
            champion_to_count[entry[2]] = 1
    return champion_to_count, countries


def display_data(champion_to_count, countries):
    print("Wimbledon Champions:")
    for champion, count in champion_to_count.items():
        print(f"{champion}: {count}")
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(', '.join(country for country in sorted(countries)))


main()
