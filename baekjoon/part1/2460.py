train_data_sheet = []

for _ in range(10):
    train_data_sheet.append(list(map(int, input().split())))

num_people = 0
max_num = 0

for data in train_data_sheet:
    out_count = data[0]
    in_count = data[1]

    num_people -= out_count
    max_num = max(max_num, num_people)

    num_people += in_count
    max_num = max(max_num, num_people)

print(max_num)
