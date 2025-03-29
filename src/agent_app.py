import requests
import json

SERVER_URL = "http://127.0.0.1:8000" 


tipos_combustivel = ['Gasolina', 'Etanol', 'Flex', 'Diesel', 'Elétrico', 'Híbrido']
cores = ['Preto', 'Branco', 'Prata', 'Cinza', 'Vermelho', 'Azul', 'Verde', 'Marrom', 'Amarelo']
transmissoes = ['Manual', 'Automática', 'CVT', 'Automatizada']

def coletar_criterios():
    """Coleta os critérios de busca do usuário, incluindo os novos filtros."""
    print("\nAgente: Entendido! Para te ajudar a encontrar o veículo ideal, preciso de alguns detalhes.")

    criterios = {} 
    marca = input("Agente: Qual marca você prefere (ou deixe em branco para qualquer uma)? ")
    if marca:
        criterios['marca'] = marca

    modelo = input("Agente: Algum modelo específico (ou deixe em branco)? ")
    if modelo:
        criterios['modelo'] = modelo

    try:
        ano_min = input("Agente: Prefere carros a partir de que ano (ex: 2018)? (ou deixe em branco) ")
        if ano_min:
            criterios['ano_min'] = int(ano_min)
    except ValueError:
        print("Agente: Ano mínimo inválido, ignorando este filtro.")

    try:
        ano_max = input("Agente: E até que ano (ex: 2022)? (ou deixe em branco) ")
        if ano_max:
            criterios['ano_max'] = int(ano_max)
    except ValueError:
        print("Agente: Ano máximo inválido, ignorando este filtro.")

    cor = input(f"Agente: Alguma preferência de cor ({', '.join(cores[:5])}...)? (ou deixe em branco) ")
    if cor:
        criterios['cor'] = cor

    try:
        preco_min = input("Agente: Gostaria de um preço MÍNIMO (ex: 30000)? (ou deixe em branco) ")
        if preco_min:
            criterios['preco_min'] = float(preco_min)
    except ValueError:
        print("Agente: Preço mínimo inválido, ignorando este filtro.")

    try:
        preco_max = input("Agente: E qual o valor MÁXIMO que você gostaria de pagar (ex: 75000)? (ou deixe em branco) ")
        if preco_max:
            criterios['preco_max'] = float(preco_max)
    except ValueError:
        print("Agente: Preço máximo inválido, ignorando este filtro.")

    combustivel = input(f"Agente: Prefere algum tipo de combustível ({', '.join(tipos_combustivel)})? (ou deixe em branco) ")
    if combustivel:
        
        criterios['combustivel'] = combustivel

    try:
        km_max = input("Agente: Qual a quilometragem máxima desejada (ex: 50000)? (ou deixe em branco) ")
        if km_max:
            criterios['km_max'] = int(km_max)
    except ValueError:
        print("Agente: Quilometragem máxima inválida, ignorando este filtro.")

    try:
        portas = input("Agente: Quantas portas (2 ou 4)? (ou deixe em branco) ")
        if portas:
            num_portas = int(portas)
            if num_portas in [2, 4]:
                criterios['portas'] = num_portas
            else:
                print("Agente: Número de portas inválido (deve ser 2 ou 4), ignorando este filtro.")
    except ValueError:
        print("Agente: Número de portas inválido, ignorando este filtro.")

    transmissao = input(f"Agente: Prefere alguma transmissão ({', '.join(transmissoes)})? (ou deixe em branco) ")
    if transmissao:
          criterios['transmissao'] = transmissao 
    crit_informados = {k: v for k, v in criterios.items() if v is not None}
    print(f"\nAgente: Ok, vou buscar por veículos com os seguintes critérios: {crit_informados}")
    return criterios

def buscar_veiculos_na_api(criterios):
    """Envia os critérios para a API e retorna os resultados."""
    try:
        search_url = f"{SERVER_URL}/search/"
        payload = {k: v for k, v in criterios.items() if v is not None}
        response = requests.post(search_url, json=payload)
        response.raise_for_status()
        resultados = response.json()
        return resultados

    except requests.exceptions.RequestException as e:
        print(f"\nAgente: Desculpe, tive um problema para me conectar ao sistema de busca: {e}")
        return None
    except json.JSONDecodeError:
        print("\nAgente: Desculpe, a resposta do sistema de busca não foi compreensível.")
        return None

def exibir_resultados(veiculos):
    if not veiculos:
        print("\nAgente: Poxa, não encontrei veículos com os critérios que você especificou.")
        return

    print(f"\nAgente: Ótimo! Encontrei {len(veiculos)} veículo(s) que podem te interessar:")
    print("-" * 40)
    for v in veiculos:
        preco_formatado = f"R$ {v.get('preco', 0):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        km_formatado = f"{v.get('quilometragem', 'N/I'):,}".replace(",", ".") if isinstance(v.get('quilometragem'), int) else 'N/I'

        print(f"  Marca: {v.get('marca', 'N/I')}")
        print(f"  Modelo: {v.get('modelo', 'N/I')}")
        print(f"  Ano: {v.get('ano_modelo', 'N/I')} (Fab: {v.get('ano_fabricacao', 'N/I')})")
        print(f"  Cor: {v.get('cor', 'N/I')}")
        print(f"  KM: {km_formatado}")
        print(f"  Combustível: {v.get('combustivel', 'N/I')}") 
        print(f"  Portas: {v.get('numero_portas', 'N/I')}") 
        print(f"  Transmissão: {v.get('transmissao', 'N/I')}") 
        print(f"  Preço: {preco_formatado}")
        print("-" * 40)

def iniciar_conversa():
    print("Agente: Olá! Sou seu assistente virtual de busca de veículos.")
    print("Agente: Você pode me pedir para 'buscar' um veículo ou digitar 'sair' para encerrar.")

    while True:
        acao_usuario = input("\nAgente: Como posso te ajudar agora? (buscar / sair) ").lower()

        if "sair" in acao_usuario or "encerrar" in acao_usuario or "nada" in acao_usuario or "nao" in acao_usuario:
            print("Agente: Entendido! Foi um prazer ajudar. Até logo!")
            break

        elif "buscar" in acao_usuario or "procurar" in acao_usuario or "veiculo" in acao_usuario or "carro" in acao_usuario:
            criterios_busca = coletar_criterios()

            print("\nAgente: Buscando no nosso inventário...")
            resultados_api = buscar_veiculos_na_api(criterios_busca)
            
            if resultados_api is not None:
                exibir_resultados(resultados_api)
            

        else:
            print("Agente: Desculpe, não entendi. Você pode pedir para 'buscar' ou 'sair'.")

if __name__ == "__main__":
    iniciar_conversa()