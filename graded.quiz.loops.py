# # A=[1,2,3]
# # for a in A:
# #   print(2*a)

x=7
while x !=2:
    print(x)
    x=x-1


# Enumerate() in Python

# A lot of times when dealing with iterators, we also get a need to keep a count of iterations. Python eases the programmers’ task by providing a built-in function enumerate() for this task.
# Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.

# li=['a', 'b', 'c']
# print(list(enumerate(li, start=0)))

# # for i,x in enumerate(['A','B','C']):
# #     print(i,2*x)


# # Python program to illustrate 
# # enumerate function 
# l1 = ['eat','sleep','repeat'] 
# s1 = 'geek'
  
# # creating enumerate objects 
# obj1 = enumerate(l1) 
# obj2 = enumerate(s1) 
  
# print("Return type:" , type(obj1))
# print(list(enumerate(l1)))
  
# # changing start index to 2 from 0 
# print(list(enumerate(s1,2)))

# for i,x in enumerate(['A','B','C']): # i is assigned the index
#     print(i,2*x) # x is assigned the element of the list 

# for i in range(1,5):
#     if i==2:
#         print(i)