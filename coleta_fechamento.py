import pandas as pd
import yfinance as yf
from datetime import date

df_papeis = pd.read_excel("Carteira.xlsx", sheet_name="PAPEIS")
papeis = (df_papeis["Papel"].dropna().astype(str).unique().tolist())
hoje = date.today()

dados = []
for papel in papeis:
    try:
        ticker = yf.Ticker(f"{papel}.SA")
        fechamento = ticker.history(period="1d")["Close"].iloc[0]
        dados.append([
            hoje,
            papel,
            round(float(fechamento), 2)
        ])
    except Exception as e:
        print(f"Erro no papel {papel}: {e}")

# =============================
# GERAR CSV
# =============================
df_fechamento = pd.DataFrame(
    dados,
    columns=["Data", "Papel", "Fechamento"]
)

df_fechamento.to_csv(
    "Fechamento_Diario.csv",
    index=False
)
