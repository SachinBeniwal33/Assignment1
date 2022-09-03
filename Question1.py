
age=[19,22,19,24,20,25,26,24,25,24]

#sorting the list using sort method

age.sort()
print("The sorted age is: \n{} ".format(age))


min=min(age)
max=max(age)
print("The minimum age is {} and maximum age is {} \n".format(min,max))


#adding min and max age to the list with method.
age.append(min)
age.append(max)
print("Age after appending the minimum and maximum age is :\n {}".format(age))


#median

length=len(age)
median=int(length/2)
print("Median is : {}".format(age[median]))

#average

total=sum(age)
average=total/length
print("Average is : {}".format(average))

#range

range=max-min
print("Range is : {}".format(range))
