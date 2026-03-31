# Estatísticas de Times Brasileiros

## Descrição

Este projeto coleta estatísticas de times brasileiros de futebol utilizando a API do SofaScore. O script principal (`puxando.py`) faz requisições para obter dados estatísticos de diversos times e salva os resultados em um arquivo Excel (`dados_times.xlsx`).

## Funcionalidades

- Coleta estatísticas de times brasileiros
- Processamento dos dados em formato tabular
- Exportação para Excel
- Tratamento de erros para times não encontrados

## Instalação

1. Clone este repositório:
   ```
   git clone <url-do-repositorio>
   cd brazilianteams
   ```

2. Crie um ambiente virtual:
   ```
   python -m venv venv
   ```

3. Ative o ambiente virtual:
   - No Linux/Mac: `source venv/bin/activate`
   - No Windows: `venv\Scripts\activate`

4. Instale as dependências:
   ```
   pip install requests pandas openpyxl
   ```

## Uso

Execute o script principal:
```
python puxando.py
```

O script irá:
- Fazer requisições para a API do SofaScore para cada time listado
- Coletar as estatísticas disponíveis
- Exibir o progresso no terminal
- Salvar os dados coletados em `dados_times.xlsx`

## Dependências

- `requests`: Para fazer requisições HTTP à API
- `pandas`: Para manipulação e processamento dos dados
- `openpyxl`: Para exportar os dados para Excel

## Arquivos

- `puxando.py`: Script principal que coleta e processa os dados
- `README.md`: Este arquivo

## Times Incluídos

O script coleta dados dos seguintes times:
- Palmeiras
- Athletico-PR
- São Paulo
- Fluminense
- Flamengo
- Bahia
- Coritiba
- Grêmio
- Vasco
- Vitória
- Corinthians
- Internacional
- Atlético-MG
- Bragantino
- Chapecoense
- Santos
- Botafogo
- Mirassol
- Remo
- Cruzeiro

## Saída

Os dados são salvos em `dados_times.xlsx` com as estatísticas normalizadas em colunas.

## Notas

- Certifique-se de ter uma conexão com a internet para executar o script
- Alguns times podem não ter dados disponíveis, sendo listados como erros
- O script usa um User-Agent para simular um navegador web