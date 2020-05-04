# lists / arrays
# lists can hold multiple values

numbers = [] # defining a list called numbers with no values
print(numbers)

numbers.append(10)
print(numbers)

numbers.append(15)
print(numbers)

numbers.append(-15)
print(numbers)

# initialize a list while creating it

myList = [2, 5, -4, 25, 100]
print("myList =", myList)

# printing the values of "myList" one value per line
print("printing elements one by one")
print(myList[0])
print(myList[1])
print(myList[2])
print(myList[3])
print(myList[4])

# you can use a FOR loop to print values easily
print("using a FOR loop")
for val in myList:
    print(val)

# use a For loop to add all the values in myList (cumulative sum)
total = 0
for val in myList:
    total = total + val
    print("current total =", total)

print("final total =", total)

# if we need to use a FOR loop to iterate through a range of numbers from
# 1-100 so we can use a "range" function instead of a list defining each
# number individually

# adding all numbers from 1-100
total = 0
for i in range(1, 100):
    total = total + i
print("the sum of numbers from 1 to 100 =", total)

# lists with strings
fruits = ["banana", "apple", "grape", "pineapple"]
for fruit in fruits:
    print(fruit)
    print(fruits)


# define a range of numbers
r1 = range(5)

# print(r1[0], r1[1], r1[2], r1[3], r1[4])