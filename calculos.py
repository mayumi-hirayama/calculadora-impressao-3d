def calcular_custo(valor_filamento, peso, tempo, tempo_prod, margem):
    hora = 10
    energia_hora = 0.10
    vida_util = 1
    valor_embalagem = 5
    margem_falha = 0.10
    comissao_market = 0.14

    margem_lucro = margem / 100
    peso_kg = peso / 1000
    custo_filam = valor_filamento * peso_kg
    custo_energia = tempo * energia_hora
    custo_mobra = tempo_prod * hora
    desgaste = vida_util * tempo

    custo_tot = custo_filam + custo_energia + custo_mobra + desgaste + valor_embalagem
    custo_ajustado = custo_tot * (1 + margem_falha)
    valor_final = (custo_ajustado * (1 + margem_lucro))
    valor_com_comissao = valor_final * (1 + comissao_market)
    lucro = valor_final - custo_ajustado

    return {
        'custo_filam': custo_filam,
        'custo_energia': custo_energia,
        'custo_mobra': custo_mobra,
        'desgaste': desgaste,
        'custo_ajustado': custo_ajustado,
        'valor_final': valor_final,
        'valor_com_comissao': valor_com_comissao,
        'lucro': lucro,
    }