# # Classes jupyter
# # Import the library

# import matplotlib.pyplot as plt
# matplotlib inline

# #creating the class circle.

# class Circle(object):

#     #constructor
#     def _init_(self, radius=3, color='blue'):
#         self.radius = radius
#         self.color = color

# # method
# def add_radius(self, r):
#     self.radius = self.radius + r
#     return(self.radius)

# # method 
# def drawCircle(self):
#     plt.gca().add_patch(plt.circle((0,0), radius=self.radius, fc=self.color))
#     plt.axis('scaled')
#     plt.show

# # Create an object RedCircle

# RedCircle = Circle(10, 'red')

# # Find out the methods can be used on the object RedCircle

# dir(RedCircle)

class Points(object):
  def __init__(self,x,y):

    self.x=x
    self.y=y

  def print_point(self):

    print('x=',self.x,' y=',self.y)

p1=Points("A","B")
p1.print_point()

class Points(object):

  def __init__(self,x,y):

    self.x=x
    self.y=y

  def print_point(self):

    print('x=',self.x,' y=',self.y)

p2=Points(1,2)

p2.x='A'

p2.print_point()