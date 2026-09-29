caixa_casquinha = 0
barra_chocolate = 0

produto = (input("Escolha o produto:Digite: 1 -Cone Trufado,2 -Brownie,3- Barra Recheada,4- Cascone,Capuccino,5- Bolo,6- Pudim,7- Pavê Zero Açúcar,8- Copo da Felicidade:  "))


if produto == "1":
   caixa_casquinha_marvi = float(input("Qual o valor da caixa? "))
   unidade = caixa_casquinha_marvi / 300

   saco_cone = float(input("Qual o valor do Saquinho da Embalagem? "))
   fexim = float(input("Insira o valor do Fexim: "))

   barra_chocolate = float(input("Qual o valor da Barra de Chocolate de um Kilo? "))
   custo_chocolate = barra_chocolate / 1000 * 25
   custo_casquinha = unidade + custo_chocolate
   print(f" O custo por casquinha banhada é de: R${custo_casquinha:.2f}")
   sabor = input("Qual sabor do Cone Trufado? 1 -Ninho,2 -Brigadeiro,3 -Kinder Bueno,4- Ferrero Rochet,5 -Duo,6 -Nutella: ")

   if sabor == "1":
        print(" Voce escolheu Ninho, o valor do custo será informado em KILOS")
        leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
        creme_leite = float(input("Insira o valor do creme de leite: "))
        leite_po = float(input("Insira o valor do leite em pó: "))
        
   elif sabor == "2":
        print(" Voce escolheu Brigadeiro, o valor do custo será informado em KILOS")
        leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
        creme_leite = float(input("Insira o valor do creme de leite: "))
        cacau_po = float(input("Insira o valor do leite Cacau em Pó: "))

   elif sabor == "3":
        print(" Voce escolheu Kinder Bueno, o valor do custo será informado em KILOS")
        leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
        creme_leite = float(input("Insira o valor do creme de leite: "))
        kinder = float(input("Insira o valor do  Kinder Bueno: "))

   elif sabor == "4":
        print(" Voce escolheu Ferrero Rochet, o valor do custo será informado em KILOS")
        leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
        creme_leite = float(input("Insira o valor do creme de leite: "))
        ferrero = float(input("Insira o valor do Kinder: "))   
        amemdoim = float(input("Insira o valor do Amemdoim Triturado: "))

   elif sabor == "5":
        print(" Voce escolheu Duo, o valor do custo será informado em KILOS")
        leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
        creme_leite = float(input("Insira o valor do creme de leite: "))

   elif sabor == "6":
        print(" Voce escolheu Nutella, o valor do custo será informado em KILOS")
        nutella = float(input("Insira o valor do Creme de Avelã: ")) 
   else:
        print("Digite um Produto Válido")  

elif produto == "2":
     sabor = input("Qual sabor do Brownie?1 -Ninho,2 -Brigadeiro,3 -Duo")

     if sabor == "1":
        print(" Voce escolheu Ninho, o valor do custo será informado em KILOS")
        leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
        creme_leite = float(input("Insira o valor do creme de leite: "))
        leite_po = float(input("Insira o valor do leite em pó: "))

     elif sabor == "2":
        print(" Voce escolheu Brigadeiro, o valor do custo será informado em KILOS")
        leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
        creme_leite = float(input("Insira o valor do creme de leite: "))
        cacau_po = float(input("Insira o valor do leite Cacau em Pó: "))

     elif sabor == "3":
        print(" Voce escolheu Duo, o valor do custo será informado em KILOS")
        leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
        creme_leite = float(input("Insira o valor do creme de leite: "))

     else:
        print("Digite um Produto Válido")
      
