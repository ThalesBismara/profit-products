
produto = (input("Escolha o produto:Digite: 1 -Cone Trufado,2 -Brownie,3- Barra Recheada,4- Cascone,5- Bolo,6- Pudim,7- Copo da Felicidade:  "))


if produto == "1":
    caixa_casquinha_marvi = float(input("Insira o valor do Pacote da Casquinha: "))
    qntd_casquinha = int(input("Insira a quantidade: "))
    casca_total = caixa_casquinha_marvi / qntd_casquinha

    saco_cone = float(input("Insira o valor da embalagem: "))
    qntd_saco = int(input("Insira a quantidade que vem na embalagem: "))
    emba_total = saco_cone / qntd_saco

    fechinho = float(input("Insira o valor da embalagem de fechinho: "))
    qntd_fechinho = int(input("Insira a quantidade: "))
    fechinho_total = fechinho / qntd_fechinho

    barra_chocolate = float(input("Qual o valor da Barra de Chocolate: "))
    qntd_choco = int(input("Quantos GRAMAS tem a barra? "))
    total_choco = (barra_chocolate / qntd_choco) * 20

    selo = float(input("Insira o valor do selo: "))
    qntd_selo = int(input("Insira a quantidade: "))
    selo_total = selo / qntd_selo

    custo_casquinha = casca_total +  emba_total + fechinho_total + total_choco + selo_total

    print(f"O custo por casquinha banhada é de: R${custo_casquinha:.2f}")

    sabor = input("Qual sabor do Cone Trufado? 1 - Ninho, 2 - Brigadeiro, 3 - Kinder Bueno, 4 - Ferrero Rochet, 5 - Duo, 6 - Nutella: ")

    if sabor == "1":
        print("Ninho, a quantidade de ingredientes será para um KILO de recheio!")

        leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
        total_condensado = leite_condensado * 3

        creme_leite = float(input("Insira o valor do creme de leite: "))
        total_creme = creme_leite * 3

        manteiga = float(input("Insira o valor da manteiga: "))
        peso_manteiga = int(input("Insira o peso: "))
        total_manteiga = (manteiga / peso_manteiga) * 30

        leite_po = float(input("Insira o valor do leite em pó: "))
        peso_leite_po = int(input("Insira quantos gramas tem o pacote: "))
        total_leite_po = (leite_po / peso_leite_po) * 400

        total_ninho = total_condensado + total_creme + total_leite_po + total_manteiga
        custo_por_uni = (total_ninho / 1000) * 80 
        custo_unidade_reche = custo_por_uni + custo_casquinha

        print(f"O custo por kilo é de: R${total_ninho}")
        print(f"O custo por casquinha banhada e recheada é de: R${custo_unidade_reche:.2f}")

    elif sabor == "2":
       print("Brigadeiro, a quantidade de ingredientes será para um KILO de recheio!")

       leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
       total_condensado = leite_condensado * 3

       creme_leite = float(input("Insira o valor do creme de leite: "))
       total_creme = creme_leite * 3

       cacau_po = float(input("Insira o valor do Cacau em Pó: "))
       qntd_cacau = int(input("Insira quantos gramas tem o pacote de cacau em pó 50%: "))
       total_cacau = (cacau_po / qntd_cacau) * 80

       total_brigadeiro = total_condensado + total_creme + total_cacau

       custo_por_uni = (total_brigadeiro / 1000) * 80
       custo_unidade_reche = custo_por_uni + custo_casquinha

       print(f"Custo total do Brigadeiro por kilo: R${total_brigadeiro:.2f}")
       print(f"Custo total do Brigadeiro por unidade banhada e recheada: R${custo_unidade_reche:.2f}")

    elif sabor == "3":
       print("Kinder Bueno, a quantidade de ingredientes será para um KILO de recheio!")

       avela = float(input("Insira o valor da Pasta de Avelã: "))
       peso_avela = int(input("Insira quantos gramas tem o pacote: "))
       total_avela = (avela / peso_avela) * 450

       leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
       total_condensado = leite_condensado * 3

       creme_leite = float(input("Insira o valor do creme de leite: "))
       total_creme = creme_leite * 3

       leite_po = float(input("Insira o valor do leite em pó: "))
       peso_leite_po = int(input("Insira quantos gramas tem o pacote: "))
       total_leite_po = (leite_po / peso_leite_po) * 750

       total_kinder_bueno = total_avela + total_condensado + total_creme + total_leite_po

       custo_por_uni = (total_kinder_bueno / 1000) * 80
       custo_unidade_reche = custo_por_uni + custo_casquinha

       print(f"O custo por kilo é de: R${total_kinder_bueno:.2f}")
       print(f"O custo por casquinha banhada e recheada é de: R${custo_unidade_reche:.2f}")

    elif sabor == "4":
       print("Ferrero Rocher, a quantidade de ingredientes será para um KILO de recheio!")

       leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
       total_condensado = leite_condensado * 3

       creme_leite = float(input("Insira o valor do creme de leite: "))
       total_creme = creme_leite * 3

       ferrero = float(input("Insira o valor do Ferrero Rocher: "))
       qntd_ferrero = int(input("Insira quantas unidades tem a embalagem: "))
       total_ferrero = (ferrero / qntd_ferrero) * 2

       amendoim = float(input("Insira o valor do amendoim triturado: "))
       qntd_amendoim = int(input("Quantos gramas tem o pacote: "))
       total_amendoim = (amendoim / qntd_amendoim) * 60

       total_ferrero_rocher = total_condensado + total_creme + total_ferrero + total_amendoim

       custo_por_uni = (total_ferrero_rocher / 1000) * 80
       custo_unidade_reche = custo_por_uni + custo_casquinha

       print(f"O custo por kilo é de: R${total_ferrero_rocher:.2f}")
       print(f"O custo por casquinha banhada e recheada é de: R${custo_unidade_reche:.2f}")

    elif sabor == "5":
       print("Duo, a quantidade de ingredientes será para um KILO de recheio!")

    # Recheio de Ninho
       leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
       total_condensado_ninho = leite_condensado * 3

       creme_leite = float(input("Insira o valor do creme de leite: "))
       total_creme_ninho = creme_leite * 3

       manteiga = float(input("Insira o valor da manteiga: "))
       peso_manteiga = int(input("Insira o peso em gramas: "))
       total_manteiga = (manteiga / peso_manteiga) * 30

       leite_po = float(input("Insira o valor do leite em pó: "))
       peso_leite_po = int(input("Insira quantos gramas tem o pacote: "))
       total_leite_po = (leite_po / peso_leite_po) * 400

       total_ninho = (
        total_condensado_ninho
        + total_creme_ninho
        + total_manteiga
        + total_leite_po )

    # Recheio de Brigadeiro
       leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
       total_condensado_brigadeiro = leite_condensado * 3

       creme_leite = float(input("Insira o valor do creme de leite: "))
       total_creme_brigadeiro = creme_leite * 3

       cacau_po = float(input("Insira o valor do cacau em pó 50%: "))
       qntd_cacau = int(input("Insira quantos gramas tem o pacote: "))
       total_cacau = (cacau_po / qntd_cacau) * 80

       total_brigadeiro = (
        total_condensado_brigadeiro
        + total_creme_brigadeiro
        + total_cacau
    )

    # Custo do recheio Duo
       custo_duo_por_kilo = (total_ninho + total_brigadeiro) / 2

       custo_por_uni = (custo_duo_por_kilo / 1000) * 80
       custo_unidade_reche = custo_por_uni + custo_casquinha

       print(f"Custo do Ninho por receita: R${total_ninho:.2f}")
       print(f"Custo do Brigadeiro por receita: R${total_brigadeiro:.2f}")
       print(f"Custo do recheio Duo por kilo: R${custo_duo_por_kilo:.2f}")
       print(f"Custo por casquinha banhada e recheada: R${custo_unidade_reche:.2f}")

    elif sabor == "6":
        print("Você escolheu Nutella, o valor do custo será informado em KILOS")

        nutella = float(input("Insira o valor do Creme de Avelã: "))
        qntd_nutella = int(input("Insira a quantidade: "))
        total_nutella = (nutella / qntd_nutella) * 60

        custo_unidade_reche = total_nutella + custo_casquinha 

    else:
        print("Digite um Produto Válido")

