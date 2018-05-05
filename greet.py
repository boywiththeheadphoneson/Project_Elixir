#Program to greet Vivek and Ajin

user = input("Who be thou?").lower() 
if (user == 'vivek') | (user == 'ajin'):
    print("Welcome, " + str(user))
else:
    print ("You're not welcome here")
