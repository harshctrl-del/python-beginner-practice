import time
a=input("Enter your name:")
timestamp=int(time.strftime("%H"))
# print(timestamp)
if timestamp<12:
    print("Good Morning",a," Sir")
elif 12<timestamp<17:
    print("Good Afternoon",a," Sir")
else:
    print("Good Night",a, "Sir")