elif produto == "2":

    preco_acucar = float(input("Valor do Kilo do açúcar:  "))
    peso_acucar = float(input("Peso no saco do açúcar em gramas: "))
    preco_por_grama = preco_acucar / peso_acucar
    total_acucar = preco_por_grama * 275


    manteiga = float(input("Valor da Manteiga sem sal - OBS: Para fazer 10 Brownies são utilizados 100 gramas: "))
    total_manteiga = manteiga / 2

    ovos = float(input("Qual o valor da bandeja de ovos? OBS: "))
    qntd_ovos = float(input("Quantidade de Ovos na bandeja: "))
    uni_ovos = ovos / qntd_ovos
    total_ovos = uni_ovos * 3


    farinha = float(input("Insira o valor da Farinha: "))
    qntd_farinha = float(input("Quantos gramas tem o pacote de farinha?: "))
    preco_farinha = farinha / qntd_farinha 
    total_farinha = preco_farinha * 190

    cacau_po = float(input("Insira o valor do Cacau em Pó 50%: "))
    qntd_cacau = float(input("Insira quantos gramas: "))
    preco_cacau = cacau_po / qntd_cacau
    total_cacau = preco_cacau * 100

    embalagem = float(input("Insira o valor da embalagem: "))
    qntd_emba = int(input("Quantas embalagens: "))
    unid_emba = embalagem / qntd_emba

    preco_brownie = (total_acucar + total_manteiga + total_ovos + total_farinha + total_cacau + unid_emba) / 10
    print(preco_brownie)

    sabor = input("Qual sabor do Brownie? 1 - Ninho, 2 - Brigadeiro, 3 - Duo: ")

    if sabor == "1":
        print("Ninho, a quantidade de ingredientes será para um KILO de recheio!")

        leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
        total_condensado = leite_condensado * 3

        creme_leite = float(input("Insira o valor do creme de leite: "))
        total_creme = creme_leite * 3

        manteiga = float(input("Insira o valor da manteiga: "))
        peso_manteiga = int(input("Insira o peso: "))
        total_manteiga = (manteiga / peso_manteiga) * 30

        leite_po = float(input("Insira o valor do leite em pó: "))
        peso_leite_po = int(input("Insira quantos gramas tem o pacote: "))

        valor_por_grama_leite_po = leite_po / peso_leite_po
        total_leite_po = valor_por_grama_leite_po * 400

        total_ninho = total_condensado + total_creme + total_leite_po + total_manteiga
        custo_por_kilo = (total_ninho / 1000) * 80 
        custo_por_unidade = (custo_por_kilo / 80) + preco_brownie


        print(f"Custo total de produção Por UNIDADE recheada: R${custo_por_unidade:.2f}")

    elif sabor == "2":
       print("Brigadeiro, a quantidade de ingredientes será para um KILO de recheio!")

       leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
       total_condensado = leite_condensado * 3

       creme_leite = float(input("Insira o valor do creme de leite: "))
       total_creme = creme_leite * 3

       cacau_po = float(input("Insira o valor do Cacau em Pó: "))
       qntd_cacau = int(input("Insira quantos gramas tem o pacote de cacau em pó 50%: "))
       total_cacau = (cacau_po / qntd_cacau) * 80

       total_brigadeiro = total_condensado + total_creme + total_cacau

       custo_por_uni = (total_brigadeiro / 1000) * 80
       custo_unidade_reche = custo_por_uni + preco_brownie

       print(f"Custo total do Brigadeiro por kilo: R${total_brigadeiro:.2f}")
       print(f"Custo total do Brigadeiro por unidade banhada e recheada: R${custo_unidade_reche:.2f}")

    elif sabor == "3":
        print("Você escolheu Duo, o valor do custo será informado em KILOS")

        leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
        creme_leite = float(input("Insira o valor do creme de leite: "))

    else:
        print("Digite um Produto Válido")
      
