import random
def a(names_of_maember,room):
    no_members=random.randint(1,10)
    flor=random.randint(1,6)
    name_of_members=random.sample(name_of_members,no_members)
    print("room","=",room,"no of member","=",no_members,"flor","=",flor)
    print(name_of_members)
        

room=int(input("enter the room no.:-"))
names_of_members=["riti","sarita","laxmi","Aahan","Parth","Aadvika","Aakriti","Aadiya","Viaan","Ridhaan","Nehal","Neel","Ahir","Aagar","Amargeet","Ambadas","Arun","Bhairav","Bilas"]
a(names_of_members,room)
