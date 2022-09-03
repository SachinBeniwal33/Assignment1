# create Empty dog dictionary
dog={
}

# add name, color, legs,breed, age to dog dictionary
dog["name"]="kikz"
dog["color"]="black"
dog["legs"]=4
dog["breed"]="Husky"
dog["age"]=7


#create student dictionary firstname, lastname, gender,age,maritalstatus,skills,country,city,address
student={
    "first_name":"Sachin",
    "last_name":"Beniwal",
    "gender":"Male",
    "age":22,
    "marital_status":"Single",
    "skills":["Python","Java"],
    "country":"India",
    "city":"Hyderabad",
    "address":"Medchal"
}


#get the length of the student dictionary

length=len(student)
print("The length of student dictionary is : \n{}".format(length))

#get the value of the skills and check the data type ,it should be list
y=[]
y=student["skills"]
print("The skills are : {} \n".format(y))
print("Type of skills is : {} \n ".format(type(y)))


#modify the skills by adding one or two skills

student["skills"].append("C")
print("The updated skills :{} \n".format(student["skills"]))

#get the dictionary keys as a list

Student_keys=list(student.keys())
Dog_keys=list(dog.keys())

print("The keys are of student dictionary are : {} \n".format(Student_keys))
print("The keys are of dog dictionary are : {} \n".format(Dog_keys))


#get the dictionary values a list

student_values=list(student.values())
dog_values=list(dog.values())

print("The values of student dictionary are : {} \n".format(student_values))
print("The values of dog dictionary are : {} \n".format(dog_values))

