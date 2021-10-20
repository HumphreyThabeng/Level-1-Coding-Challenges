List1 = [11, 22, 33]
List2 = [1, 2, 3]

List3 = []

for x in range(len(List1)):
    List3.append(List1[x])
    List3.append(List2[x])

print(List3)