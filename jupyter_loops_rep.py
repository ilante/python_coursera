#Rep of loops
numbers = [2, 3, 4, 45]
l = len(numbers)

for i in range(l):
    print(numbers[i]) # each iteration the i takes on a different 
#value according to len of numbers (4)

for i in range(8):
    print(i) # prints numbers 0 through 7 

for el in numbers:
    print(el)

# using a loop to change elements within a list

items = ['yellow', 'red', 'green', 'purple', 'blue'] #list of colours
for  i in range(5):
    print('Before item ', i , 'is', items[i])
    items[i] = 'different'
    print('After item ', i , 'is', items[i])


items = ['yellow', 'red', 'green', 'purple', 'blue'] #list of colours

for index_of_enumerate, colors in enumerate(items):
    print(index_of_enumerate, colors)

# while:
months = ['june', 'august', 'july', 'may']

i = 0
month = 'a'

while month != 'august':
    month = months[i]
    print(month)
    i += 1

# Write your code below and press Shift+Enter to execute
# Write a while loop to display the values of the Rating of an album playlist stored in the list PlayListRatings. If the score is less than 6, exit the loop. The list PlayListRatings is given by: PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]

i = 0
score = PlayListRatings[i]
#print(score)

while score >= 6:
    score = PlayListRatings[i]
    print(score)
    i += 1

