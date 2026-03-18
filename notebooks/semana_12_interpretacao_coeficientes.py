import marimo

__generated_with = "0.11.20"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import statsmodels.formula.api as smf
    from scipy import stats
    from physical_education_statistics import load_dataset

    sns.set_theme(style="whitegrid")
    df = load_dataset("growth")
    variable_options = [
            "forca_membros_inferiores",
            "idade",
            "altura_cm",
            "massa_kg",
    ]
    return df, mo, np, pd, plt, sns, smf, stats, variable_options


@app.cell
def _(mo):
    mo.md(r"""
    # Semana 12 — Interpretação de coeficientes

    **Objetivo da semana:** Traduzir coeficientes e intervalos de confiança para linguagem aplicada.

    **Por que isso importa?** Nesta semana a ênfase é comunicação científica. O notebook ajuda a transformar saídas numéricas em frases interpretáveis por profissionais da Educação Física.

    > Dica para iniciantes: siga o notebook de cima para baixo. Em cada etapa, altere os controles interativos e observe como a interpretação muda.
    """)
    return


@app.cell
def _(df, mo):
    linhas = mo.ui.slider(5, min(5, len(df)), value=min(8, len(df)), label="Quantas linhas da base você quer inspecionar?")
    return linhas


@app.cell
def _(df, linhas, mo):
    mo.vstack([
        mo.md("## 1. Conhecendo a base de dados"),
        mo.md(f"A base possui **{df.shape[0]} linhas** e **{df.shape[1]} colunas**."),
        df.head(linhas.value),
    ])
    return


@app.cell
def _(mo, variable_options):
    variavel_x = mo.ui.dropdown(options=variable_options, value="forca_membros_inferiores", label="Variável principal")
    variavel_y = mo.ui.dropdown(options=variable_options, value="idade", label="Variável secundária")
    return variavel_x, variavel_y


@app.cell
def _(df, mo, variavel_x):
    resumo = df[variavel_x.value].describe().to_frame(name="valor")
    interpretacao = mo.md(
        f"""
        ## 2. Resumo estatístico

        A variável **{variavel_x.value}** foi resumida com medidas clássicas de posição e dispersão.

        - **Média:** indica o valor médio do grupo.
        - **Desvio-padrão:** indica quão espalhados os dados estão.
        - **Mínimo e máximo:** ajudam a localizar valores extremos.
        """
    )
    mo.vstack([interpretacao, resumo])
    return resumo


@app.cell
def _(df, mo, plt, sns, variavel_x):
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(df[variavel_x.value], kde=True, ax=ax, color="#2a9d8f")
    ax.set_title("Intervalos de confiança de " + variavel_x.value)
    ax.set_xlabel(variavel_x.value)
    ax.set_ylabel("Frequência")
    mo.vstack([
        mo.md("## 3. Visualização inicial"),
        mo.md("Use o histograma para verificar se os valores parecem concentrados, assimétricos ou muito dispersos."),
        mo.as_html(fig),
    ])
    return fig


@app.cell
def _(mo):
    filtro_grupo = mo.ui.dropdown(options=["Todos", "sexo"] if "sexo" in ["sexo", "participa_esporte", "grupo", "idade"] else ["Todos"], value="Todos", label="Agrupar análise?")
    return filtro_grupo


@app.cell
def _(df, mo, plt, sns, variavel_x):
    coluna_grupo = "sexo"
    componentes = [mo.md("## 4. Comparando grupos")] 
    if coluna_grupo in df.columns:
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.boxplot(data=df, x=coluna_grupo, y=variavel_x.value, ax=ax, palette="Set2")
        ax.set_title("Cenários simulados para " + variavel_x.value)
        componentes.extend([
            mo.md(f"A comparação por **{coluna_grupo}** ajuda a observar se a distribuição muda entre grupos relevantes da pesquisa."),
            mo.as_html(fig),
            df.groupby(coluna_grupo)[variavel_x.value].agg(["mean", "median", "std", "count"]).round(2),
        ])
    else:
        componentes.append(mo.md("Esta base não possui um agrupador categórico simples para esta etapa, então foque na interpretação da distribuição geral."))
    mo.vstack(componentes)
    return


@app.cell
def _(df, mo, np, pd, plt, sns, stats, variavel_x, variavel_y):
    componentes = [mo.md("## 5. Relação entre duas variáveis")]
    if variavel_x.value != variavel_y.value:
        pares = df[[variavel_x.value, variavel_y.value]].dropna()
        r, p = stats.pearsonr(pares[variavel_x.value], pares[variavel_y.value])
        fig, ax = plt.subplots(figsize=(7, 5))
        sns.regplot(data=pares, x=variavel_x.value, y=variavel_y.value, ax=ax, scatter_kws={"alpha": 0.7})
        ax.set_title("Relação entre " + variavel_x.value + " e " + variavel_y.value)
        componentes.extend([
            mo.md(f"Correlação de Pearson: **r = {r:.3f}** com **p = {p:.4f}**."),
            mo.md("Lembre-se: correlação não prova causa e efeito. Ela apenas mostra o quanto duas variáveis variam juntas de maneira linear."),
            mo.as_html(fig),
            pares.corr(numeric_only=True).round(2),
        ])
    else:
        componentes.append(mo.md("Escolha variáveis diferentes nos controles acima para enxergar a relação entre elas."))
    mo.vstack(componentes)
    return


@app.cell
def _(df, mo, smf, variavel_x, variavel_y):
    componentes = [mo.md("## 6. Modelo estatístico explicado")]
    if variavel_x.value != variavel_y.value:
        formula = f"{variavel_y.value} ~ {variavel_x.value}"
        modelo = smf.ols(formula, data=df).fit()
        tabela = modelo.summary2().tables[1].round(4)
        componentes.extend([
            mo.md(f"Modelo ajustado: `{formula}`"),
            mo.md("Leia a linha da variável explicativa como a mudança média esperada em Y quando X aumenta uma unidade."),
            tabela,
            mo.md(f"**R² = {modelo.rsquared:.3f}**. Isso indica a proporção da variação de `{variavel_y.value}` explicada por `{variavel_x.value}`."),
        ])
    else:
        componentes.append(mo.md("Quando X e Y são iguais, não faz sentido ajustar regressão. Selecione variáveis diferentes."))
    mo.vstack(componentes)
    return


@app.cell
def _(df, mo, variable_options):
    perguntas = [
        "O que a média me conta sobre o grupo estudado?",
        "A dispersão observada parece pequena ou grande para o contexto aplicado?",
        "Os grupos parecem diferentes visualmente? Como eu justificaria isso em texto?",
        "Se eu estivesse escrevendo um artigo, que resultado principal eu destacaria?",
    ]
    mo.vstack([
        mo.md("## 7. Perguntas-guia para estudo"),
        mo.md("Use estas perguntas como roteiro de interpretação antes de avançar para a próxima semana:"),
        mo.md("\n".join([f"- {p}" for p in perguntas])),
    ])
    return


if __name__ == "__main__":
    app.run()
