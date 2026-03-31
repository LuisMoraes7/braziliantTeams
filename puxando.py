import requests
import pandas as pd

teams = {
    "Palmeiras": 1963,
    "Athletico-PR": 1967,
    "São Paulo": 1981,
    "Fluminense": 1961,
    "Flamengo": 5981,
    "Bahia": 1955,
    "Coritiba": 1982,
    "Gremio": 5926,
    "Vasco": 1974,
    "Vitoria": 1962,
    "Corinthians": 1957,
    "Internacional": 1966,
    "Atletico-MG": 1977,
    "Bragantino": 1999,
    "Chapecoense": 21845,
    "Santos": 1968,
    "Botafogo": 1958,
    "Mirassol": 21982,
    "Remo": 2012,
    "Cruzeiro": 1954
}

headers = {
    "User-Agent": "Mozilla/5.0"
}

dados = []
erros = []
for nome, team_id in teams.items():
    
    url = f"http://sofascore.com/api/v1/team/{team_id}/unique-tournament/325/season/87678/statistics/overall"
    try:
        res = requests.get(url, headers=headers)
        if res.status_code != 200:
            
            erros.append(nome)
            continue
        data = res.json()

        stats = data.get("statistics", {})

        if not stats:
            erros.append(nome)
            continue

        stats["team"] = nome

        dados.append(stats)

        print(f"✅ {nome}")

    except:
        erros.append(nome)

# transformar em tabela

print("\nFinalizado!")
print(f"Coletados: {len(dados)}")

if erros:
    print("\n❌ Erros:")
    for e in erros:
        print(e)

print("Convertendo para DataFrame...")
df = pd.DataFrame(dados)
stats_type_df = pd.json_normalize(df["statisticsType"])
df = pd.concat([df, stats_type_df], axis=1)
df = df.drop(columns=["statisticsType"])
print("checar se foi salvo")
df.to_excel("dados_times.xlsx", index=False)