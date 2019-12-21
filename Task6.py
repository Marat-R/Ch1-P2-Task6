a = int(input("Number: "))
b = str(a)
if -10 < a < 10:
    print(int(b[-1]))
elif 10 <= a:
    print(int(b[-2]))
elif a <= -10:
    print(int(b[-2]))
else:
    print("Error")
