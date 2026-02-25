import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

# conexão
engine = create_engine("postgresql://postgres:regp2569@127.0.0.1:5432/engdados")

try:
    # ler csv
    df = pd.read_csv("data/clientes.csv")
    print("Arquivo lido com sucesso!")
    print(df)

    # inserir no banco
    df.to_sql(
        "clientes",
        engine,
        if_exists="append",  # mantém tabela e adiciona registros
        index=False
    )

    print("Dados inseridos com sucesso!")

except SQLAlchemyError as e:
    print("Erro ao inserir no banco:")
    print(e)

except Exception as e:
    print("Erro geral:")
    print(e)
