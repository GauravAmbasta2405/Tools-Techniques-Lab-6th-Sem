test_list1 = []
count = int(input('How many numbers?: '))
for n in range(count):
    number = int(input('Enter number: '))
    test_list1.append(number)
test_list2 = []
count = int(input('How many numbers?: '))
for n in range(count):
    number = int(input('Enter number: '))
    test_list2.append(number)

for i in test_list2:
    test_list1.append(i)
print("Concatenated list: " + str(test_list1))