#create a tuple names of your sisters and brothers
brothers=("Kunny","Munny","Sunny")
sisters=("Geetha","Babitha","Lalitha")

#join brothers and sisters and assign to siblings
siblings=brothers+sisters
print(siblings)

#how many siblings do you have
length=len(siblings)
print(length)

#modify tuple and add the names of your father and mother and assign to family members

#converting set to list
sibling_list=list(siblings)

#appending mother and father names to the list
sibling_list.append("papa")
sibling_list.append("mummy")

#converting sibiling to set and assiging the set to family_members
family_members=set(sibling_list)
print(family_members)
