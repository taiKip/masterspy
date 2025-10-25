# File Processing - Score
# tarvk002


def convert_items_to_int(position_from_end, data_list):
    abs_pos = abs(position_from_end)
    if len(data_list) < abs_pos:
        raise ValueError(f"List must contain atleast {abs_pos} items")
    items_to_convert = data_list[position_from_end:]
    converted_items = [int(item) for item in items_to_convert]
    data_list[position_from_end:] = converted_items
    return data_list


def load_records(filename):
    records = []
    try:
        infile = open(filename)
    except Exception as e:
        print(f"Something went wrong:{e}")
    for line in infile:
        items = line.split(',')
        converted_items = convert_items_to_int(-3,items)
        records.append(converted_items)
    infile.close()
    return records

def print_records(records):
    if len(records) == 0:
        print("No records available")
        return
    print(f"{'Full Name':<20}{'A':<5}{'B':<5}{'C':<5}{'Avg'}")
    print("="*40)
    for record in records:
        fullName = record[1] + ' ' + record[0]
        average = round((record[2] + record[3] +record[4])/3,1)
        print(f"{fullName:<20}{record[2]:<5}{record[3]:<5}{record[4]:<5}{average}")


def save_average_scores(fileName,records):
    try:
        outFile = open(fileName,'w')
        for record in records:
            avg = round((record[2] + record[3] + record[4])/3,1)
            outFile.write(f"{record[0]},{record[1]},{avg}\n")
    except Exception as e:
        print(f"Something went wrong: {e}")
    outFile.close()


def main():
    records = load_records('score_input.txt')
    print_records(records)
    save_average_scores('score_ouput.txt',records)

main()


f = open('hello.txt')

for l in f:
    w = l.split()
    print(w)

f.write("welcome!\n")
f.close()