it_companies={'Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'}
A={19,22,24,20,25,26}
B={19,22,20,25,26,24,28,27}
age=[22,19,24,25,26,24,25,24]

#length of the set it_companies using length method

length_of_it_companies=len(it_companies)
print("\n Length of IT companies : {}".format(length_of_it_companies))

#length of the set it_companies without using length method

#count=0
#for i in it_companies:
    #count=count+1

#add twitter to the it_companies

it_companies.add("Twitter")
print("\n After adding twitter to the it companies : \n{} ".format(it_companies))

#add multiple it companies to the set it_companies

it_companies.update(["Infosys","Tech Mahindra","Capgemini"])
print("\n After adding multiple companies  to the it companies : \n{} ".format(it_companies))

#remove one of the companies from set it_companies

it_companies.remove('Infosys')
print("\n Removing Infosys from the set : \n{} ".format(it_companies))


#what is the difference between remove and discard

#The built-in Python function remove() works similarly to the discard() method in that it only
# removes an element from the set if it is already there. An error or exception is thrown if the element is missing from the set.

#removing the value which is not present in the set

#it_companies.remove('Meta')

#discarding the value which is not present in the set

#it_companies.discard('Meta')


#join A and B

join=A.union(B)
print("\n Joining A and B : \n{} ".format(join))


#A intersection B

intersect=A.intersection(B)
print("The intersection of A and B : \n  {}".format(intersect))

#Is A subset of B

print("Is A subset of B : \n {}".format(A.issubset(B)))


#Are A and B disjoint Sets

print("Are A and B are disjoint sets : \n {}".format(A.isdisjoint(B)))

#join a with b and b with a

joina=A.union(B)
joinb=B.union(A)
print("Joining A with B : \n {}".format(joina))
print("Joining B with A : \n {}".format(joinb))

#what is the symmetric difference between a and b

symmetric_difference=A.symmetric_difference(B)
print("The symmetric difference between A and B is : \n {}".format(symmetric_difference))

#delete the sets completely

A.clear()
B.clear()


#convert ages to set and compare the length of the list to the set

age_List=set(age)
print("Length of age in set format : \n {}".format(len(age_List)))
print("Length of age in List format: \n {}".format(len(age)))


