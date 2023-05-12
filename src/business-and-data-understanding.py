# %%
import pandas as pd
import numpy as np
# %%
df = pd.read_csv('../data/netflix_titles.csv')
df.head()
# %%
print(f'{df.shape[0]} Linhas')
print(f'{df.shape[1]} Colunas')
# %%
df.info()
# %%
df.describe()
# %%
# Verificando dados nulos
df.isnull().sum()/df.shape[0]*100
# %%
# Verificando se existe algum dados em branco com string vazia
df[df['country'] == '']
# %%
# Preparação dos dados
# Seleção de dados
# Verificando se existe dados duplicados
df[df.duplicated()]
# %%
# Verificando se existe dados duplicados apatir da variável show_id
df[df.duplicated( subset='show_id')]
# %%
# Verificando se existe dados duplicados apatir da variável title e director
df[df.duplicated(subset=['title','director'])]
# %%
# Verificando a quantidade de show_id único
print(df['show_id'].nunique())
# %%
print(df['show_id'].info())
# %%
# Verificando a quantidade de dados únicos
df['type'].nunique()
# %%
# Verificando os tipos de variável na coluna
df['type'].info()
# %%
# Quantidade de tipo de variável
df['type'].unique()
# %%
# Contando quantas variáveis únicas existem
df['type'].value_counts()
# %%
df['type'].value_counts(normalize=True)
# %%
# Indentificando quais titulos estão duplicados
df[df.duplicated('title')]['title'].unique()
# %%
# Transformando a coluna director
# transformando valores string de uma coluna para lista usando split()
df['director'] = df['director'].str.split(',')
# %%
# Usando o metodo explode para duplicar a linha para cada diretor a mais
df = df.explode('director')
# %%
# Corrigindo o espaço em branco causado pelo método explode acima
df['director'] = df['director'].str.strip()
# %%
# Resetando o indice que foi duplicado no processo de explode
df.reset_index(inplace=True, drop=False)
# %%
# Recetindo o procedimento para as colunas director, cast, country e listed_in
# Fazendo split para as colunas
df['cast'] = df['cast'].str.split(',')
df['country'] = df['country'].str.split(',') 
df['listed_in'] = df['listed_in'].str.split(',')
# %%
# Explode para coluna cast
df = df.explode('cast', ignore_index=True)
df['cast'] = df['cast'].str.strip()
# %%
df['cast'].unique()
# %%
df.head()
# %%
df = df.explode('country', ignore_index=True)
df['country'] = df['country'].str.strip()
# %%
df['country'].unique()
# %%
df[df['country'] == '']
# %%
# Removendo o valores em branco encontrado acima
shape_before = df.shape[0]
df.drop(df[df['country'] == ''].index, inplace=True)
print(f'{shape_before-df.shape[0]} dados foram removidos')
# %%
df.head()
# %%
df = df.explode('listed_in', ignore_index=True)
df['listed_in'] = df['listed_in'].str.strip()
# %%
# Dados únicos para variável director
df['director'].unique()
# %%
# Dados unicos para variável listed_in
df['listed_in'].unique()
# %%
# Verificando se existe alguma linha com caracter em branco
df[df['director'].str.len()==0]
# %%
# Verificando se existe alguma linha com caracter em branco
df[df['listed_in'].str.len()==0]
# %%
shape_before = df.shape[0]
df.drop_duplicates(inplace=True)
print(f'{shape_before-df.shape[0]} dados foram removidos')
# %%
# Pegando datas aleatórias para entendimento do problema
index = df.sample(10).index
df.loc[index, 'date_added']
# %%
df['date_added'] = pd.to_datetime(df['date_added'], format='mixed')
# %%
df['release_year'].info()
# %%
df['release_year'].unique()
# %%
df['duration'].info()
# %%
df['duration'].unique()
# %%
df[df['type']=='TV Show']['duration'].unique()
# %%
filter_filmes = df['type']=='Movie'
# %%
# Removendo o min string da coluna duration
df[filter_filmes]['duration'].str.replace('min','').str.strip().astype(int)
# %%
# Criando nova coluna para duration. Tempo do filme
df['duration_movie'] = np.NaN
df
# %%
filmes_index = df[filter_filmes].index
# %%
df.loc[filmes_index, 'duration_movie'] = df.loc[filmes_index]['duration'].str.replace('min','').str.strip()
# %%
# Checando valores nulos
df[df['duration_movie'].isna()]['type'].value_counts()
# %%
df['duration_movie'].info()
# %%
# Transformando a coluna duration_movie em int
df['duration_movie'] = df['duration_movie'].astype('Int64')
# %%
df['duration_movie'].info()
# %%
# tratando a series
filter_series = df['type']=='TV Show'
# %%
df[filter_series]['duration'].unique()
# %%
# Replace usando Dicionário
# dic = {'Seasons':'','Season':''}
# df['qtd_temporada'] = df[filter_series]['duration'].replace(dic, regex=True)
df['qtd_temporada'] = df[filter_series]['duration'].replace(to_replace=['Seasons','Season'],
                                                            value=['',''],
                                                            regex=True)
