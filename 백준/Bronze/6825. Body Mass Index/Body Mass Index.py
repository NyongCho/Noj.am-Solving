import sys
input = sys.stdin.readline

w = float(input().strip())
h = float(input().strip())

BMI = w/(h*h)

if BMI >= 25:
    print("Overweight")
elif BMI >= 18.5:
    print("Normal weight")
else:
    print("Underweight")