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
def deflation_brl(ano_ini, ano_fim, ano_data_column ,data_set):
    
    
    import subprocess
    import sys
    try:
        import sidrapy
        import pandas as pd
        import importlib
        
    except ImportError:
        print("Pacotes nao encontrados. Instalando...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "sidrapy","pandas","importlib"])
        sidrapy = importlib.import_module("sidrapy")
        pandas = importlib.import_module("pandas")
        importlib = importlib.import_module("importlib")
        print("Pacotes instalados com sucesso!")
    """
    Calcula o valor deflacionado de pagamentos em uma base de dados com ano e mês.
    Usa o IPCA acumulado do ano (variável 69 da tabela 1737 do SIDRA).
    
    Parâmetros:
    - ano_ini: ano inicial
    - ano_fim: ano final
    - diretorio: caminho do arquivo base
    - base_ano: ano de referência para trazer os valores reais
    - col_var_ano: coluna da variação (padrão 'V')
    
    Retorna:
    - DataFrame com coluna 'Pago_real' ajustada pelo deflator.
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
    #Realizando deflacao
    deflatores = []
    prod = 1.0
    for _, row in ipca_filtrado.iterrows():
        ano = row['ano']
        var = row['V'] / 100.0
        deflatores.append({'ano': ano, 'deflator': prod})
        prod *= (1 + var)

    df_deflatores = pd.DataFrame(deflatores).sort_values('ano')
    df = base.merge(df_deflatores, how='left', left_on=ano_data_column, right_on='ano')
    

    return df

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
    
    
    
