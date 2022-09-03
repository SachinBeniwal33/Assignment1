text="I am a teacher and I love to inspire and teach people"

#split the string and converting into set
words=set(text.split())
print(words)

#using for loop to get the count of strings present in the set
count=0
for i in words:
    count=count+1
print(count)

