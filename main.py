import re
from typing import List, Tuple
import csv


def load_column_into_list(file_path: str, column_number: int = 0) -> List[str]:
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        data = []
        for row in csv_reader:
            # skip processing header
            if line_count == 0:
                line_count += 1
            else:
                data.append(row[column_number])
                line_count += 1
        print(f'Processed {line_count} lines.')

        return data

target = '[Cc]asual'
n = 3


def search(text: str, target: str, n: int) -> object:
    #Searches for text,and retrieves n words either side of the text,which are returned seperately
    word = r"\W*([\w]+)"
    groups = re.search(r'{}\W*{}{}'.format(word * n, target, word * n), text).groups()
    return groups[:n], groups[n:]

    #run_search = data.apply(lambda row: search(row['text'],target,n),
    #        axis=1)
    # run_search = [(lambda row: search(row['text'],target,n))(row) for row in data]

    # print(run_search)

data = load_column_into_list("data.csv")

with open("output.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["text", "result"])

    for text in data:
        result = search(text,target,n)
        csv_writer.writerow([text, result[0], result[1]])
        print(f"text: {text}, result: {result}")

    csv_file.close()