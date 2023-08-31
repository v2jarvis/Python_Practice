def update_value(a, user):
    c= a[:-len(user)]
    a = a[0] + user
    return a

a = "C00000"
user = input("Enter a number: ")
updated = update_value(a, user)
print("Updated value:", updated)






















'''given_string = "C000000"

userInput = int(input(":"))

len_of_given_string = len(given_string)

total_number_of_zero = len_of_given_string - len(str(userInput))

remove_all_zero_after_c = given_string[:-total_number_of_zero]
add_zero_with_user_input = f"{userInput:0{total_number_of_zero}d}"
result_i_want = remove_all_zero_after_c + add_zero_with_user_input
print("result:",result_i_want)'''

'''a="C00000"
user1= input("enter number")
c= a[:-len(user1)]
c+=user1
print(c)'''