elif produto == "3":
     barra_chocolate = float(input("Qual o valor da Barra de Chocolate de um Kilo?: "))
     qntd_barra = int(input("Qual o peso?: "))
     peso_barra = barra_chocolate / qntd_barra
     total_barra = peso_barra * 120

     papel_manteiga = float(input(" Qual o valor do Papel Manteiga: "))
     qntd_papel = int(input("Qual a quantidade?: "))
     total_papel_manteiga = (papel_manteiga / qntd_papel) / 8

     embalagem_plastico = float(input(" Insira o valor da Embalagem: "))
     qntd_embalagem = int(input("Quantos na embalagem?: "))
     total_embalagem = embalagem_plastico / qntd_embalagem

     fechinho = float(input("Insira o valor do fechinho: "))
     qntd_fechinho = int(input("Qual a quantidade: "))
     total_fechinho = fechinho / qntd_fechinho

     barra = total_barra + total_papel_manteiga + total_embalagem + total_fechinho
     print(barra)

     sabor = input("Qual sabor do Barra Recheada?1 -Ninho,2 -Brigadeiro,3 -Duo: ")

     if sabor == "1":
        print("Ninho, a quantidade de ingredientes será para um KILO de recheio!")

        leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
        total_condensado = leite_condensado * 3

        creme_leite = float(input("Insira o valor do creme de leite: "))
        total_creme = creme_leite * 3

        manteiga = float(input("Insira o valor da manteiga: "))
        peso_manteiga = int(input("Insira o peso: "))
        total_manteiga = (manteiga / peso_manteiga) * 30

        leite_po = float(input("Insira o valor do leite em pó: "))
        peso_leite_po = int(input("Insira quantos gramas tem o pacote: "))
        total_leite_po = (leite_po / peso_leite_po) * 400

        total_ninho = total_condensado + total_creme + total_leite_po + total_manteiga
        custo_por_uni = (total_ninho / 1000) * 80 
        custo_unidade_reche = custo_por_uni + barra

        print(f"O custo por kilo é de: R${total_ninho}")
        print(f"O custo por casquinha banhada e recheada é de: R${custo_unidade_reche:.2f}")

     elif sabor == "2":
       print("Brigadeiro, a quantidade de ingredientes será para um KILO de recheio!")

       leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
       total_condensado = leite_condensado * 3

       creme_leite = float(input("Insira o valor do creme de leite: "))
       total_creme = creme_leite * 3

       cacau_po = float(input("Insira o valor do Cacau em Pó: "))
       qntd_cacau = int(input("Insira quantos gramas tem o pacote de cacau em pó 50%: "))
       total_cacau = (cacau_po / qntd_cacau) * 80

       total_brigadeiro = total_condensado + total_creme + total_cacau

       custo_por_uni = (total_brigadeiro / 1000) * 130
       custo_unidade_reche = custo_por_uni + barra

       print(f"Custo total do Brigadeiro por kilo: R${total_brigadeiro:.2f}")
       print(f"Custo total do Brigadeiro por unidade banhada e recheada: R${custo_unidade_reche:.2f}")

     elif sabor == "3":
       print("Duo, a quantidade de ingredientes será para um KILO de recheio!")

    # Recheio de Ninho
       leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
       total_condensado_ninho = leite_condensado * 3

       creme_leite = float(input("Insira o valor do creme de leite: "))
       total_creme_ninho = creme_leite * 3

       manteiga = float(input("Insira o valor da manteiga: "))
       peso_manteiga = int(input("Insira o peso em gramas: "))
       total_manteiga = (manteiga / peso_manteiga) * 30

       leite_po = float(input("Insira o valor do leite em pó: "))
       peso_leite_po = int(input("Insira quantos gramas tem o pacote: "))
       total_leite_po = (leite_po / peso_leite_po) * 400

       total_ninho = (
        total_condensado_ninho
        + total_creme_ninho
        + total_manteiga
        + total_leite_po )

    # Recheio de Brigadeiro
       leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
       total_condensado_brigadeiro = leite_condensado * 3

       creme_leite = float(input("Insira o valor do creme de leite: "))
       total_creme_brigadeiro = creme_leite * 3

       cacau_po = float(input("Insira o valor do cacau em pó 50%: "))
       qntd_cacau = int(input("Insira quantos gramas tem o pacote: "))
       total_cacau = (cacau_po / qntd_cacau) * 80

       total_brigadeiro = (
        total_condensado_brigadeiro
        + total_creme_brigadeiro
        + total_cacau
    )

    # Custo do recheio Duo
       custo_duo_por_kilo = (total_ninho + total_brigadeiro) / 2

       custo_por_uni = (custo_duo_por_kilo / 1000) * 130
       custo_unidade_reche = custo_por_uni + barra

       print(f"Custo do Ninho por receita: R${total_ninho:.2f}")
       print(f"Custo do Brigadeiro por receita: R${total_brigadeiro:.2f}")
       print(f"Custo do recheio Duo por kilo: R${custo_duo_por_kilo:.2f}")
       print(f"Custo por casquinha banhada e recheada: R${custo_unidade_reche:.2f}")
     else:
        print("Digite um Produto Válido")
     
