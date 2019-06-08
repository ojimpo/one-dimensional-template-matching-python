data = [1, 1, 4, 5, 1, 4, 8, 1, 0, 1, 9, 1, 9]
template = [8, 1, 0]

# print(template)

for i in range(0, len(data), len(template)):
    scan = data[i:i+len(template)]
    for j in range(len(scan)):
        diff = scan[j] - template[j]
        print(diff)