
# Count a number of words in a given sentence

sentence = input("Enter your string here")
print(sentence)
count=0
for i in sentence:
    if i == " ":
        count+=1
print("The number of words in a sentence:",count+1)