elif produto == "4":
   caixa_casquinha_marvi = float(input("Insira o valor do Pacote da Casquinha: "))
   qntd_casquinha = int(input("Insira a quantidade: "))
   casca_total = caixa_casquinha_marvi / qntd_casquinha

   saco_cone = float(input("Insira o valor da embalagem: "))
   qntd_saco = int(input("Insira a quantidade que vem na embalagem: "))
   emba_total = saco_cone / qntd_saco

   fechinho = float(input("Insira o valor da embalagem de fechinho "))
   qntd_fechinho = int(input("Insira a quantidade: "))
   fechinho_total = fechinho / qntd_fechinho

   barra_chocolate = float(input("Qual o valor da Barra de Chocolate: "))
   qntd_choco = int(input(" Quantos GRAMAS tem a barra?"))
   total_choco =  barra_chocolate / qntd_choco

   qntd_choco_casca = int(input("Qual a quantidade de CHOCOLATE você usa para banhar a casquinha? "))
   custo_chocolate = total_choco * qntd_choco_casca

   selo = float(input("Insira o valor do selo: "))
   qntd_selo = int(input("Insira a quantidade: "))
   selo_total = selo / qntd_selo

   custo_casquinha = casca_total + custo_chocolate + emba_total + selo_total

   sabor = input("Qual sabor do Cascone ? 1 -Ninho,2 -Brigadeiro,3 -Kinder Bueno,4- Ferrero Rochet,5 -Duo,6 -Nutella: ")

   if sabor == "1":
        print("Ninho, a quantidade de ingredientes será para um KILO de recheio!")

        print("Ninho, a quantidade de ingredientes será para um KILO de recheio!")

        leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
        total_condensado = leite_condensado * 3

        creme_leite = float(input("Insira o valor do creme de leite: "))
        total_creme = creme_leite * 3

        manteiga = float(input("Insira o valor da manteiga: "))
        peso_manteiga = int(input("Insira o peso: "))
        total_manteiga = (manteiga / peso_manteiga) * 30

        leite_po = float(input("Insira o valor do leite em pó: "))
        peso_leite_po = int(input("Insira quantos gramas tem o pacote: "))
        total_leite_po = (leite_po / peso_leite_po) * 400

        total_ninho = total_condensado + total_creme + total_leite_po + total_manteiga
        custo_por_uni = (total_ninho / 1000) * 130 
        custo_unidade_reche = custo_por_uni + custo_casquinha

        print(f"O custo por kilo é de: R${total_ninho}")
        print(f"O custo por casquinha banhada e recheada é de: R${custo_unidade_reche:.2f}")

        
   elif sabor == "2":
       print("Brigadeiro, a quantidade de ingredientes será para um KILO de recheio!")

       leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
       total_condensado = leite_condensado * 3

       creme_leite = float(input("Insira o valor do creme de leite: "))
       total_creme = creme_leite * 3

       cacau_po = float(input("Insira o valor do Cacau em Pó: "))
       qntd_cacau = int(input("Insira quantos gramas tem o pacote de cacau em pó 50%: "))
       total_cacau = (cacau_po / qntd_cacau) * 80

       total_brigadeiro = total_condensado + total_creme + total_cacau

       custo_por_uni = (total_brigadeiro / 1000) * 130
       custo_unidade_reche = custo_por_uni + custo_casquinha

       print(f"Custo total do Brigadeiro por kilo: R${total_brigadeiro:.2f}")
       print(f"Custo total do Brigadeiro por unidade banhada e recheada: R${custo_unidade_reche:.2f}")

   elif sabor == "3":
       print("Kinder Bueno, a quantidade de ingredientes será para um KILO de recheio!")

       avela = float(input("Insira o valor da Pasta de Avelã: "))
       peso_avela = int(input("Insira quantos gramas tem o pacote: "))
       total_avela = (avela / peso_avela) * 450

       leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
       total_condensado = leite_condensado * 3

       creme_leite = float(input("Insira o valor do creme de leite: "))
       total_creme = creme_leite * 3

       leite_po = float(input("Insira o valor do leite em pó: "))
       peso_leite_po = int(input("Insira quantos gramas tem o pacote: "))
       total_leite_po = (leite_po / peso_leite_po) * 750

       total_kinder_bueno = total_avela + total_condensado + total_creme + total_leite_po

       custo_por_uni = (total_kinder_bueno / 1000) * 80
       custo_unidade_reche = custo_por_uni + custo_casquinha

       print(f"O custo por kilo é de: R${total_kinder_bueno:.2f}")
       print(f"O custo por casquinha banhada e recheada é de: R${custo_unidade_reche:.2f}")
 
   elif sabor == "4":
       print("Ferrero Rocher, a quantidade de ingredientes será para um KILO de recheio!")

       leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
       total_condensado = leite_condensado * 3

       creme_leite = float(input("Insira o valor do creme de leite: "))
       total_creme = creme_leite * 3

       ferrero = float(input("Insira o valor do Ferrero Rocher: "))
       qntd_ferrero = int(input("Insira quantas unidades tem a embalagem: "))
       total_ferrero = (ferrero / qntd_ferrero) * 2

       amendoim = float(input("Insira o valor do amendoim triturado: "))
       qntd_amendoim = int(input("Quantos gramas tem o pacote: "))
       total_amendoim = (amendoim / qntd_amendoim) * 60

       total_ferrero_rocher = total_condensado + total_creme + total_ferrero + total_amendoim

       custo_por_uni = (total_ferrero_rocher / 1000) * 80
       custo_unidade_reche = custo_por_uni + custo_casquinha

       print(f"O custo por kilo é de: R${total_ferrero_rocher:.2f}")
       print(f"O custo por casquinha banhada e recheada é de: R${custo_unidade_reche:.2f}")


   elif sabor == "5":
       print("Duo, a quantidade de ingredientes será para um KILO de recheio!")

    # Recheio de Ninho
       leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
       total_condensado_ninho = leite_condensado * 3

       creme_leite = float(input("Insira o valor do creme de leite: "))
       total_creme_ninho = creme_leite * 3

       manteiga = float(input("Insira o valor da manteiga: "))
       peso_manteiga = int(input("Insira o peso em gramas: "))
       total_manteiga = (manteiga / peso_manteiga) * 30

       leite_po = float(input("Insira o valor do leite em pó: "))
       peso_leite_po = int(input("Insira quantos gramas tem o pacote: "))
       total_leite_po = (leite_po / peso_leite_po) * 400

       total_ninho = (
        total_condensado_ninho
        + total_creme_ninho
        + total_manteiga
        + total_leite_po )

    # Recheio de Brigadeiro
       leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
       total_condensado_brigadeiro = leite_condensado * 3

       creme_leite = float(input("Insira o valor do creme de leite: "))
       total_creme_brigadeiro = creme_leite * 3

       cacau_po = float(input("Insira o valor do cacau em pó 50%: "))
       qntd_cacau = int(input("Insira quantos gramas tem o pacote: "))
       total_cacau = (cacau_po / qntd_cacau) * 80

       total_brigadeiro = (
        total_condensado_brigadeiro
        + total_creme_brigadeiro
        + total_cacau
    )

    # Custo do recheio Duo
       custo_duo_por_kilo = (total_ninho + total_brigadeiro) / 2

       custo_por_uni = (custo_duo_por_kilo / 1000) * 130
       custo_unidade_reche = custo_por_uni + custo_casquinha

       print(f"Custo do Ninho por receita: R${total_ninho:.2f}")
       print(f"Custo do Brigadeiro por receita: R${total_brigadeiro:.2f}")
       print(f"Custo do recheio Duo por kilo: R${custo_duo_por_kilo:.2f}")
       print(f"Custo por casquinha banhada e recheada: R${custo_unidade_reche:.2f}")

   elif sabor == "6":
        print("Você escolheu Nutella, o valor do custo será informado em KILOS")

        nutella = float(input("Insira o valor do Creme de Avelã: "))
        qntd_nutella = int(input("Insira a quantidade: "))
        total_nutella = (nutella / qntd_nutella) * 60

        custo_unidade_reche = total_nutella + custo_casquinha 

   else:
        print("Digite um Produto Válido") 

