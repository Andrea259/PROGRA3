num1 = int(input("escribe un numero: "))
num2 = int(input("escribe otro numero: "))
num3 = int(input("escribe otro numero: "))

#if(num1>num2&num3)
if(num1>num2 and num1>num3):
    print(f"el mayor es {num1}")
elif(num2>num3 and num2>num3):
    print(f"el mayor es {num2}")
elif(num3>num1 and num3>num1):
    print(f"el mayor es {num3}")
else:
    print("los tres numeros son iguales")