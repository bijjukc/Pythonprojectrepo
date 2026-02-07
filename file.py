# f = open("demo.text", "r")
# # data = f.read(5) # we are giving 5 it means it will read 5 data
# # print(data)
# line1 = f.readline()
# print(line1)
# # print(type(data))
# f.close()



# Writing to a file

# f = open("demo.text" , "a+")
# data = f.write("I am lerning python currently")
# print(data)



 # Create a new file 

with open("practice.txt", "r") as f:
    data = f.read()
    
new_data = data.replace("Java", "Python")    
print(new_data)

with open("practice.txt", "w") as f:
   f.write(new_data)
