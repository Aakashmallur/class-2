

sentence=input("enter the sentace")
sentence=sentence.lower()

dictionary={}
for letter in sentence:
    if letter.isalpha():
        if letter not in dictionary:
          dictionary[letter]=1
        else:
           dictionary[letter]+=1
if len(dictionary)==26:
   print("this is a a panogram")
else:
   print("not a panogram")