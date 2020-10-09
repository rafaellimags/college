# reverse() changes the value of the variable in memory address

def change_values(list_values):
    list_values.reverse()
    print(list_values)


values = []
size = int(input('Size: '))

for x in range(size):
    values.append(int(input('Numbers: ')))

change_values(values)