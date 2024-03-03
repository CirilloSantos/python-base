salario = int(input(("digite seu salario: ")))
aumento = 30
imposto = 1200

print(salario + (salario * aumento / 100))

if salario >= imposto:
    print("Sim, pagara o imposto DEVIDO")
if salario <= imposto:
    print("Não pagara o imposto")    

 