# Python Program to Swap Two Elements in a List
input_str = input("Enter the elements separated by commas: ")
my_list = [int(item) for item in input_str.split(',')]

print("Original list:", my_list)

index1 = int(input("Enter the index of the first element to swap (0-based): "))
index2 = int(input("Enter the index of the second element to swap (0-based): "))

if 0 <= index1 < len(my_list) and 0 <= index2 < len(my_list):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp
    print("List after swapping:", my_list)
else:
    print("Invalid indices. Elements not swapped.")
