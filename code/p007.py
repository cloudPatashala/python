# Today we will be looking at Variables in python.


a = 10
b = 12

print(a)
print(b)

c = a + b
print(c)


first_name = input("What is your first name: ")
last_name = input("What is your Last Name: ")

len_first_mame = len(first_name)
len_last_name = len(last_name)

total_len = len_first_mame + len_last_name

print(type(total_len))
print("The name " + first_name + " " + last_name +
      " has " + str(total_len) + " characters in it")
