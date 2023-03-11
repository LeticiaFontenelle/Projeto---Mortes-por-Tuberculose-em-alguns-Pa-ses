#!/usr/bin/env python
# coding: utf-8

# # Mortes por Tuberculose
# 
# Letícia Fontenelle, 10 de Março.  
# 
# 
# Dentro dos Objetivos de Desenvolvimento do Milênio para redução da pobreza e as doenças, diminuição da desigualdade de gênero e a sustentabilidade ambiental entre outros. 
# 
# A tuberculose (TB) em comparação com outras epidemias, às vezes, é pouco comentada, porém seu nível de mortalidade é bem expressivo. 
# 
# Para obter mais informações, consulte a página da Organização Mundial da Saúde (OMS) <http://www.who.int/gho/tb/en/>.
# 
# Conforme a amostra populacional e o número de mortes por tuberculose em alguns países durante um ano, as seguintes mensurações forma extraídas:
# 
# - Quantitativo em número total, máximo, mínimo e médio de mortes para esse ano.
# - Dentre os países elencados, os países com mais ou menos mortes.
# - Taxa de mortalidade para cada país.                                                                                        - - - Países com taxa de mortalidade mais baixa e mais alta. 
# 
# Usou-se a taxa de mortalidade, pois permite uma melhor comparação de países com tamanhos populacionais diferentes.

# ## Os dados
# 
# Os dados correspondem a população total e número total de mortes por TB (excluídos os casos de HIV) em 2013 para cada um dos BRICS (Brasil, Rússia, Índia, China, África do Sul) e países de língua portuguesa.
# 
# Fonte dos dados extraídos em 07/2015 <http://apps.who.int/gho/data/node.main.POP107?lang=en> (população) e <http://apps.who.int/gho/ data/node.main.1317?lang=en> (mortes). 
# 
# A coleta foi feita por meio de arquivo Excel.

# In[1]:


import warnings
warnings.simplefilter('ignore', FutureWarning)

from pandas import *
data = read_excel('WHO POP TB some.xls')
data


# ## Magnitude do problema 

# In[2]:


tbColumn = data['TB deaths']


# O número total de mortes em 2013 é:

# In[3]:


tbColumn.sum()


# O maior e o menor número de mortes em um único país é da ordem de: 

# In[4]:


tbColumn.max()


# In[5]:


tbColumn.min()


# Quase um quarto de milhão de mortes é uma grande variação. O número médio de mortes, em todos os países nos dados, fornece uma  ideia melhor da gravidade do problema em cada país. A média pode ser calculada como a média ou a mediana. Dada a ampla gama de mortes, a mediana é provavelmente uma medida média mais coerente.

# In[6]:


tbColumn.mean()


# In[7]:


tbColumn.median()


# A mediana é bem menor do que a média. Indicando que alguns dos países obtiveram um número elevado de mortes por tuberculose em 2013, aumentando o valor da média.

# ## Países mais impactados
# 
# Para visualizar os países mais impactadoss, a tabela é classificada em ordem crescente pela última coluna, o que coloca esses países nas últimas linhas.

# In[8]:


data.sort_values('TB deaths')


# Quantos aos dados da tabela parece que um enorme número de mortes possa ser parcialmente devido a uma grande população. Para efetuar a comparar entre os países de forma mais igualitária, calculou-se a taxa de mortalidade por 100.000 habitantes.

# In[9]:


populationColumn = data['Population (1000s)']
data['TB deaths (per 100,000)'] = tbColumn * 100 / populationColumn
data


# ## Conclusão
# 
# Para os países como Brasil, Rússia, Índia, China, África do Sul (BRICS) e os países de língua portuguesa, estes obtiveram um total de cerca de 350 mil óbitos por Tuberculose em 2013. A mediana demonstra que metade desses países teve menos de 5.650 óbitos. A média muito mais elevada (mais de 29.000) mostra que alguns países tiveram um número muito alto. Os menos impactados foram São Tomé e Príncipe e a Guiné Equatorial, com 18 e 67 mortos respetivamente, e os mais impactados foram a China e a Índia com 41 mil e 240 mil mortos num só ano. No entanto, tendo em conta a dimensão da população, os menos impactados foram Portugal e Brasil com menos de 2,2 mortos por 100 mil habitantes, e os mais impactados foram a Guiné-Bissau e Timor-Leste com mais de 70 mortos por 100 mil habitantes.
# 
# Ressaltando que os valores são estimativas, e que os países escolhidos são uma pequena amostra de todos os países do mundo. No entanto, eles permitem chegar a conclusão de que a tuberculose ainda é uma das principais causas de mortes e que há uma grande disparidade entre os países, com diversos deles sendo elevadamente impactados.

# In[ ]:




