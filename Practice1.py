# Variables , Data Types , Operators

# Swap two numbers 
# num1 = 5
# num2 = 10 
# num3 = num1
# num1 = num2
# num2 = num3

# print("Num1 value is : ", num1)
# print("Num2 value is : ", num2)

# Sum of three numbers 
# num1 = int(input("Please enter a num1 : "))
# num2 = int(input("Please enter a num2 : "))
# num3 = int(input("Please enter a num3 : "))

# sum = num1 + num2 +num3
# print("Total sum of three numbers is : ", sum)


#  Check even or odd
# num1 = int(input("Please enter a num1 : "))
# if num1 %2 == 0:
#     print("Num1 is an even number", num1)
# else:
#     print("Num1 is an odd number", num1)


# Find the largest number of three numbers

# num1 = int(input("Please enter a num1 : "))
# num2 = int(input("Please enter a num2 : "))
# num3 = int(input("Please enter a num3 : "))

# num = [num1, num2, num3]

# if num1 > num2 and num1 > num3:
#     print(num1, "is the greates num")
# elif num2 > num3:
#     print(num2, "is the gretest")
# else:
#     print(num3, "is the greatest")   



# Strings

# Reverse a string

# name = input("Please enter any programming lnaguage: ")
# reversed_name = ""
# for char in name:
#     reversed_name =  char + reversed_name
# print(reversed_name)


#  Check if a string is palindrome

# name = input("Please enter any name : ")

# reversed_name = ""
# for char in name:
#     reversed_name = char + reversed_name
# if name == reversed_name:
#   print("Its a plaindrome")
# else:
#   print("Its not a palindrome")

# Count Vowels in a String

# name = input("Please enter any name : ")
# vowel = ["a", "e", "i", "o" ,"u"]
# count = 0
# for char in name :
#     if char in vowel:
#         count += 1
# print(count)


# Remove all spaces from a string

# love = input("How do you express your love to me : ")
# love_with_no_space = love.replace(" ", "")
# print(love_with_no_space)
 

# Lists and Loops 
#  Find sum all elements in a list
# list = [1, 2, 3, 4, ]
# sum = sum(list)

# print(sum)

# Find max and min in a list

# list = [3,7,1, 9]
# max = max(list)
# min = min(list)
# print(max)
# print(min)


#  Print even numbers from a list

# list = [1, 2, 3, 4, 5, 6]

# for val in list:
#  if val %2 == 0:
#     print("Its a even num")
#  else:
#     print("Its a odd num")
    
# numbers = [1, 2, 3, 4, 5, 6]

# [print(f"{num} is even") if num % 2 == 0 else print(f"{num} is odd") for num in numbers]


# Find second largest element in a list

# list = [10,20,80,90]
# max = max(list)
# min = min(list)
# for val in list:
#     if val < max and val > min:
#      print(val, "Thats a second largest num")


# Dictionaries and Sets 
# Count frequency of each element in a list
# num = [1, 2, 2, 3, 3,] 

# count = {}      # null dictionary
# for i in num:
#     if i in count:
#         count[i] +=1
#     else:
#         count[i] = 1
# print(count)


#  Merge two dictionary

# num1 = {1:"a"}
# num2 = {2: "b"}
# num1.update(num2)
# print(num1)

# Find keys with max val in dictionary 

# dic = {"a" : 5, "b": 10, "c" : 10}

# max_val = max(dic.values())


# max_keys = [key for key, value in dic.items() if value ==max_val]
# print(max_keys)


#  Check if two lists have common elements

# num1 = [1,2,3]
# num2 = [9,4,5]

# has_common = bool(set(num1) & set(num2))
# print(has_common)
    
#  remove duplicate from a list using set

list = [1,1,2,2,3]


print(set(list))