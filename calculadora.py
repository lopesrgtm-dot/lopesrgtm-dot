nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) /3
print(f"sua media é {media:.2f}")

if media >= 7:
    print ("Aprovado")
elif media >= 5 :
    print ("Recuperação")
else:
    print ("Reprovado")
