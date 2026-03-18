from __future__ import annotations

import csv
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
random.seed(42)


def clip(value, low, high):
    return max(low, min(high, value))


def write_csv(filename, fieldnames, rows):
    with open(DATA / filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

rows = []
for idx in range(1, 241):
    sexo = random.choice(["Feminino", "Masculino"])
    idade = random.randint(6, 10)
    correr = clip(random.gauss(8 + 0.45 * idade, 1.3), 3, 20)
    saltar = clip(random.gauss(7 + 0.40 * idade, 1.1), 3, 20)
    chutar = clip(random.gauss(6.5 + 0.35 * idade, 1.4), 2, 20)
    arremessar = clip(random.gauss(6 + 0.50 * idade + (0.8 if sexo == "Masculino" else 0), 1.6), 2, 22)
    atividade = clip(random.gauss(45 + 1.8 * idade, 8), 15, 95)
    total = correr + saltar + chutar + arremessar
    rows.append({
        "id": idx, "idade": idade, "sexo": sexo,
        "correr": round(correr, 1), "saltar": round(saltar, 1), "chutar": round(chutar, 1),
        "arremessar": round(arremessar, 1), "atividade_fisica_min_semana": round(atividade, 1),
        "escore_motor_total": round(total, 1),
    })
write_csv("tgmd_dataset.csv", list(rows[0].keys()), rows)

rows = []
for idx in range(1, 261):
    sexo = random.choice(["Feminino", "Masculino"])
    idade = random.randint(7, 14)
    competencia = clip(random.gauss(50 + 2.6 * idade, 9), 20, 100)
    aptidao = clip(20 + 0.55 * competencia + random.gauss(0, 8), 10, 95)
    imc = clip(random.gauss(19 + 0.22 * idade - 0.05 * competencia, 2.5), 14, 32)
    atividade = clip(35 + 0.75 * competencia + 1.2 * idade - 0.9 * imc + random.gauss(0, 10), 10, 120)
    percepcao = clip(2.2 + 0.03 * competencia + random.gauss(0, 0.4), 1, 5)
    rows.append({
        "id": idx, "idade": idade, "sexo": sexo, "competencia_motora": round(competencia, 1),
        "atividade_fisica": round(atividade, 1), "aptidao_fisica": round(aptidao, 1),
        "imc": round(imc, 1), "percepcao_competencia": round(percepcao, 2),
    })
write_csv("motor_competence_dataset.csv", list(rows[0].keys()), rows)

rows = []
for idx in range(1, 221):
    sexo = random.choice(["Feminino", "Masculino"])
    idade = random.randint(10, 17)
    idade_maturacional = clip(random.gauss(idade, 0.9), 9, 18)
    altura = clip(random.gauss(120 + 5.6 * idade, 6), 125, 195)
    massa = clip(random.gauss(18 + 2.7 * idade, 5), 25, 100)
    forca = clip(10 + 2.1 * idade + idade_maturacional + 0.14 * altura + random.gauss(0, 6), 20, 110)
    sprint = clip(8.5 - 0.11 * idade - 0.05 * idade_maturacional + random.gauss(0, 0.35), 5.5, 9.5)
    rows.append({
        "id": idx, "idade": idade, "sexo": sexo, "idade_maturacional": round(idade_maturacional, 2),
        "altura_cm": round(altura, 1), "massa_kg": round(massa, 1),
        "forca_membros_inferiores": round(forca, 1), "sprint_20m_s": round(sprint, 2),
    })
write_csv("growth_dataset.csv", list(rows[0].keys()), rows)

rows = []
for idx in range(1, 181):
    sexo = random.choice(["Feminino", "Masculino"])
    participa = random.choices(["Não", "Sim"], weights=[0.45, 0.55])[0]
    atividade_8 = clip(random.gauss(55, 12), 20, 100)
    atividade_10 = clip(0.72 * atividade_8 + random.gauss(14, 8), 15, 100)
    atividade_12 = clip(0.76 * atividade_10 + random.gauss(12, 9), 10, 100)
    atividade_14 = clip(0.80 * atividade_12 + random.gauss(8, 9), 5, 100)
    rows.append({
        "id": idx, "sexo": sexo, "participa_esporte": participa,
        "atividade_8_anos": round(atividade_8, 1), "atividade_10_anos": round(atividade_10, 1),
        "atividade_12_anos": round(atividade_12, 1), "atividade_14_anos": round(atividade_14, 1),
    })
write_csv("longitudinal_activity_dataset.csv", list(rows[0].keys()), rows)

rows = []
for idx in range(1, 201):
    grupo = random.choice(["Foco Interno", "Foco Externo"])
    tentativa_1 = clip(random.gauss(48, 7), 25, 70)
    bonus = 8 if grupo == "Foco Externo" else 4
    tentativa_5 = clip(tentativa_1 + bonus + random.gauss(0, 3), 30, 90)
    retencao = clip(tentativa_5 - random.gauss(4, 3) + (2 if grupo == "Foco Externo" else 0), 25, 90)
    transferencia = clip(retencao + random.gauss(0, 4), 20, 90)
    rows.append({
        "id": idx, "grupo": grupo, "tentativa_1": round(tentativa_1, 1), "tentativa_5": round(tentativa_5, 1),
        "retencao": round(retencao, 1), "transferencia": round(transferencia, 1),
    })
write_csv("motor_learning_experiment.csv", list(rows[0].keys()), rows)

print("Datasets gerados em", DATA)
