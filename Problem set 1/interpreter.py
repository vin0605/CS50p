ae = input("Expression: ")
n1 , y , n2 = ae.split(" ")
x = int(n1)
z = int(n2)
if y == "+":
    ans = x + z
elif y == "-":
    ans = x - z
elif y == "*":
    ans = x * z
elif y == "/":
    ans = x / z

print(round(float(ans), 1))
