phrase1 = "Make a lot of money"
phrase2 = "buy now"
phrase3= "subscribe this"
phrase4 = "click this"

text = input("Enter Comment : ")
if(phrase1 in text):
    print("This comment is a spam")
elif(phrase2 in text):
    print("This comment is a spam")
elif(phrase3 in text):
    print("This comment is a spam")
elif(phrase4 in text):
    print("This comment is a spam")
else:
    print("This comment is not a spam")