elif produto == "3":
     barra_chocolate = float(input("Qual o valor da Barra de Chocolate de um Kilo? "))

     sabor = input("Qual sabor do Barra Recheada?1 -Ninho,2 -Brigadeiro,3 -Duo: ")

     if sabor == "1":
        print(" Voce escolheu Ninho, o valor do custo será informado em KILOS")
        leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
        creme_leite = float(input("Insira o valor do creme de leite: "))
        leite_po = float(input("Insira o valor do leite em pó: "))

     elif sabor == "2":
        print(" Voce escolheu Brigadeiro, o valor do custo será informado em KILOS")
        leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
        creme_leite = float(input("Insira o valor do creme de leite: "))
        cacau_po = float(input("Insira o valor do leite Cacau em Pó: "))

     elif sabor == "3":
        print(" Voce escolheu Duo, o valor do custo será informado em KILOS")
        leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
        creme_leite = float(input("Insira o valor do creme de leite: "))

     else:
        print("Digite um Produto Válido")
     
elif produto == "4":
   casquinha_marvi_grande = float(input("Qual o valor da caixa? "))
   unidade = casquinha_marvi_grande / 120

   saco_cone = float(input("Qual o valor do Saquinho da Embalagem? "))
   fexim = float(input("Insira o valor do Fexim: "))

   barra_chocolate = float(input("Qual o valor da Barra de Chocolate de um Kilo? "))
   custo_chocolate = barra_chocolate / 1000 * 90
   custo_casquinha = unidade + custo_chocolate
   print(f" O custo por casquinha banhada é de: R${custo_casquinha:.2f}")

   sabor = input("Qual sabor do Cascone ? 1 -Ninho,2 -Brigadeiro,3 -Kinder Bueno,4- Ferrero Rochet,5 -Duo,6 -Nutella: ")

   if sabor == "1":
        print(" Voce escolheu Ninho, o valor do custo será informado em KILOS")
        leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
        creme_leite = float(input("Insira o valor do creme de leite: "))
        leite_po = float(input("Insira o valor do leite em pó: "))
        
   elif sabor == "2":
        print(" Voce escolheu Brigadeiro, o valor do custo será informado em KILOS")
        leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
        creme_leite = float(input("Insira o valor do creme de leite: "))
        cacau_po = float(input("Insira o valor do leite Cacau em Pó: "))

   elif sabor == "3":
        print(" Voce escolheu Kinder Bueno, o valor do custo será informado em KILOS")
        leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
        creme_leite = float(input("Insira o valor do creme de leite: "))
        kinder = float(input("Insira o valor do  Kinder Bueno: "))

   elif sabor == "4":
        print(" Voce escolheu Ferrero Rochet, o valor do custo será informado em KILOS")
        leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
        creme_leite = float(input("Insira o valor do creme de leite: "))
        ferrero = float(input("Insira o valor do Kinder: "))   
        amemdoim = float(input("Insira o valor do Amemdoim Triturado: "))

   elif sabor == "5":
        print(" Voce escolheu Duo, o valor do custo será informado em KILOS")
        leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
        creme_leite = float(input("Insira o valor do creme de leite: "))

   elif sabor == "6":
        print(" Voce escolheu Nutella, o valor do custo será informado em KILOS")
        nutella = float(input("Insira o valor do Creme de Avelã: ")) 
   else:
        print("Digite um Produto Válido") 

elif produto == "5":
     sabor = input("Qual sabor do Bolo? 1 -Ninho,2 -Brigadeiro,3 -Duo: ")

     if sabor == "1":
        print(" Voce escolheu Ninho, o valor do custo será informado em KILOS")
        leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
        creme_leite = float(input("Insira o valor do creme de leite: "))
        leite_po = float(input("Insira o valor do leite em pó: "))
        
     elif sabor == "2":
        print(" Voce escolheu Brigadeiro, o valor do custo será informado em KILOS")
        leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
        creme_leite = float(input("Insira o valor do creme de leite: "))
        cacau_po = float(input("Insira o valor do leite Cacau em Pó: ")) 

     elif sabor == "5":
        print(" Voce escolheu Duo, o valor do custo será informado em KILOS")
        leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
        creme_leite = float(input("Insira o valor do creme de leite: "))

     else:
        print("Digite um Produto Válido")

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

else:
   print("Digite um Produto Válido")