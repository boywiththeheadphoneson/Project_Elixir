#program to ask the users for "n" numbers, finding if they are divisble by 3 & 5 and finding their sum

num = int(input("Enter n numbers to perform the operation: ")) #n = 4
total_sum = 0 

for n in range(num):
    numbers = int(input("Enter the number: ")) 
    if(numbers % 3 == 0) or (numbers % 5 == 0):  
        total_sum += numbers
        
print(total_sum)




   