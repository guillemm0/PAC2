import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

st.title("Emissions de CO₂ per Sector i Continent – Gràfic Marimekko")
st.markdown(
    "L'**amplada** de cada columna representa el total d'emissions absolutes del continent. "
    "L'**alçada** de cada segment mostra el pes percentual de cada sector dins d'aquell continent. "
    "Els rectangles més grans indiquen on cal focalitzar els esforços de reducció."
)

# ── Càrrega de dades ───────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    return pd.read_csv("data/co-emissions-by-sector/co-emissions-by-sector.csv")

df = load_data()

CONTINENTS = ["Africa", "Asia", "Europe", "North America", "South America", "Oceania"]
SECTORS = [
    "Electricity and heat",
    "Manufacturing and construction",
    "Transport",
    "Industry",
    "Buildings",
    "Fugitive emissions",
    "Other fuel combustion",
    "Land-use change and forestry",
    "Aviation and shipping",
]
NOMS_SECTORS = {
    "Electricity and heat":              "Electricitat i calor",
    "Manufacturing and construction":    "Manufactura i construcció",
    "Transport":                         "Transport",
    "Industry":                          "Indústria",
    "Buildings":                         "Edificis",
    "Fugitive emissions":                "Emissions fugitives",
    "Other fuel combustion":             "Altra combustió",
    "Land-use change and forestry":      "Canvi d'ús del sòl",
    "Aviation and shipping":             "Aviació i navegació",
}
COLORS = [
    "#e15759", "#4e79a7", "#f28e2b", "#59a14f",
    "#76b7b2", "#edc948", "#b07aa1", "#ff9da7", "#9c755f",
]

# ── Filtres de la barra lateral ────────────────────────────────────────────────
st.sidebar.header("Filtres")
any_disponibles = sorted(df["Year"].unique())
any_inici, any_fi = st.sidebar.select_slider(
    "Rang d'anys",
    options=any_disponibles,
    value=(1990, 2023),
)

# ── Preparació de la taula pivot ───────────────────────────────────────────────
mask = (df["Year"] >= any_inici) & (df["Year"] <= any_fi) & (df["Entity"].isin(CONTINENTS))
pivot = (
    df[mask]
    .groupby("Entity")[SECTORS]
    .mean()
    .fillna(0)
    .reindex(CONTINENTS)
)

# Totals per continent i ordenació per emissions totals (descendent)
pivot["_total"] = pivot[SECTORS].sum(axis=1)
pivot = pivot.sort_values("_total", ascending=False)
totals = pivot["_total"].values
pivot = pivot[SECTORS]

# Percentatges (alçada de cada segment dins la columna)
pct = pivot.div(pivot.sum(axis=1), axis=0) * 100

# Amplades normalitzades: la suma total ocupa tot l'eix X (0–100)
total_global = totals.sum()
amplades = totals / total_global * 100

# Posicions centrals de cada columna (per als eixos X)
x_centres = []
x_right = []
acc = 0
for w in amplades:
    x_centres.append(acc + w / 2)
    acc += w
    x_right.append(acc)

continents = pivot.index.tolist()

# ── Construcció del gràfic Marimekko amb rectangles ───────────────────────────
fig = go.Figure()

for i, (sector, color) in enumerate(zip(SECTORS, COLORS)):
    nom = NOMS_SECTORS[sector]
    # Cada continent és un rectangle: x0,x1,y0,y1
    for j, continent in enumerate(continents):
        # y0 = suma dels percentatges dels sectors anteriors
        y0 = pct[SECTORS[:i]].iloc[j].sum()
        y1 = y0 + pct[sector].iloc[j]
        x0 = x_right[j] - amplades[j]
        x1 = x_right[j]

        val_tones = pivot[sector].iloc[j]
        val_gt = val_tones / 1e9  # gigatones

        fig.add_trace(
            go.Scatter(
                x=[x0, x1, x1, x0, x0],
                y=[y0, y0, y1, y1, y0],
                fill="toself",
                fillcolor=color,
                line=dict(color="white", width=0.8),
                mode="lines",
                name=nom,
                legendgroup=nom,
                showlegend=(j == 0),  # una sola entrada a la llegenda per sector
                hovertemplate=(
                    f"<b>{continent}</b><br>"
                    f"Sector: {nom}<br>"
                    f"Emissions: {val_gt:.2f} Gt CO₂<br>"
                    f"% del continent: {pct[sector].iloc[j]:.1f}%<br>"
                    f"% del total global: {val_tones/total_global*100:.1f}%"
                    "<extra></extra>"
                ),
            )
        )

# Etiquetes dels continents a l'eix X (centre de cada columna)
fig.update_layout(
    xaxis=dict(
        tickvals=x_centres,
        ticktext=[
            f"<b>{c}</b><br>{totals[i]/1e9:.1f} Gt"
            for i, c in enumerate(continents)
        ],
        tickfont=dict(size=11),
        showgrid=False,
        range=[0, 100],
    ),
    yaxis=dict(
        title="% d'emissions dins el continent",
        ticksuffix="%",
        range=[0, 100],
        showgrid=True,
        gridcolor="rgba(255,255,255,0.1)",
    ),
    title=f"Emissions de CO₂ per sector i continent ({any_inici}–{any_fi})" if any_inici != any_fi else f"Emissions de CO₂ per sector i continent ({any_inici})",
    template="plotly_dark",
    height=620,
    legend=dict(
        title="Sector",
        orientation="v",
        yanchor="top",
        y=1,
        xanchor="left",
        x=1.01,
        font=dict(size=11),
    ),
    margin=dict(l=60, r=220, t=80, b=80),
    hovermode="closest",
)

st.plotly_chart(fig, use_container_width=True)

# ── Mètriques de context ───────────────────────────────────────────────────────
st.subheader("Context global")
col1, col2, col3 = st.columns(3)
label_periode = f"{any_inici}–{any_fi}" if any_inici != any_fi else str(any_inici)
col1.metric(f"Mitjana anual global ({label_periode})", f"{total_global/1e9:.1f} Gt CO₂")
top_cont = continents[0]
col2.metric("Major emissor", f"{top_cont} ({totals[0]/total_global*100:.0f}%)")
top_sector_global = pivot.sum().idxmax()
col3.metric("Sector dominant", NOMS_SECTORS[top_sector_global])
