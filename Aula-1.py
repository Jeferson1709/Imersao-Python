# Puxando a biblioteca Pandas.
import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv"
)

# Lendo a base de dados.
df.head()

# Informação dos tipos dos dados.
df.info()

# Descrição dos dados.
df.describe()

# Dimensão da base de dados.
df.shape

# Quantidade de linhas e colunas.
linhas, colunas = df.shape[0], df.shape[1]

print("linhas: ", linhas)
print("Colunas: ", colunas)

# Lista os nomes das colunas.
df.columns
# prompt: traduza para mim as colunas do dataframe df para português brasileiro.
colunas_traduzidas = {
    "work_year": "ano",
    "experience_level": "senioridade",
    "employment_type": "contrato",
    "job_title": "cargo",
    "salary": "salario",
    "moeda_salario": "moeda",
    "salary_currency": "usd",
    "salary_in_usd": "residencia",
    "remote_ratio": "remoto",
    "company_location": "empresa",
    "employee_residence": "residencia_funcionario",
    "company_size": "tamanho_empresa",
}

df = df.rename(columns=colunas_traduzidas)
print("Novas colunas do DataFrame:")
print(df.columns)

# Contando a frequência de cada nívelx de experiência:
df["senioridade"].value_counts()

# Contando a frequência de cada tipo de emprego:
df["cargo"].value_counts()


# Contando a frequência de cada tipo de trabalho:
df["remoto"].value_counts()

# Contando a frequência de tamanho da empresa:
df["tamanho_empresa"].value_counts()

# prompt: traduza para português as categorias da coluna "senioridade" do dataframe df
df["senioridade"] = df["senioridade"].replace(
    {"SE": "Senior", "MI": "Pleno", "EN": "Junior", "EX": "Executivo"}
)

print("Novas categorias da coluna 'senioridade':")
df["senioridade"].value_counts()

# prompt: traduza para português as categorias da coluna "contrato" do dataframe df
df["contrato"] = df["contrato"].replace(
    {"FT": "Tempo Integral", "CT": "Contrato", "PT": "Meio Período", "FL": "Freelancer"}
)

print("Novas categorias da coluna 'contrato':")
df["contrato"].value_counts()

# prompt: traduza para português as categorias da coluna "tamanho_empresa" do dataframe df
df["tamanho_empresa"] = df["tamanho_empresa"].replace(
    {"M": "Médio", "L": "Grande", "S": "Pequeno"}
)

print("Novas categorias da coluna 'tamanho_empresa':")
df["tamanho_empresa"].value_counts()

# prompt: traduza para português as categorias da coluna "remoto" do dataframe df
df["remoto"] = df["remoto"].replace(
    {0: "Presencial", 50: "Híbrido", 100: "Remoto Total"}
)

print("Novas categorias da coluna 'remoto':")
df["remoto"].value_counts()

df.head()

df.describe(include="object")

df.describe()