elif produto == "5":
     ovo = float(input("Insira o valor da bandeja de ovos com 20: "))
     qntd_ovos = int(input("Insira a quantidade de ovos na bandeja: "))
     total_ovos = (ovo / qntd_ovos) * 3

     acucar = float(input("Insira o valor do kilo do açúcar: "))
     qntd_acucar = int(input("Quantos gramas tem o pacote de açúcar?: "))
     total_acucar = acucar / qntd_acucar

     cacau_po = float(input("Insira o valor do  Cacau em Pó 50%: "))
     qntd_cacau = int(input("Quantos gramas tem o pacote?: "))
     total_cacau = cacau_po / qntd_cacau

     fermento = float(input(" Insira o valor do Fermento"))
     qntd_fermento = int(input("Quantos gramas tem o fermento?: "))
     total_fermento = (fermento / qntd_fermento) * 40

     pote = float(input("Insira o valor dos Potes: "))
     qntd_potes = int(input("Quantidade de potes: "))
     total_potes = pote / qntd_potes

     total_bolo = total_ovos + total_acucar + total_cacau + total_fermento + total_potes

     sabor = input("Qual sabor do Bolo? 1 -Ninho,2 -Brigadeiro,3 -Duo: ")

     if sabor == "1":
        print("Ninho, a quantidade de ingredientes será para um KILO de recheio!")

        leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
        total_condensado = leite_condensado * 3

        creme_leite = float(input("Insira o valor do creme de leite: "))
        total_creme = creme_leite * 3

        manteiga = float(input("Insira o valor da manteiga: "))
        peso_manteiga = int(input("Insira o peso: "))
        total_manteiga = (manteiga / peso_manteiga) * 30

        leite_po = float(input("Insira o valor do leite em pó: "))
        peso_leite_po = int(input("Insira quantos gramas tem o pacote: "))
        total_leite_po = (leite_po / peso_leite_po) * 400

        total_ninho = total_condensado + total_creme + total_leite_po + total_manteiga
        custo_por_uni = (total_ninho / 1000) * 80 
        custo_unidade_reche = custo_por_uni + total_bolo

        print(f"O custo por kilo é de: R${total_ninho}")
        print(f"O custo por casquinha banhada e recheada é de: R${custo_unidade_reche:.2f}")

     elif sabor == "2":
       print("Brigadeiro, a quantidade de ingredientes será para um KILO de recheio!")

       leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
       total_condensado = leite_condensado * 3

       creme_leite = float(input("Insira o valor do creme de leite: "))
       total_creme = creme_leite * 3

       cacau_po = float(input("Insira o valor do Cacau em Pó: "))
       qntd_cacau = int(input("Insira quantos gramas tem o pacote de cacau em pó 50%: "))
       total_cacau = (cacau_po / qntd_cacau) * 80

       total_brigadeiro = total_condensado + total_creme + total_cacau

       custo_por_uni = (total_brigadeiro / 1000) * 80
       custo_unidade_reche = custo_por_uni + total_bolo

       print(f"Custo total do Brigadeiro por kilo: R${total_brigadeiro:.2f}")
       print(f"Custo total do Brigadeiro por unidade banhada e recheada: R${custo_unidade_reche:.2f}")

     elif sabor == "3":
        print("Você escolheu Duo, o valor do custo será informado em KILOS")

        leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
        total_condensado = leite_condensado * 3

        creme_leite = float(input("Insira o valor do creme de leite: "))
        total_creme = creme_leite * 3

        manteiga = float(input("Insira o valor da manteiga: "))
        peso_manteiga = int(input("Insira o peso: "))
        total_manteiga = (manteiga / peso_manteiga) * 30

        leite_po = float(input("Insira o valor do leite em pó: "))
        peso_leite_po = int(input("Insira quantos gramas tem o pacote: "))
        valor_por_grama_leite_po = leite_po / peso_leite_po
        total_leite_po = valor_por_grama_leite_po * 400

        total_ninho = total_condensado + total_creme + total_leite_po
        total_unidade = (total_ninho / 1000) * 40


        leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
        total_condensado = leite_condensado * 3

        creme_leite = float(input("Insira o valor do creme de leite: "))
        total_creme = creme_leite * 3

        cacau_po = float(input("Insira o valor do Cacau em Pó: "))
        qntd_cacau = int(input("Insira quantos gramas tem o pacote de cacau em pó 50%: "))
        valor_por_grama_cacau = cacau_po / qntd_cacau
        total_cacau = valor_por_grama_cacau * 80

        total_brigadeiro = total_condensado + total_creme + total_cacau + custo_casquinha
        custo_por_kilo = (total_brigadeiro / 1000) * 80
        custo_por_unidade = (custo_por_kilo / 80) + total_bolo


        duo = (total_brigadeiro + total_ninho) / 2
        total_duo = duo * 80
     else:
        print("Digite um Produto Válido")

