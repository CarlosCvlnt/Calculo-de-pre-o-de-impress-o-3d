def calcular_preco_impressao3d(peso_gramas, custo_material_por_grama, tempo_horas, custo_maquina_por_hora, margem_lucro=0.2):
    
    custo_material = peso_gramas * custo_material_por_grama
    custo_maquina = tempo_horas * custo_maquina_por_hora
    custo_total = custo_material + custo_maquina

    preco_final = custo_total * (1 + margem_lucro)
    return round(preco_final, 2)



custo_material_por_grama = 0.10   # R$ por grama
custo_maquina_por_hora = 8.00     # R$ por hora
margem_lucro = 0.65              # 25% de lucro

while True:
    peso = float(input("Digite o peso da peça em gramas: "))
    tempo = float(input("Digite o tempo de impressão em horas: "))

    preco = calcular_preco_impressao3d(peso, custo_material_por_grama, tempo, custo_maquina_por_hora, margem_lucro)

    print(f"Preço da impressão 3D: R$ {preco}")

    repetir = input("Deseja calcular outro preço?(s/n): ").strip().lower()
    if repetir != 's':
        break
