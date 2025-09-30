import pandas as pd
import re
import numpy as np
from unidecode import unidecode
import dask.dataframe as dd
import multiprocessing
import os
import time
import dask.system
# BRL Deflation
def deflation_brl(ano_ini, ano_fim,db_host,db_name,user,password):
    
    
    import subprocess
    import sys
    try:
        import sidrapy
        import pandas as pd
        import importlib
        import psycopg
        
    except ImportError:
        print("Pacotes nao encontrados. Instalando...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "sidrapy","pandas","importlib","psycopg[binary]"])
        sidrapy = importlib.import_module("sidrapy")
        pandas = importlib.import_module("pandas")
        importlib = importlib.import_module("importlib")
        print("Pacotes instalados com sucesso!")
    """
    
    
    Parâmetros:
    - ano_ini: ano inicial
    - ano_fim: ano final
  
    """
    base = data_set
    #Coleta de dados do IPCA atraves do pacote sidraPy que é gerido pelo IBGE
    data = sidrapy.get_table(
        table_code="1737",
        territorial_level="1",
        ibge_territorial_code="all",
        period="all",
        variable="all"
    )
    ipca = data[data['D3C'] == '69'].copy()
    ipca['ano'] = ipca['D2C'].str[:4].astype(int)
    ipca['mes'] = ipca['D2C'].str[-2:]
    ipca['ano'] = pd.to_numeric(ipca['ano'])
    ipca_filtrado = ipca[(ipca['mes'] == '12') & (ipca['ano'] >= ano_ini) & (ipca['ano'] <= ano_fim)]
    ipca_filtrado = ipca_filtrado.sort_values('ano', ascending=False)
    ipca_filtrado['V'] = pd.to_numeric(ipca_filtrado['V'])
    ipca_filtrado.rename(columns={'V':'inflacao',
                                  'ano':'year'},inplace = True)
    conn = psycopg.connect(f"host={db_host} dbname={db_name} user={user} password={password}")
    with conn:
        with conn.cursor() as cur:
            for row in ipca_filtrado[['year','inflacao']].itertuples(index=False):
                cur.execute(
                        "INSERT INTO indice_inflacao (year, inflacao) VALUES (%s, %s);",
                        (row.year, row.inflacao)
                )



# dollarization function
def dollarization(date_ini,date_fim,db_host,db_name,user,password):
    """
    date_ini: yyyy-mm-dd
    date_fim: yyyy-mm-dd
    """
    
    import importlib
    import subprocess
    import sys
    try:
        from bcb.sgs import get
        import pandas as pd
        import psycopg
        
    except ImportError:
        print("Pacotes nao encontrados. Instalando...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas", "bcb","psycopg[binary]"])
        import pandas as pd
        from bcb.sgs import get
        
        print("Pacotes instalados com sucesso!")
    
    cambio = get({'dolar_compra': 1}, start=date_ini, end=date_fim)
    cambio.reset_index(inplace = True)
    cambio['year']  = cambio.Date.dt.year
    cambio_mean_by_year = cambio.groupby('year').dolar_compra.mean().reset_index()
    conn = psycopg.connect(f"host={db_host} dbname={db_name} user={user} password={password}")
    with conn:
        with conn.cursor() as cur:
            for row in cambio_mean_by_year.itertuples(index=False):
                cur.execute(
                    "INSERT INTO bcb_dolar (year, cotacao_dolar) VALUES (%s, %s);",
                    (row.year, row.dolar_compra)
            )
    
    
    
