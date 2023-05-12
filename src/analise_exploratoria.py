# %%
import pandas as pd
# %%
filename = '../data/netflix_filmes_clear.csv'
df = pd.read_csv(filename, parse_dates=['date_added'])
# %%
df.head()
# %%
# Verificando os dados
df.info()
# %%
df.isna().sum()
# %%
df[df.duplicated()]
# %%
# Gerando relatório de análise descritiva
from pandas_profiling import ProfileReport
import matplotlib.pyplot as plt
# %%
report = ProfileReport(df, title='Pandas Profile Report')
report.to_file('../report/relatorio-filmes-01.html')
# %%
import sweetviz as sv
# %%
report2 = sv.analyze(df)
# %%
report2.show_html(filepath='../report/relatorio-filmes-02.html')
# %%
#importing Autoviz class
from bokeh.models.annotations import Box
from autoviz.AutoViz_Class import AutoViz_Class
AV = AutoViz_Class()
# %%
AV = AutoViz(filename='',
            sep='',
            dfte=df,
            chart_format='html')
# %%%
# Analisando dados
df['country'].value_counts()
# %%
df['country'].value_counts(normalize=True)
# %%
df['listed_in'].value_counts(normalize=True)
# %%
df.groupby('release_year')
# %%
df.groupby('release_year').count()
# %%
df.groupby('release_year').mean()
# %%
df.agg({'duration_movie':'median'})
# %%
df.agg({'duration_movie':['mean','max','min']})
# %%
df.describe()
# %%
# Agrupando e agregando dados
df.groupby('director').agg(count=('show_id','count'),
                            nunique=('show_id','nunique')).sort_values('nunique', ascending=False)
# %%
df.groupby(['listed_in']).agg(nunique=('show_id','nunique')).sort_values('nunique', ascending=False)
# %%
df.groupby(['release_year','listed_in']).agg(nunique=('show_id','nunique')).sort_values('nunique', ascending=False)
# %%
# Correlação de Spearman
df[['release_year','duration_movie']].corr(method='spearman')
# %%
df[['release_year','duration_movie']].corr()
# %%
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline 
# %%
# Visualização de Dados
df.hist(figsize=(20,20))
plt.show()
# %%
n_bins = 20
fig, ax = plt.subplots(1,2, figsize=(20,5), tight_layout=True)
ax[0].hist(df['duration_movie'], bins=n_bins)
ax[1].hist(df['release_year'], bins=n_bins)
# %%
f, ax = plt.subplots(figsize=(5,5))
sns.heatmap(df.corr(), annot=True, linewidths=.5, fmt= '.1f', ax=ax)
# %%
plt.subplots(figsize=(20,5))
ax = sns.countplot(x=df['date_added'].dt.month_name(),
                   order=df['date_added'].dt.month_name().value_counts().index)
plt.xticks(rotation=90)
# %%
plt.subplots(figsize=(20,5))
ax = sns.countplot(x=df['date_added'].dt.day_name(),
                   order=df['date_added'].dt.day_name().value_counts().index)
plt.xticks(rotation=90)
# %%
plt.subplots(figsize=(20,5))
ax = sns.countplot(x=df['date_added'].dt.year,
                   order=df['date_added'].dt.year.value_counts().index)
plt.xticks(rotation=90)
# %%
plt.subplots(figsize=(20,5))
ax = sns.countplot(x=df['rating'],
                   order=df['rating'].value_counts().index)
plt.xticks(rotation=90)
# %%
plt.subplots(figsize=(20,5))
ax = sns.countplot(x=df['director'],
                   order=df['director'].value_counts().iloc[:10].index)
ax.bar_label(container=ax.containers[0], labels=df['director'].value_counts(ascending=False).iloc[:10].values)
plt.xticks(rotation=90)
# %%
# Usando catplot()
sns.catplot(data=df, x="duration", kind='count')
# %%
sns.displot(data=df, x="release_year")
# %%
sns.pairplot(df)
# %%
g = sns.JointGrid(x=f'release_year', y='duration_movie', data=df)
g = g.plot(sns.regplot, sns.distplot)
# %%
