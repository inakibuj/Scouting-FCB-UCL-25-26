import undetected_chromedriver as uc
import pandas as pd
import time
import re
from io import StringIO

print("🤖 Iniciando navegador Chrome automatizado (Modo Seguro)...")
opciones = uc.ChromeOptions()


opciones.add_argument('--disable-gpu')
opciones.add_argument('--no-sandbox')
opciones.add_argument('--disable-dev-shm-usage')


driver = uc.Chrome(options=opciones, version_main=146)

url = "https://fbref.com/en/squads/206d90db/2025-2026/c8/Barcelona-Stats-Champions-League"

print("🌐 Accediendo a FBref y negociando con Cloudflare...")
driver.get(url)


print("⏳ Esperando 20 segundos para asegurar que la página cargue por completo...")
time.sleep(20) 


html_crudo = driver.page_source
driver.quit() 
print("✅ ¡Seguridad superada y HTML capturado!")

print("🧹 Limpiando y buscando tablas...")
html_limpio = re.sub(r'', '', html_crudo)


df_standard = pd.read_html(StringIO(html_limpio), match=r"G\+A")[0]
df_playing = pd.read_html(StringIO(html_limpio), match=r"Min%")[0]

def limpiar_fbref(df):
    nuevas_columnas = []
    for col in df.columns:
        if isinstance(col, tuple):
            if "Unnamed" in col[0]:
                nuevas_columnas.append(col[1])
            else:
                nuevas_columnas.append(f"{col[0]}_{col[1]}")
        else:
            nuevas_columnas.append(col)
            
    df.columns = nuevas_columnas
    df = df[~df['Player'].isin(['Squad Total', 'Opponent Total'])]
    return df

print("🔄 Normalizando estructuras...")
df_standard_clean = limpiar_fbref(df_standard)
df_playing_clean = limpiar_fbref(df_playing)

print("✂️ Eliminando columnas duplicadas antes de cruzar...")

columnas_llave = ['Player', 'Nation', 'Pos', 'Age']
columnas_comunes = set(df_standard_clean.columns).intersection(set(df_playing_clean.columns))
columnas_duplicadas = list(columnas_comunes - set(columnas_llave))


df_playing_clean = df_playing_clean.drop(columns=columnas_duplicadas)

print("🔗 Realizando el Merge maestro...")
df_master = pd.merge(df_standard_clean, df_playing_clean, on=columnas_llave, how='left')

nombre_archivo = 'barca_ucl_stats_automated.csv'
df_master.to_csv(nombre_archivo, index=False)
print(f"🎉 ¡Éxito! Base de datos maestra '{nombre_archivo}' creada sin duplicados.")