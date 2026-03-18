<div align="center">

# 📊 Estatística Aplicada ao Desenvolvimento Motor
### Plano de Estudos para Estudantes de Educação Física (Preparação para Mestrado)

</div>

Este repositório apresenta um **roteiro estruturado de estudo em estatística aplicada ao desenvolvimento humano**, com foco em **desenvolvimento motor, crescimento, aprendizagem motora e atividade física ao longo da vida**.

O objetivo é ajudar estudantes de Educação Física a **reaprender estatística de forma aplicada**, conectando teoria estatística, leitura de artigos científicos e análise de dados com Python.

O plano é inspirado no funcionamento real da pesquisa científica na área.

---

## 🧭 Sumário

- [Filosofia do Plano](#-filosofia-do-plano)
- [Duração e Carga de Estudo](#-duração-e-carga-de-estudo)
- [Livros Utilizados](#-livros-utilizados)
- [Ambiente Computacional](#-ambiente-computacional)
- [Datasets Utilizados](#-datasets-utilizados)
- [Artigos Seminais Utilizados](#-artigos-seminais-utilizados)
- [Cronograma de Estudos](#-cronograma-de-estudos)
- [Projeto Final](#-projeto-final)
- [Estrutura Recomendada de Cada Notebook](#-estrutura-recomendada-de-cada-notebook)
- [Resultado Esperado](#-resultado-esperado)
- [Objetivo Final](#-objetivo-final)

---

## 🎯 Filosofia do Plano

O aprendizado segue o ciclo:

```text
Conceito → Artigo Científico → Análise de Dados → Interpretação Científica
```

Em cada semana, o estudante irá:

1. Ler um capítulo de livro-texto para entender o conceito estatístico.
2. Ler um artigo científico seminal da área de desenvolvimento.
3. Reproduzir uma análise semelhante usando Python e datasets públicos.

O foco não é apenas aprender teoria estatística, mas **entender como estatística responde perguntas científicas sobre desenvolvimento humano**.

---

## ⏳ Duração e Carga de Estudo

**Duração total:** 16 semanas (~4 meses)

**Carga semanal recomendada:**

| Atividade | Tempo |
|---|---|
| Leitura de livro | 2–3h |
| Leitura de artigo | 1–2h |
| Exercícios Python | 3–4h |

**Total semanal:** **6–8h**

---

## 📚 Livros Utilizados

### Livro principal

**Statistics in Kinesiology**  
Vincent J. Vincent & Joseph P. Weir  
Human Kinetics

Conteúdo principal:

- estatística descritiva
- correlação
- regressão
- testes t
- ANOVA
- confiabilidade
- interpretação de resultados

### Livro complementar

**Research Methods in Physical Activity**  
Thomas, Nelson & Silverman

Conteúdo principal:

- desenho de pesquisa
- interpretação de artigos científicos
- métodos quantitativos

---

## 💻 Ambiente Computacional

Ferramentas recomendadas:

- Python 3.10+
- marimo para notebooks interativos
- VS Code, terminal ou editor de sua preferência

Bibliotecas necessárias (já configuradas no projeto):

```text
marimo
pandas
numpy
matplotlib
seaborn
scipy
statsmodels
scikit-learn
plotly
```

Instalação plug and play:

```bash
python -m venv .venv
source .venv/bin/activate  # no Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install --no-build-isolation -e .
python scripts/generate_datasets.py
```

Como abrir um notebook marimo:

```bash
marimo edit notebooks/semana_01_estatistica_descritiva.py
```

Atalhos úteis:

```bash
make setup
make generate-data
make list-notebooks
```

Os notebooks interativos das 16 semanas estão na pasta `notebooks/` e o índice completo está em `notebooks/README.md`.

---

## 🗂️ Datasets Utilizados

### TGMD Dataset (Test of Gross Motor Development)

**Descrição:**

Avalia habilidades motoras fundamentais em crianças.

**Variáveis comuns:**

- correr
- saltar
- chutar
- arremessar
- escore motor total

**Fontes possíveis:**

Open Science Framework  
[https://osf.io](https://osf.io)

Exemplos de datasets TGMD publicados em repositórios de pesquisa.

### Early Childhood Longitudinal Study (ECLS)

[https://nces.ed.gov/ecls/](https://nces.ed.gov/ecls/)

Contém:

- desenvolvimento infantil
- habilidades motoras
- desempenho escolar
- atividade física

Muito usado em estudos de desenvolvimento humano.

### NHANES Youth Physical Activity

[https://www.cdc.gov/nchs/nhanes/](https://www.cdc.gov/nchs/nhanes/)

Variáveis:

- atividade física
- IMC
- idade
- sexo
- indicadores de saúde

### Motor Competence Dataset

Datasets usados em estudos baseados no modelo de Stodden.

Fontes:

Open Science Framework  
[https://osf.io](https://osf.io)

### Growth and Maturation Dataset

Dados de crescimento infantil e adolescência.

Exemplo clássico:

Berkeley Growth Study

Outros datasets disponíveis em repositórios acadêmicos.

### Youth Sports Participation Dataset

Participação esportiva em jovens.

Fonte:

Kaggle  
[https://www.kaggle.com](https://www.kaggle.com)

### Motor Learning Experiment Dataset

Dados experimentais de aprendizagem motora.

Disponíveis em:

Open Science Framework  
[https://osf.io](https://osf.io)

---

## 🧪 Artigos Seminais Utilizados

### Desenvolvimento Motor

#### Stodden et al. (2008)

**A Developmental Perspective on the Role of Motor Skill Competence in Physical Activity**

DOI:  
[https://doi.org/10.1249/MSS.0b013e31818160e8](https://doi.org/10.1249/MSS.0b013e31818160e8)

Contribuição:

Propõe um modelo de relação entre:

- competência motora
- atividade física
- aptidão física
- obesidade infantil

Este é um dos artigos mais influentes da área.

#### Robinson et al. (2015)

**Motor Competence and its Effect on Positive Developmental Trajectories**

DOI:  
[https://doi.org/10.1016/j.jsams.2014.12.007](https://doi.org/10.1016/j.jsams.2014.12.007)

Discute a importância da competência motora para o desenvolvimento saudável.

### Crescimento e Maturação

#### Malina, Bouchard & Bar-Or

**Growth, Maturation, and Physical Activity**

DOI:  
[https://doi.org/10.5040/9781492596837](https://doi.org/10.5040/9781492596837)

Referência clássica sobre:

- crescimento físico
- maturação biológica
- desenvolvimento motor

### Tracking de Atividade Física

#### Telama (2009)

**Tracking of Physical Activity from Childhood to Adulthood**

DOI:  
[https://doi.org/10.1249/MSS.0b013e3181a7c4b1](https://doi.org/10.1249/MSS.0b013e3181a7c4b1)

Mostra como níveis de atividade física se mantêm ao longo da vida.

### Aprendizagem Motora

#### Schmidt (1975)

**Schema Theory of Discrete Motor Skill Learning**

DOI:  
[https://doi.org/10.1123/jmle.7.2.225](https://doi.org/10.1123/jmle.7.2.225)

Teoria fundamental da aprendizagem motora.

#### Wulf (2013)

**Attentional Focus and Motor Learning**

DOI:  
[https://doi.org/10.1123/mcj.2012-0113](https://doi.org/10.1123/mcj.2012-0113)

Mostra como foco atencional influencia aprendizagem motora.

---

## 🗓️ Cronograma de Estudos

## Fase 1 — Medindo Desenvolvimento Motor (Semanas 1–4)

**Pergunta científica central:**

> Como descrever o nível de desenvolvimento motor de uma população?

**Estatística aprendida:**

- média
- desvio padrão
- percentis
- visualização de dados

### Semana 1 — Estatística Descritiva

**Livro:**  
Statistics in Kinesiology  
Capítulos iniciais de estatística descritiva.

**Artigo:**  
Stodden et al. (2008)

**Tarefa computacional:**  
Dataset: TGMD

**Objetivos:**

- calcular média de habilidades motoras
- calcular desvio padrão
- criar histogramas
- comparar médias por sexo

Exemplo:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("tgmd_dataset.csv")

print(df.describe())

df.hist()
plt.show()
```

### Semana 2 — Percentis e Normativas

**Objetivo:**

Criar curvas de referência de desenvolvimento motor.

**Tarefa:**

- calcular percentis por idade
- criar gráficos de desenvolvimento

**Dataset:**

TGMD dataset

### Semana 3 — Correlação

**Pergunta:**

> Crianças com maior competência motora são mais fisicamente ativas?

**Estatística:**

- correlação de Pearson

**Dataset:**

motor competence dataset

**Tarefas Python:**

- matriz de correlação
- scatter plots

### Semana 4 — Regressão

**Objetivo:**

Modelar relação entre variáveis de desenvolvimento.

Modelo exemplo:

```text
atividade_fisica ~ competencia_motora
```

Ferramentas:

statsmodels ou scikit-learn

## Fase 2 — Competência Motora e Atividade Física (Semanas 5–8)

**Artigo central:**  
Stodden et al. (2008)

**Pergunta científica:**

> Competência motora prediz níveis de atividade física?

**Estatística aprendida:**

- regressão linear
- regressão múltipla

Exemplo de modelo:

```text
atividade_fisica ~ competencia + idade + sexo
```

## Fase 3 — Crescimento e Maturação (Semanas 9–12)

**Artigo central:**  
Malina — Growth, Maturation and Physical Activity

**Pergunta científica:**

> Idade cronológica explica desempenho físico?

Modelo estatístico:

```text
desempenho ~ idade + maturacao + altura
```

**Dataset:**

growth dataset

**Tarefas Python:**

- regressão múltipla
- interpretação de coeficientes

## Fase 4 — Desenvolvimento Longitudinal (Semanas 13–16)

**Artigo central:**  
Telama (2009)

**Pergunta científica:**

> Crianças fisicamente ativas permanecem ativas na adolescência?

**Estatística aprendida:**

- correlação longitudinal
- regressão
- introdução a modelos mistos

**Dataset:**

longitudinal physical activity dataset

**Exercício:**

- correlacionar atividade em diferentes idades
- criar gráfico de trajetória

---

## 🧩 Projeto Final

Ao final do curso o estudante deverá produzir **3 análises completas em Python**.

### Projeto 1 — Competência Motora e Atividade Física

Baseado em:

Stodden 2008

Análise:

regressão entre competência motora e atividade física.

### Projeto 2 — Crescimento e Desempenho

Baseado em:

Malina

Análise:

regressão múltipla incluindo maturação biológica.

### Projeto 3 — Tracking de Atividade Física

Baseado em:

Telama

Análise:

relação longitudinal de atividade física.

---

## 🧠 Notebooks marimo implementados

Cada semana do cronograma agora possui um notebook marimo interativo correspondente.

- Semanas 1–4: fundamentos de estatística descritiva, percentis, correlação e regressão
- Semanas 5–8: competência motora, atividade física, comparação entre grupos e interpretação aplicada
- Semanas 9–12: crescimento, maturação, regressão múltipla e diagnóstico de modelos
- Semanas 13–16: análises longitudinais, trajetórias, introdução a modelos mistos e síntese para projeto final

Além dos notebooks, o repositório inclui datasets sintéticos educacionais em `data/` para que a experiência seja executável desde o primeiro clone do projeto.

---

## 🧱 Estrutura Recomendada de Cada Notebook

Cada notebook deve conter:

1. Introdução científica
2. Descrição do dataset
3. Estatística descritiva
4. Visualização
5. Modelo estatístico
6. Interpretação dos resultados
7. Discussão científica

---

## ✅ Resultado Esperado

Após completar este plano o estudante será capaz de:

- interpretar estatística em artigos de desenvolvimento motor
- aplicar regressões e análises em Python
- compreender estudos longitudinais
- analisar datasets de desenvolvimento humano
- estruturar um projeto de pesquisa

---

## 🚀 Objetivo Final

Preparar o estudante para:

- leitura crítica da literatura científica
- desenvolvimento de projeto de mestrado
- aplicação prática de estatística em Educação Física
