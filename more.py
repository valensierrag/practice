#Iterate the given list of numbers and print only those numbers which are divisible by 5
list = [10, 20, 33, 46, 55]
divisible5 = []
for i in list:
    if i % 5 == 0 :
        divisible5.append(i)
    i += 1

print(divisible5)

# find how many times substring “Emma” appears in the given string.
str_x = "Emma is good developer. Emma is a writer"
print(str_x.count("Emma"))

#Print the following patter
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
for i in range (6):
    num = str(i)
    print(i*num +"\n")

for num in range(10):
    for i in range(num):
        print (num, end=" ") #print number
    # new line after each row to display pattern correctly
    print("\n")

#create a new list such that it should contain odd numbers from the first list and even numbers from the second list.
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
new_list = []
for i in list1:
    if i % 2 != 0:
        new_list.append(i)
for i in list2:
    if i % 2 == 0:
        new_list.append(i)

print(new_list)

#Write a Program to extract each digit from an integer in the reverse order
number = int(input("Give me a number "))
while number > 0:
    # get the last digit
    digit = number % 10
    # remove the last digit and repeat the loop
    number = number // 10
    print(digit, end=" ")
