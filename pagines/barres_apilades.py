import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("Informe Mundial de la Felicitat 2023 – Barres Apilades")
st.markdown(
    "Cada barra representa la puntuació de felicitat d'un país, "
    "desglossada pels sis factors explicatius i la distopia residual."
)

# Càrrega de dades 
@st.cache_data
def load_data():
    df = pd.read_csv("data/WHR2023.csv")
    return df

df = load_data()

# Columnes dels factors (les que sumen el Ladder score)
FACTORS = {
    "Explained by: Log GDP per capita":          "PIB per càpita",
    "Explained by: Social support":              "Suport social",
    "Explained by: Healthy life expectancy":     "Esperança de vida",
    "Explained by: Freedom to make life choices":"Llibertat d'elecció",
    "Explained by: Generosity":                  "Generositat",
    "Explained by: Perceptions of corruption":   "Percepció de corrupció",
    "Dystopia + residual":                       "Distopia + residual",
}

COLORS = [
    "#4e79a7",  # PIB
    "#f28e2b",  # Suport social
    "#59a14f",  # Esperança de vida
    "#e15759",  # Llibertat
    "#76b7b2",  # Generositat
    "#edc948",  # Corrupció
    "#b07aa1",  # Distopia
]

# Filtres de la barra lateral 
st.sidebar.header("Filtres")
n_paisos = st.sidebar.slider("Nombre de països a mostrar", 5, 30, 15)
ordre = st.sidebar.radio("Ordre", ["Descendent", "Ascendent"])

ascending = ordre.startswith("Ascendent")
top_df = (
    df.sort_values("Ladder score", ascending=ascending)
    .head(n_paisos)
    .reset_index(drop=True)
)

# Construcció del gràfic 
fig = go.Figure()

for (col_orig, nom_cat), color in zip(FACTORS.items(), COLORS):
    fig.add_trace(
        go.Bar(
            name=nom_cat,
            x=top_df["Country name"],
            y=top_df[col_orig],
            marker_color=color,
            hovertemplate=(
                "<b>%{x}</b><br>"
                f"{nom_cat}: %{{y:.3f}}<extra></extra>"
            ),
        )
    )

fig.update_layout(
    barmode="stack",
    title=f"Puntuació de felicitat per país — Top {n_paisos} ({ordre.split()[0].lower()})",
    xaxis_title="País",
    yaxis_title="Puntuació de felicitat (Ladder score)",
    template="plotly_dark",
    height=600,
    legend=dict(
        title="Factor",
        orientation="v",
        yanchor="top",
        y=1,
        xanchor="left",
        x=1.01,
    ),
    margin=dict(l=50, r=200, t=80, b=120),
    xaxis_tickangle=-40,
)

st.plotly_chart(fig, use_container_width=True)