elif produto == "6": #pudim
     
     leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))

     ovo = float(input("Insira o valor da bandeja de ovos: "))
     qntd_ovo = int(input("Quantidade de Ovos: "))
     total_ovos = (ovo / qntd_ovo) * 1

     acucar = float(input("Insira o valor do kilo do açúcar: "))
     qntd_acucar = int(input("Quantos gramas tem o pacote: "))
     total_acucar = (acucar / qntd_acucar) * 190

     leite = float(input("Insira o valor do leite: "))
     total_leite = (leite / 1000) * 395


     pote = float(input("Insira o valor dos Potes: "))
     qntd_pote = int(input("Quantos potes vem na embalagem?: "))
     total_pote = pote / qntd_pote

     total_pudim = total_ovos + total_acucar + total_pote + total_leite  + leite_condensado
     print(total_pudim)

elif produto == "7":
     
     copo = float(input("Insira o valor dos Potes: "))
     copo_qntd = int(input("Insira a quantidade: "))
     total_copo = copo / copo_qntd

     selo = float(input("Insira o valor dos selos: "))
     qntd_selo = int(input("Insira a quantidade: "))
     total_selos = selo / qntd_selo

     total = total_selos + total_copo
     
     sabor = input("Qual sabor do Copo da Felicidade? 1 -Ninho,2 -Brigadeiro,3 -Kinder Bueno,4- Ferrero Rochet,5 -Duo,6 -Nutella: ")

     if sabor == "1":
        print("Ninho, a quantidade de ingredientes será para um KILO de recheio!")

        leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
        total_condensado = leite_condensado * 3

        creme_leite = float(input("Insira o valor do creme de leite: "))
        total_creme = creme_leite * 3

        manteiga = float(input("Insira o valor da manteiga: "))
        peso_manteiga = int(input("Insira o peso: "))
        total_manteiga = (manteiga / peso_manteiga) * 30

        leite_po = float(input("Insira o valor do leite em pó: "))
        peso_leite_po = int(input("Insira quantos gramas tem o pacote: "))
        total_leite_po = (leite_po / peso_leite_po) * 400

        total_ninho = total_condensado + total_creme + total_leite_po + total_manteiga
        custo_por_uni = (total_ninho / 1000) * 80 
        custo_unidade_reche = custo_por_uni + total

        print(f"O custo por kilo é de: R${total_ninho}")
        print(f"O custo por casquinha banhada e recheada é de: R${custo_unidade_reche:.2f}")

     elif sabor == "2":
       print("Brigadeiro, a quantidade de ingredientes será para um KILO de recheio!")

       leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
       total_condensado = leite_condensado * 3

       creme_leite = float(input("Insira o valor do creme de leite: "))
       total_creme = creme_leite * 3

       cacau_po = float(input("Insira o valor do Cacau em Pó: "))
       qntd_cacau = int(input("Insira quantos gramas tem o pacote de cacau em pó 50%: "))
       total_cacau = (cacau_po / qntd_cacau) * 80

       total_brigadeiro = total_condensado + total_creme + total_cacau

       custo_por_uni = (total_brigadeiro / 1000) * 130
       custo_unidade_reche = custo_por_uni + total

       print(f"Custo total do Brigadeiro por kilo: R${total_brigadeiro:.2f}")
       print(f"Custo total do Brigadeiro por unidade banhada e recheada: R${custo_unidade_reche:.2f}")

     elif sabor == "3":
       print("Kinder Bueno, a quantidade de ingredientes será para um KILO de recheio!")

       avela = float(input("Insira o valor da Pasta de Avelã: "))
       peso_avela = int(input("Insira quantos gramas tem o pacote: "))
       total_avela = (avela / peso_avela) * 450

       leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
       total_condensado = leite_condensado * 3

       creme_leite = float(input("Insira o valor do creme de leite: "))
       total_creme = creme_leite * 3

       leite_po = float(input("Insira o valor do leite em pó: "))
       peso_leite_po = int(input("Insira quantos gramas tem o pacote: "))
       total_leite_po = (leite_po / peso_leite_po) * 750

       total_kinder_bueno = total_avela + total_condensado + total_creme + total_leite_po

       custo_por_uni = (total_kinder_bueno / 1000) * 80
       custo_unidade_reche = custo_por_uni + total

       print(f"O custo por kilo é de: R${total_kinder_bueno:.2f}")
       print(f"O custo por casquinha banhada e recheada é de: R${custo_unidade_reche:.2f}")

        
     elif sabor == "4":
        print("Você escolheu Ferrero Rochet, o valor do custo será informado em KILOS")

        leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
        total_condensado = leite_condensado * 3

        creme_leite = float(input("Insira o valor do creme de leite: "))
        total_creme = creme_leite * 3

        ferrero = float(input("Insira o valor do Ferro: "))
        qntd_ferrero = int(input("Insira quantas unidades: "))
        total_ferrero = (ferrero / qntd_ferrero) / 2

        amendoim = float(input("Insira o valor do Amendoim Triturado: "))
        qntd_amendoim = int(input("Quantos Gramas tem o pacote: "))
        total_amendoim = (amendoim / qntd_amendoim) * 60

        custo_ferrero = total + total_condensado + total_creme + total_ferrero + total_amendoim
        print(f"Custo total do Brigadeiro: R${custo_ferrero:.2f}") 

     elif sabor == "5":
       print("Duo, a quantidade de ingredientes será para um KILO de recheio!")

    # Recheio de Ninho
       leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
       total_condensado_ninho = leite_condensado * 3

       creme_leite = float(input("Insira o valor do creme de leite: "))
       total_creme_ninho = creme_leite * 3

       manteiga = float(input("Insira o valor da manteiga: "))
       peso_manteiga = int(input("Insira o peso em gramas: "))
       total_manteiga = (manteiga / peso_manteiga) * 30

       leite_po = float(input("Insira o valor do leite em pó: "))
       peso_leite_po = int(input("Insira quantos gramas tem o pacote: "))
       total_leite_po = (leite_po / peso_leite_po) * 400

       total_ninho = (
        total_condensado_ninho
        + total_creme_ninho
        + total_manteiga
        + total_leite_po )

    # Recheio de Brigadeiro
       leite_condensado = float(input("Insira o valor do leite condensado de 372mls: "))
       total_condensado_brigadeiro = leite_condensado * 3

       creme_leite = float(input("Insira o valor do creme de leite: "))
       total_creme_brigadeiro = creme_leite * 3

       cacau_po = float(input("Insira o valor do cacau em pó 50%: "))
       qntd_cacau = int(input("Insira quantos gramas tem o pacote: "))
       total_cacau = (cacau_po / qntd_cacau) * 80

       total_brigadeiro = (
        total_condensado_brigadeiro
        + total_creme_brigadeiro
        + total_cacau
    )

    # Custo do recheio Duo
       custo_duo_por_kilo = (total_ninho + total_brigadeiro) / 2

       custo_por_uni = (custo_duo_por_kilo / 1000) * 80
       custo_unidade_reche = custo_por_uni + total

       print(f"Custo do Ninho por receita: R${total_ninho:.2f}")
       print(f"Custo do Brigadeiro por receita: R${total_brigadeiro:.2f}")
       print(f"Custo do recheio Duo por kilo: R${custo_duo_por_kilo:.2f}")
       print(f"Custo por casquinha banhada e recheada: R${custo_unidade_reche:.2f}")

     elif sabor == "6":
        print("Você escolheu Nutella, o valor do custo será informado em KILOS")

        nutella = float(input("Insira o valor do Creme de Avelã: "))
        qntd_nutella = int(input("Insira a quantidade: "))
        total_nutella = (nutella / qntd_nutella) * 130

     else:
        print("Digite um Produto Válido")

else:
   print("Digite um Produto Válido")