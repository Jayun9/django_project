import csv
with open("./resource/sample1.csv" , 'r', encoding='EUC-KR') as f:
    reader = csv.reader(f)
    # header 스킵 가능
    next(reader)
    print(dir(reader))
    print()
    # __iter__ 가 있으니 반복 가능
    for c in reader:
        print(c)
print("----------------------------------------------------------")
print("----------------------------------------------------------")

with open("./resource/sample2.csv" , 'r', encoding='EUC-KR') as f:
    reader = csv.reader(f, delimiter='|')
    # header 스킵 가능
    next(reader)
    # __iter__ 가 있으니 반복 가능
    for c in reader:
        print(c)

print("----------------------------------------------------------")
print("----------------------------------------------------------")

with open("./resource/sample1.csv" , 'r', encoding='EUC-KR') as f:
    reader = csv.DictReader(f)
    # header 스킵 가능
    # __iter__ 가 있으니 반복 가능
    for c in reader:
        print(c)

print("----------------------------------------------------------")
print("----------------------------------------------------------")
write_list = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
with open("./resource/sample3.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    for line in write_list:
        writer.writerow(line)

print("----------------------------------------------------------")
print("----------------------------------------------------------")
with open("./resource/sample4.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(write_list)