num1 = int(input())
num2 = int(input())

result = num1 * (num1 // num2) + num2 * (num2 // num1)

result = result // (num1 // num2 + num2 // num1)

print(result)
