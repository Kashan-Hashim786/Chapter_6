name = "Harry" 
post = input("Write a post : ")
if(name.lower() in post.lower()):
    print("The post is about the Harry")
else:
    print("The post is not about Harry")