import pandas as pd
from pathlib import Path

arquivo = Path("202608-divvy-tripdata.csv")
n_partes = 2

df = pd.read_csv(arquivo, dtype=str)

linhas_por_parte, resto = divmod(len(df), n_partes)
inicio = 0

for i in range(n_partes):
    quantidade = linhas_por_parte + (1 if i < resto else 0)
    parte = df.iloc[inicio:inicio + quantidade]
    caminho_saida = arquivo.with_name(
        f"{arquivo.stem}_parte{i + 1}.csv"
    )
    parte.to_csv(caminho_saida, index=False)
    print(f"Parte {i + 1}: {len(parte)} linhas")
    inicio += quantidade