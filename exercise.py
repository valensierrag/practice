#Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum
try:
    num1 = int(input("Give me a number"))
    num2 = int(input("Give me another number"))
    if num1*num2 <=1000:
        print("Their product is ", num1*num2)
    else:
        print("Their sum is ", num1+num2)
except ValueError:
    print("I am sorry, but that is not a valid number")

# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
for i in range(11):
    previous =int(i-1) if i > 0 else 0
    print(f"Current number {i}, Previous number {previous}, Sum {i+previous}")
    i +=1

# Write a program to accept a string from the user and display characters that are present at an even index number.
string = input("Type something ")
print(string[:len(string):2])

#Write a program to remove characters from a string starting from zero up to n and return a new string.
strings = input("Type the string")
nn = int(input("Up to which character do you want to delete"))
def remove(string, n):
    """

    :param string: text the user inputs
    :param n: number of characters to delete
    :return: new string
    """
    new_string = string[n:]
    print(f"The new string is {new_string}")

print(remove(strings, nn))

def remove_chars(word, num):
    print('Original string:', word)
    x = word[num:]
    return x

print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))

#Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.
def first_and_last(list):
    """

    :param list: list
    :return: True if the first and last number of a given list is same
    """
    return(list[0] == list[-1])

print(first_and_last([1,2,3,4,5,1]))


