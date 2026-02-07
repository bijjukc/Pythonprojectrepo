# num = 1
# while num <=100:
#     print( "num : ", num)
#     num += 1
    
    # print the numers from 100 to 1
# i = 100
# while i >=1:
#      print("num : ", i)
#      i -=1



#  print the multiplication table of a number n
# num = int(input("Please enter a number: "))
# i = 1
# while i <=10 :
#     print (num * i )
#     i +=1
    
    
    #   print the elements of the following the list using a loop
# num = [1, 4, 9 ,16, 25, 36, 49, 64, 81, 100]
# idx = 0
# while idx < len(num):
#     print(num[idx])
#     idx += 1
    
    
# Search for a numbers x in ti=his tuple using loop
# nums = (1, 4, 9,26,25,36,49,64,81,100)
# x = 1
# idx = 0
# while idx < len(nums):
#     if(nums[idx] == x):
#         print("found at idx" , idx)
#     else:
#         print("finding....")
#     idx +=1


# using for 
#  Print the elements of the following list uisng a loop

# nums = [1, 2, 5,6,6,9, 8, 10, 45, 86]
# for num in nums:
#     print("vaulue of num : " , num) 


# Search for a number x in this tuple using loop

# nums = (1, 4, 9, 16, 25, 36, 49, 81, 100)
# x = 100

# for num in nums:
#     if(num == x):
#         print(x)


#  Using for & range()

# print numbers from 1 to 100

# for val in range(100):
#     print(val)
    
    
# print numbers from 100 to 1
# for val in range (100, 1 , -1):
#     print(val)
    
#  print the multiplication table of a number n

# n = int(input("Please enter a number : "))
# for i in range( 1,11):
#     print(n*i)
 

#  WAP to find the sum of first n numbers
# n = 5
# i = 1
# sum = 0
# while i <=n:
#     sum += i
#     i+=1
# print(sum)
  

# for i in range(1, n+1):
#     sum += i
#   print(sum)



# WAP to find the factorial of first n numbers (using for)

n = int(input("Please enter a num : "))
fact = 1
for i in range(1, n+1):
    fact *= i
   
print(fact)

