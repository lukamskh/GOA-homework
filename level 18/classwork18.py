amount = int(input("enter any amount: "))
numbers = []
for i in range (amount):
 num = int(input("enter number " + str(i + 1) + ": "))
           
 numbers.append(num)
print(sum(numbers))
