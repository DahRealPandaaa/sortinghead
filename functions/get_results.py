import csv


def get_results() -> list:
    results = []
    with open("results.csv", "r") as file:
        csv_file = csv.DictReader(file)

        for line in csv_file:
            results.append(line)

    return results
