import mysql.connector
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()

hora = 10 #valor da mão de obra
energia_hora = 0.10 #valor gasto em energia/hora
vida_util = 1 #valor gasto de depreciação da impressora/hora
valor_embalagem = 5 #valor aproximado gasto em embalagens
margem_falha = 0.10 #10% do custo para cobrir possíveis reimpressões
comissao_market = 0.14 #14% de comissão do anúncio em marketplace, partindo do valor maior

def conectar():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
    )
def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
        create table if not exists produtos (
            id int auto_increment primary key,
            nome varchar(30) not null,
            valor_filamento decimal(10,2) not null,
            peso decimal(10,2) not null,
            tempo decimal(10,2) not null,
            tempo_prod decimal(10,2) not null,
            margem decimal(10,2) not null,
            custo_tot decimal(10,2) not null,
            valor_final decimal(10,2) not null,
            valor_com_comissao decimal(10,2) not null,
            lucro decimal(10,2) not null,
            criado_em timestamp default current_timestamp
        )
    ''')
    conexao.commit()
    cursor.close()
    conexao.close()

def salvar_produto(nome, valor_filamento, peso, tempo, tempo_prod, margem, custo_tot, valor_final, valor_com_comissao, lucro):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
        insert into produtos (nome, valor_filamento, peso, tempo, tempo_prod, margem, custo_tot, valor_final, valor_com_comissao, lucro)
        values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ''', (nome, valor_filamento, peso, tempo, tempo_prod, margem, custo_tot, valor_final, valor_com_comissao, lucro))
    conexao.commit()
    cursor.close()
    conexao.close()

def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('select id, nome, valor_final, criado_em from produtos order by criado_em desc')
    produtos = cursor.fetchall()
    cursor.close()
    conexao.close()
    return produtos

def carregar_produto(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('select * from produtos where id = %s', (id,))
    produto = cursor.fetchone()
    cursor.close()
    conexao.close()
    return produto

def excluir_produto(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('delete from produtos where id = %s', (id,))
    conexao.commit()
    cursor.close()
    conexao.close()