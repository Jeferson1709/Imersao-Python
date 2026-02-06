#Puxando a biblioteca Pandas.
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

#Lendo a base de dados. 
df.head()

#Informação dos tipos dos dados.
df.info()

#Descrição dos dados.
df.describe()

#Dimensão da base de dados.
df.shape

#Quantidade de linhas e colunas.
linhas, colunas = df.shape[0], df.shape[1]

print("linhas: " , linhas)
print("Colunas: ", colunas)

#Lista os nomes das colunas.
df.columns
#prompt: traduza para mim as colunas do dataframe df para português brasileiro. 
colunas_traduzidas = {
    'work_year': 'ano',
    'experience_level': 'senioridade',
    'employment_type': 'contrato',
    'cargo': 'cargo',
    'salario': 'salario',
    'moeda_salario': 'moeda',
    'salario_em_usd': 'usd',
    'residencia_funcionario': 'residencia',
    'remote_ratio': 'remoto',
    'localizacao_empresa': 'empresa',
    'company_size': 'tamanho_empresa'
}

df = df.rename(columns=colunas_traduzidas)
print("Novas colunas do DataFrame:")
print(df.columns)

#Contando a frequência de cada nívelx de experiência:
df['senioridade'].value_counts()

#Contando a frequência de cada tipo de emprego:
df['contrato'].value_counts()


#Contando a frequência de cada tipo de trabalho:
df['remoto'].value_counts()

#Contando a frequência de tamanho da empresa: 
df['tamanho_empresa'].value_counts()

#prompt: traduza para português as categorias da coluna "senioridade" do dataframe df
df['senioridade'] = df['senioridade'].replace({
    'SE': 'Senior',
    'MI': 'Pleno',
    'EN': 'Junior',
    'EX': 'Executivo'
})

print("Novas categorias da coluna 'senioridade':")
df['senioridade'].value_counts()

#prompt: traduza para português as categorias da coluna "contrato" do dataframe df
df['contrato'] = df['contrato'].replace({
    'FT': 'Tempo Integral',
    'CT': 'Contrato',
    'PT': 'Meio Período',
    'FL': 'Freelancer'
})

print("Novas categorias da coluna 'contrato':")
df['contrato'].value_counts()

#prompt: traduza para português as categorias da coluna "tamanho_empresa" do dataframe df
df['tamanho_empresa'] = df['tamanho_empresa'].replace({
    'M': 'Médio',
    'L': 'Grande',
    'S': 'Pequeno'
})

print("Novas categorias da coluna 'tamanho_empresa':")
df['tamanho_empresa'].value_counts()

# prompt: traduza para português as categorias da coluna "remoto" do dataframe df
df['remoto'] = df['remoto'].replace({
    0: 'Presencial',
    50: 'Híbrido',
    100: 'Remoto Total'
})

print("Novas categorias da coluna 'remoto':")
df['remoto'].value_counts()

df.head()

df.describe(include=['object' , 'string'])

df.describe()

# Soma dos valaores nulos.
#df.isnull.sum()

#Valores únicos nesse campo.
df['ano'].unique()

#Ver todos todo os nulos da base.
df[df.isnull().any(axis =1)]

# Manipulação de valores.
import numpy as np
#Criando um Dataframe de para usar de exemplo. 
df_salarios = pd.DataFrame({
    'nome ': ["Ana", "Bruno", "Carlos", "Daniele", "Val"],
    'salario': [4000, np.nan , 5000, np.nan, 100000]
})

#Calcula a média salarial e substitui os nulos pela média e arrendonda os valores 
df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))

'''Calcula mediana e substitui os nulos pela mediana '''

df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median().round(2))

df_salarios

df_temperatura  = pd.DataFrame({
    "Dia" : ["Segunda", "Terça", "Quarta" , "Quinta", "Sexta"],
    "Temperatura" : [30 , np.nan , np.nan , 20 , 27]
})

df_temperatura["preenchido_fill"]= df_temperatura["Temperatura"].ffill()
df_temperatura

df_temperatura  = pd.DataFrame({
    "Dia" : ["Segunda", "Terça", "Quarta" , "Quinta", "Sexta"],
    "Temperatura" : [30 , np.nan , np.nan , 20 , 27]
})

df_temperatura["preenchido_fill"]= df_temperatura["Temperatura"].bfill()
df_temperatura

df_cidades = pd.DataFrame({
    'nome' : ["Ana" , "Bruno" , "Carlos", "Daniele", "Val"],
    "cidade" : ["São Paulo", np.nan, "Curitiba" , np.nan, "Belém"]
    
})

df_cidades ["cidade_preenchida"] = df_cidades["cidade"].fillna("Não encontrado")
df_cidades

df_limpo= df.dropna()
df_limpo.isnull().sum()

df_limpo.info()

df_limpo.assign(ano = df_limpo["ano"].astype('int64'))