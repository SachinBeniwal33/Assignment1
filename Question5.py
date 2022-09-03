radius_of_circle=30

#area of a circle
_area_of_circle_=3.14*radius_of_circle**2
print("The area of Circle 1 is {}".format(_area_of_circle_))

#circumference of a circle
_circum_of_circle_=2*3.14*radius_of_circle
print("The circumference of  Circle 1 is {}".format(_circum_of_circle_))

#taking radius as user input and calculate the area
radius=float(input("Enter the radius "))
def area(radius):
    area_of_circle2=3.14*radius**2
    print("The area of Circle 2 is {}".format(area_of_circle2))
area(radius)
