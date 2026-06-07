from flask import Flask, render_template, request, redirect, url_for
from calculadora_custo import (
    criar_tabela,
    salvar_produto,
    listar_produtos,
    carregar_produto,
    excluir_produto
)

app = Flask(__name__)

hora = 10
energia_hora = 0.10
vida_util = 1
valor_embalagem = 5
margem_falha = 0.10
comissao_market = 0.14

criar_tabela()

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    produtos = listar_produtos()

    if request.method == 'POST':
        valor_filamento = float(request.form['valor_filamento'])
        peso = float(request.form['peso'])
        tempo = float(request.form['tempo'])
        tempo_prod = float(request.form['tempo_prod']) / 60
        margem = float(request.form['margem'])

        margem_lucro = margem / 100
        peso_kg = peso / 1000
        custo_filam = valor_filamento * peso_kg
        custo_energia = tempo * energia_hora
        custo_mobra = tempo_prod * hora
        desgaste = vida_util * tempo

        custo_tot = custo_filam + custo_energia + custo_mobra + desgaste + valor_embalagem
        custo_ajustado = custo_tot * (1 + margem_falha)
        valor_final = custo_ajustado * (1 + margem_lucro)
        valor_com_comissao = valor_final * (1 + comissao_market)
        lucro = valor_final - custo_ajustado

        resultado = {
            'custo_filam': custo_filam,
            'custo_energia': custo_energia,
            'custo_mobra': custo_mobra,
            'desgaste': desgaste,
            'custo_ajustado': custo_ajustado,
            'comissao': valor_com_comissao - valor_final,
            'valor_com_comissao': valor_com_comissao,
            'lucro': lucro,
            'valor_filamento': valor_filamento,
            'peso': peso,
            'tempo': tempo,
            'tempo_prod': tempo_prod,
            'margem': margem,
            'valor_final': valor_final
        }

    return render_template('index.html', resultado=resultado, produtos=produtos)

@app.route('/salvar', methods=['POST'])
def salvar():
    nome = request.form['nome']
    salvar_produto(
        nome,
        float(request.form['valor_filamento']),
        float(request.form['peso']),
        float(request.form['tempo']),
        float(request.form['tempo_prod']),
        float(request.form['margem']),
        float(request.form['custo_tot']),
        float(request.form['valor_final']),
        float(request.form['valor_com_comissao']),
        float(request.form['lucro'])
    )
    return redirect(url_for('index'))

@app.route('/excluir/<int:id>')
def excluir(id):
    excluir_produto(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)