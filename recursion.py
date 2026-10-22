def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

print(input(factorial))

#factorial
n=int(input("Enter your Number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("Factorial:",fact)

#Palindrome
word=str(input("Enter your Number:"))
reverse=word[::-1]
if word==reverse:
    print("Pallindrome")
else:
    print("not a palliondrome")

#Armstrong
num = int(input("enter your number:"))
original=num
digits=len(str(num))
sum=0
while num>0:
    digit=num%10
    sum=sum+digit**digits
if sum==original:
    print("Armstrong number")

#fibonacci series
n=int(input("enter your number:"))
a=0
b=1
for i in range(n):
    print(a,end="")
    a,b=b,a+b


#Perfect Number
num=int(input("enter your number"))
sum=0
for i in range(1,num):
    if num%i==0
    sum=sum+i

if sum==sum:
    print("Num is perfect")
else:
    print("Your number is not perfect")


#GCD
x=int(input("Enter your number:"))
y=int(input("Enter your number:"))
if(x==0 or y==o);
    print("Value must be non zero")
else:
    while(y!=0):
        x,y=y,x%y
    print("GCD",x)


#perfect or not 
num=int(input("enter your number"))
divisor_num=0
for i in range(1,num):
    if num%i==0:
        divisor_num+=1
if divisor_num==num:
    print(num,"is a perfect number")
else:
    print(num,"is not a prime number")



#perfect or not
num=7
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print(num,"is prime")
else:
    print(num,"is not prime")

#leap year
year=int(input("Enter your number:"))
if year%4==0:
    print("leap year")
else:
    ("not a leap year")



