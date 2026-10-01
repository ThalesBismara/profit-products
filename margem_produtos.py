

produto = (input("Escolha o produto:Digite: 1 -Cone Trufado,2 -Brownie,3- Barra Recheada,4- Cascone,Capuccino,5- Bolo,6- Pudim,7- Copo da Felicidade:  "))


if produto == "1":
   caixa_casquinha_marvi = float(input("Insira o valor do Pacote da Casquinha: "))
   qntd_casquinha = int(input("Insira a quantidade: "))
   casca_total = caixa_casquinha_marvi / qntd_casquinha

   saco_cone = float(input("Insira o valor da embalagem: "))
   qntd_saco = int(input("Insira a quantidade que vem na embalagem: "))
   emba_total = saco_cone / qntd_saco

   fechinho = float(input("Insira o valor da embalagem de fechinho "))
   qntd_fechinho = int(input("Insira a quantidade: "))
   fechinho_total = fechinho / qntd_fechinho

   barra_chocolate = float(input("Qual o valor da Barra de Chocolate de um Kilo? "))
   qntd_choco_casca = int(input("Qual a quantidade de CHOCOLATE você usa para banhar a casquinha? "))
   custo_chocolate = barra_chocolate / qntd_choco_casca

   selo = float(input("Insira o valor do selo: "))
   qntd_selo = int(input("Insira a quantidade: "))
   selo_total = selo / qntd_selo

   custo_casquinha = casca_total + custo_chocolate + emba_total + selo_total
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

     acucar = float(input(" Valor do Kilo do açúcar -OBS -Para fazer 10 Brownies são utilizados 275 gramas "))
     manteiga = float(input("Valor da Menteiga, sem sal: OBS -Para fazer 10 Brownies são utilizados 100 gramas"))
     ovos = float(input("Qual o valor da bandeja com 20 ovos? OBS - Para fazer 10 Brownies são utilizados 3 ovos"))
     farinha = float(input("Insira o valor do KILO da Farinha: OBS - Para fazer 10 Brownies são utilizados 190 gramas  "))
     cacau_po1 = float(input("Insira o valor do  Cacau em Pó 50%: "))
     embalagem = float(input("Insira o valor da embalagem: "))
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
     barra_chocolate = float(input("Qual o valor da Barra de Chocolate de um Kilo? - 130 gramas por Barra "))
     papel_manteiga = float(input(" Qual o valor do Papel Manteiga com 30 Unidades: "))
     embalagem_plastico = float(input(" Insira o valor da Embalagem de plástico com 100: "))
     fechinho = float(input("Insira o valor do fechinho com 100 unidades: "))

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
   fechinho = float(input("Insira o valor do fechinho com 100 unidades: "))
   kraft = float(input(" Insira o valor da Embalagem Kraft com 10: "))

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
     ovo = float(input("Insira o valor da bandeja de ovos com 20: "))
     acucar = float(input("Insira o valor do kilo do açúcar: "))
     cacau_po = float(input("Insira o valor do  Cacau em Pó 50%: "))
     fermento = float(input(" Insira o valor do Fermento"))
     pote = float(input("Insira o valor dos Potes: "))
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

elif produto == "6": #pudim
     
     leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
     ovo = float(input("Insira o valor da bandeja de ovos com 20: "))
     acucar = float(input("Insira o valor do kilo do açúcar: "))
     pote = float(input("Insira o valor dos Potes: "))


elif produto == "7":
     pote = float(input("Insira o valor dos Potes: "))
     
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