# %%
df[df['qtd_temporada'].isna()==False]['type'].value_counts()
# %%
df['qtd_temporada'].info()
# %%
df['qtd_temporada'].fillna(0, inplace=True)
df['qtd_temporada'] = df['qtd_temporada'].astype('int64')
# %%
del df['duration']
# %%
df.info()
# %%
# Trabalhando somente com filmes
df_filmes = pd.DataFrame(df[filter_filmes])
df_filmes
# %%
# deletando colunas que náo vamos usar
df_filmes.drop(['qtd_temporada', 'type'], axis=1, inplace=True)
# %%
df_filmes.reset_index(inplace=True, drop=True)
# %%
# Verificando a existencia de nulos
df_filmes.isna().sum()/df_filmes.shape[0]*100
# %%
shape_before = df_filmes.shape[0]
df_filmes.drop(df_filmes[df_filmes['director'].isna()].index, inplace=True)
print(f'{shape_before-df_filmes.shape[0]} dados foram removidos')
# %%
df_filmes.isna().sum()/df_filmes.shape[0]*100
# %%
shape_before = df_filmes.shape[0]
df_filmes.drop(df_filmes[df_filmes['cast'].isna()].index, inplace=True)
print(f'{shape_before-df_filmes.shape[0]} dados foram removidos')
# %%
df_filmes.isna().sum()/df_filmes.shape[0]*100
# %%
shape_before = df_filmes.shape[0]
df_filmes.drop(df_filmes[df_filmes['country'].isna()].index, inplace=True)
print(f'{shape_before-df_filmes.shape[0]} dados foram removidos')
# %%
df_filmes.isna().sum()/df_filmes.shape[0]*100
# %%
shape_before = df_filmes.shape[0]
df_filmes.drop(df_filmes[df_filmes['rating'].isna()].index, inplace=True)
print(f'{shape_before-df_filmes.shape[0]} dados foram removidos')
# %%
df_filmes.isna().sum()/df_filmes.shape[0]*100
# %%
df_filmes.head()
# %%
# Criando uma classificação para a coluna duration move
df_filmes['duration_movie'].describe()
# %%
df_filmes['duration'] = pd.cut(df_filmes['duration_movie'],
                                            bins=3,
                                            labels=['baixa','média','alta'])
# %%
df_filmes.sample(10)
# %%
df_filmes.sort_values(['date_added','show_id','director','cast','country','listed_in'], inplace=True)
# %%
df_filmes.to_csv('../data/netflix_filmes_clear.csv', index=False)
# %%
# Tratando dados para Series
df_series = pd.DataFrame(df[filter_series])
df_series.isna().sum()/df_series.shape[0]*100
# %%
df_series.drop(['director', 'duration_movie'], axis=1, inplace=True)
# %%
df_series.isna().sum()/df_series.shape[0]*100
# %%
df_series.dropna(subset=['cast','date_added','rating'], inplace=True)
# %%
df_series.isna().sum()/df_series.shape[0]*100
# %%
df_series.info()
# %%
df_series.sort_values(['date_added','show_id','cast','country','listed_in'], inplace=True)
df_series.to_csv('../data/netflix_series_clear.csv', index=True)
# %%
