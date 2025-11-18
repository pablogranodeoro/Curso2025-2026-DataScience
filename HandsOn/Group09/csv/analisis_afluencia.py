import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("afluencia_media_mensual.csv")

meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio",
               "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

df["mes"] = pd.Categorical(df["mes"], categories=meses, ordered=True)

# ─────────────────────────────────────────────
# Media de cada línea por año
# ─────────────────────────────────────────────
media_linea_anio = df.groupby(["anio", "linea"], as_index=False)["afluencia_media"].mean()

plt.figure(figsize=(10,6))
for linea, datos in media_linea_anio.groupby("linea"):
    plt.plot(datos["anio"], datos["afluencia_media"], marker="o", label=linea)
plt.title("Media de afluencia por línea y año")
plt.xlabel("Año")
plt.ylabel("Afluencia media")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ─────────────────────────────────────────────
# Media de cada línea por mes
# ─────────────────────────────────────────────
media_linea_mes = df.groupby(["mes", "linea"], as_index=False)["afluencia_media"].mean()

plt.figure(figsize=(10,6))
for linea, datos in media_linea_mes.groupby("linea"):
    plt.plot(datos["mes"], datos["afluencia_media"], marker="o", label=linea)
plt.title("Media de afluencia por línea y mes")
plt.xlabel("Mes")
plt.ylabel("Afluencia media")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ─────────────────────────────────────────────
# Estaciones con mayor afluencia (Top 10)
# ─────────────────────────────────────────────
media_estacion = df.groupby("ESTACION_URI", as_index=False)["afluencia_media"].mean()
top_estaciones = media_estacion.sort_values("afluencia_media", ascending=False).head(10)

plt.figure(figsize=(10,6))
plt.barh(top_estaciones["ESTACION_URI"], top_estaciones["afluencia_media"], color="steelblue")
plt.title("Top 10 estaciones con mayor afluencia media")
plt.xlabel("Afluencia media")
plt.ylabel("Estación")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# ─────────────────────────────────────────────
# Meses con mayor afluencia (promedio global)
# ─────────────────────────────────────────────
media_mes_global = df.groupby("mes", as_index=False)["afluencia_media"].mean()

plt.figure(figsize=(10,6))
plt.bar(media_mes_global["mes"], media_mes_global["afluencia_media"], color="orange")
plt.title("Afluencia media global por mes")
plt.xlabel("Mes")
plt.ylabel("Afluencia media")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ─────────────────────────────────────────────
# Heatmap (año vs mes)
# ─────────────────────────────────────────────
import seaborn as sns

tabla_heatmap = (
    df.groupby(["anio", "mes"], as_index=False)["afluencia_media"].mean()
    .pivot(index="anio", columns="mes", values="afluencia_media")
    .reindex(columns=meses)
)

plt.figure(figsize=(12,7))
sns.heatmap(tabla_heatmap, cmap="YlOrRd", annot=True, fmt=".0f")
plt.title("Mapa de calor: afluencia media por año y mes")
plt.xlabel("Mes")
plt.ylabel("Año")
plt.tight_layout()
plt.show()
