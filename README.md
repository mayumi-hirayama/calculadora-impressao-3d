# 🖨️ Calculadora de Custo de Impressão 3D

Calculadora para precificação de produtos impressos em 3D, com armazenamento em banco de dados MySQL. Desenvolvida em Python, permite calcular o custo total de um produto considerando filamento, energia, mão de obra, desgaste, embalagem, margem de reimpressão e comissão de marketplace.

---

## ✅ Funcionalidades

- Cálculo detalhado de custo por produto
- Margem de falha/reimpressão automática (10% sobre o custo total)
- Cálculo de comissão de marketplace (14% sobre o preço final — Shopee/Mercado Livre)
- Sugestão de preço final para anúncio já com comissão embutida
- Sugestão de preço final com margem de lucro
- Salvar produtos no banco de dados para consultas futuras
- Carregar produtos salvos sem precisar redigitar os dados
- Excluir produtos salvos
- Menu interativo no terminal

---

## 🧮 O que é calculado

| Item                  | Descrição                                                       |
| --------------------- | --------------------------------------------------------------- |
| Filamento             | Custo com base no peso usado e preço por kg                     |
| Energia               | Custo por hora de impressão                                     |
| Mão de obra           | Custo por hora de processamento do produto                      |
| Desgaste              | Depreciação da impressora por hora de uso                       |
| Embalagem             | Custo fixo por produto                                          |
| Margem de falha       | 10% sobre o custo total para cobrir eventuais reimpressões      |
| Comissão marketplace  | 14% sobre o preço final (média Shopee/Mercado Livre)            |

---

## 🚀 Como usar

### 1. Clone o repositório

```
git clone https://github.com/mayumi-hirayama/calculadora-impressao-3d.git
cd calculadora-impressao-3d
```

### 2. Instale as dependências

```
pip install mysql-connector-python
```

### 3. Configure o banco de dados

No MySQL, execute:

```
CREATE DATABASE calculadora_custo;
```

> A tabela `produtos` é criada automaticamente ao rodar o programa.

### 4. Configure a conexão

No arquivo `calculadora_custo.py`, edite a função `conectar()` com suas credenciais:

```python
def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='seu_usuario',
        password='sua_senha',
        database='calculadora_custo'
    )
```

### 5. Execute

```
python calculadora_custo.py
```

---

## 📋 Requisitos

- Python 3.x
- MySQL
- mysql-connector-python

---

## 🛠️ Tecnologias utilizadas

- Python
- MySQL
- mysql-connector-python
