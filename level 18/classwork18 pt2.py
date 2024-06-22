num = int(input("enter amount of seconds: "))
num2 = int(input("enter amount: "))
for i in range (num):
    i = i + 1
    print(i)
if i <= num2:
    print("your number is below " + str(num2))
else:
    print("your number is above " + str(num2))