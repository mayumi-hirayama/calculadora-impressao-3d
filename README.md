# 🖨️ Calculadora de Custo de Impressão 3D

Calculadora para precificação de produtos impressos em 3D, com armazenamento em banco de dados MySQL. Desenvolvida em Python, permite calcular o custo total de um produto considerando filamento, energia, mão de obra, desgaste e embalagem.

---

## ✅ Funcionalidades

- Cálculo detalhado de custo por produto
- Sugestão de preço final com margem de lucro
- Salvar produtos no banco de dados para consultas futuras
- Carregar produtos salvos sem precisar redigitar os dados
- Excluir produtos salvos
- Menu interativo no terminal

---

## 🧮 O que é calculado

| Item | Descrição |
|---|---|
| Filamento | Custo com base no peso usado e preço por kg |
| Energia | Custo por hora de impressão |
| Mão de obra | Custo por hora de processamento do produto |
| Desgaste | Depreciação da impressora por hora de uso |
| Embalagem | Custo fixo por produto |

---

## 🚀 Como usar

### 1. Clone o repositório
```bash
git clone https://github.com/mayumi-hirayama/calculadora-impressao-3d.git
cd calculadora-impressao-3d
```

### 2. Instale as dependências
```bash
pip install mysql-connector-python
```

### 3. Configure o banco de dados
No MySQL, execute:
```sql
CREATE DATABASE calculadora_custo;
```
> A tabela `produtos` é criada automaticamente ao rodar o programa.

### 4. Configure a conexão
No arquivo `calculadora.py`, edite a função `conectar()` com suas credenciais:
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
```bash
python calculadora.py
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
