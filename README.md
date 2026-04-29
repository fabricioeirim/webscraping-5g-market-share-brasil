📊 Web Scraping – Market Share 5G no Brasil
📌 Visão Geral
Este projeto realiza web scraping de dados públicos sobre o mercado 5G no Brasil, coletando informações de market share, quantidade de celulares 5G e adições mensais/trimestrais por operadora.
A extração é feita a partir do site Teleco, utilizando BeautifulSoup e Pandas, com posterior estruturação dos dados para análise e armazenamento.

🌐 Fonte dos Dados

Site: https://www.teleco.com.br/5g_brasil.asp
Conteúdo:

Market share 5G por operadora
Quantidade total de celulares 5G
Adições mensais e trimestrais



📌 Os dados são de acesso público e utilizados apenas para fins educacionais e analíticos.

🛠️ Tecnologias Utilizadas

Python 3
Requests
BeautifulSoup (bs4)
Pandas
lxml / html5lib
Excel (.xlsx)

🔄 Pipeline de Extração:

HTTP Request
     ↓
HTML Parsing (BeautifulSoup)
     ↓
Extração de tabelas HTML
     ↓
Tratamento com Pandas
     ↓
Exportação para Excel

▶️ Funcionamento do Script
✅ 1. Requisição HTTP

Acesso ao site com requests
Uso de User-Agent para evitar bloqueios

✅ 2. Parsing do HTML

Leitura do conteúdo HTML com BeautifulSoup
Identificação das tabelas relevantes

✅ 3. Extração dos Dados

Conversão das tabelas HTML para DataFrames Pandas
Separação lógica dos dados:

Market Share 5G (mês a mês)
Quantidade total de celulares 5G
Adições mensais
Adições trimestrais



✅ 4. Persistência

Exportação dos datasets em Excel
Dados prontos para análise exploratória e visualização


📁 Dados Gerados

MKS_5G_MES_A_MES.xlsx
QTD_CELULARES_5G_MES_A_MES.xlsx
TOTAL_CELULARES_5G_ADD_MES_A_MES.xlsx
TOTAL_CELULARES_5G_ADD_TRIMESTRE_A_TRIMESTRE.xlsx


🎯 Objetivos do Projeto

Praticar web scraping estruturado
Trabalhar com dados não estruturados (HTML)
Criar pipeline reutilizável de coleta de dados
Analisar o mercado 5G no Brasil
Construir projeto de portfólio para Data Engineer / Data Analyst


🚀 Possíveis Evoluções

Automatização com agendador (cron / Task Scheduler)
Armazenamento em banco de dados
Carga em BigQuery
Criação de dashboards
Monitoramento de mudanças no layout da página
Versionamento histórico dos dados


📄 Observações
Este projeto possui finalidade educacional, sem fins comerciais, e respeita os dados disponibilizados publicamente pela fonte.


