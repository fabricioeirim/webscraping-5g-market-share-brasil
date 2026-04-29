import requests
import pandas as pd
from bs4 import BeautifulSoup


url = "https://www.teleco.com.br/5g_brasil.asp"
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.55"}
site = requests.get(url, headers = headers)


if requests.status_codes == 200:
    print("OK")


soup = BeautifulSoup(site.content, "html.parser")
tabela = soup.find_all('table',width="95%",height="219",border="1",align="center",cellpadding="5",cellspacing="0")
tabela_str = str(tabela)
tabela_str
df1 = pd.read_html(tabela_str)


soup = BeautifulSoup(site.content, "html.parser")
tabela = soup.find_all('table',width="95%",height="219",border="1",align="center",cellpadding="5",cellspacing="0")
tabela_str = str(tabela)
tabela_str
df2 = pd.read_html(tabela_str)


#O Mks nesse caso é apenas para o 5G
df_MKS_5G_MES_a_MES=pd.DataFrame(df1[0])
df_MKS_5G_MES_a_MES


#O número absoluto de celulares 5G deve ser x1000
df_QTD_CELULARES = df2[1]
df_QTD_CELULARES


#Adições celulares 5G mes a mes.
df_ADD_CELULARES = df2[2]
df_ADD_CELULARES


#Adições celulares 5G mes a mes.
df_ADD_CELULARES_TRIMETRE = df2[2]
df_ADD_CELULARES_TRIMETRE


df_MKS_5G_MES_a_MES.to_excel("MKS_5G_MES_a_MES.xlsx",index=False)
#df_MKS_5G_TRIMETRE.to_excel("MKS_5G_TIMESTRE_a_TRIMESTRE.xlsx",index=False,encoding='utf-8')
df_QTD_CELULARES.to_excel("QTD_CELULARES_5G_MES_A_MES.xlsx",index=False)
df_ADD_CELULARES.to_excel("TOTAL_CELULARES_5G_ADD_MES_a_MES.xlsx",index=False)
df_ADD_CELULARES_TRIMETRE.to_excel("TOTAL_CELULARES_5G_ADD_TRIMETRE_a_TRIEMSTRE.xlsx",index=False)


