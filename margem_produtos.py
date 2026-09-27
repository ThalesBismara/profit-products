produtos = {
   # "Cone Trufado": Casquinha Marvi,Choco Meio Amargo Top Harald,
    "Brownie": 12.90,
    "Barra Recheada": 24.90,
    "Cascone": 23.90,
    "Bolo": 12.70,
}

produto = (input("Escolha o produto:Digite: 1 -Cone Trufado,2 -Brownie,3- Barra Recheada,4- Cascone,Capuccino,5- Bolo,6- Pudim,7- Pavê Zero Açúcar,8- Copo da Felicidade:  "))


if produto == "1":
     sabor = input("Qual sabor do Cone Trufado? 1 -Ninho,2 -Brigadeiro,3 -Kinder Bueno,4- Ferrero Rochet,5 -Duo,6 -Nutella: ")

     if sabor == "1":
        print(" Voce escolheu Ninho")
     elif sabor == "2":
        print(" Voce escolheu Brigadeiro")
     elif sabor == "3":
        print(" Voce escolheu Kinder Bueno") 
     elif sabor == "4":
        print(" Voce escolheu Ferrero Rochet")       
     elif sabor == "5":
        print(" Voce escolheu Duo")       
     elif sabor == "6":
        print(" Voce escolheu Nutella")      

elif produto == "2":
     sabor = input("Qual sabor do Brownie?1 -Ninho,2 -Brigadeiro,3 -Duo")

     if sabor == "1":
        print(" Voce escolheu Ninho")
     elif sabor == "2":
        print(" Voce escolheu Brigadeiro")     
     elif sabor == "3":
        print(" Voce escolheu Duo")       

elif produto == "3":
     sabor = input("Qual sabor do Barra Recheada?1 -Ninho,2 -Brigadeiro,3 -Duo: ")

     if sabor == "1":
        print(" Voce escolheu Ninho")
     elif sabor == "2":
        print(" Voce escolheu Brigadeiro")     
     elif sabor == "3":
        print(" Voce escolheu Duo")  
     
elif produto == "4":
     sabor = input("Qual sabor do Cascone ? 1 -Ninho,2 -Brigadeiro,3 -Kinder Bueno,4- Ferrero Rochet,5 -Duo,6 -Nutella: ")

     if sabor == "1":
        print(" Voce escolheu Ninho")
     elif sabor == "2":
        print(" Voce escolheu Brigadeiro")
     elif sabor == "3":
        print(" Voce escolheu Kinder Bueno") 
     elif sabor == "4":
        print(" Voce escolheu Ferrero Rochet")       
     elif sabor == "5":
        print(" Voce escolheu Duo")       
     elif sabor == "6":
        print(" Voce escolheu Nutella")  

elif produto == "5":
     sabor = input("Qual sabor do Bolo? 1 -Ninho,2 -Brigadeiro,3 -Duo: ")

     if sabor == "1":
        print(" Voce escolheu Ninho")
     elif sabor == "2":
        print(" Voce escolheu Brigadeiro")     
     elif sabor == "3":
        print(" Voce escolheu Duo") 

elif produto == "6":
     sabor = input("Qual sabor do Pudim ")

elif produto == "7":
     sabor = input("Qual sabor do Pave Zero ")

elif produto == "8":
     sabor = input("Qual sabor do Copo da Felicidade? 1 -Ninho,2 -Brigadeiro,3 -Kinder Bueno,4- Ferrero Rochet,5 -Duo,6 -Nutella: ")

     if sabor == "1":
        print(" Voce escolheu Ninho")
     elif sabor == "2":
        print(" Voce escolheu Brigadeiro")
     elif sabor == "3":
        print(" Voce escolheu Kinder Bueno") 
     elif sabor == "4":
        print(" Voce escolheu Ferrero Rocher")       
     elif sabor == "5":
        print(" Voce escolheu Duo")       
     elif sabor == "6":
        print(" Voce escolheu Nutella")  

else:
   print("Digite um Produto Válido")