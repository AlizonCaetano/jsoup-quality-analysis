"""
Estatística descritiva e gráficos a partir dos resultados do collect.py.

Gera em results/:
  ck_stats.csv        média, mediana, desvio, mín e máx de cada métrica por release
  codeql_stats.csv    estatística descritiva dos alertas ao longo das releases
  codeql_rules.csv    quantidade de alertas por regra em cada release
  figures/*.png       gráficos de evolução
"""
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # gera imagens sem precisar de janela
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"
FIG = RESULTS / "figures"
METRICS = ["wmc", "dit", "noc", "cbo", "lcom", "rfc", "loc"]
LABELS = {
    "wmc": "WMC (complexidade)", "dit": "DIT (profundidade de herança)",
    "noc": "NOC (subclasses diretas)", "cbo": "CBO (acoplamento)",
    "lcom": "LCOM (falta de coesão)", "rfc": "RFC (resposta da classe)",
    "loc": "LOC (linhas por classe)",
}


def short(release):
    return release.replace("jsoup-", "")


def setup_xaxis(ax, releases):
    ax.set_xticks(range(len(releases)))
    ax.set_xticklabels([short(r) for r in releases], rotation=60, fontsize=7)
    ax.grid(alpha=0.3)


def ck_stats(ck, releases):
    """Uma linha por release, com as estatísticas de cada métrica."""
    grouped = ck.groupby("release")
    stats = grouped[METRICS].agg(["mean", "median", "std", "min", "max"])
    stats.columns = [f"{m}_{s}" for m, s in stats.columns]
    size = grouped.agg(date=("date", "first"), classes=("class", "count"), loc_total=("loc", "sum"))
    out = size.join(stats).reindex(releases).reset_index()
    out.to_csv(RESULTS / "ck_stats.csv", index=False, float_format="%.3f")
    return out


def plot_ck_evolution(stats, releases):
    """Média e mediana de cada métrica ao longo das releases."""
    fig, axes = plt.subplots(4, 2, figsize=(14, 16))
    for ax, m in zip(axes.flat, METRICS):
        ax.plot(stats[f"{m}_mean"], marker="o", ms=3, label="média")
        ax.plot(stats[f"{m}_median"], marker="s", ms=3, label="mediana")
        ax.set_title(LABELS[m])
        setup_xaxis(ax, releases)
        ax.legend(fontsize=8)
    axes.flat[-1].axis("off")
    fig.tight_layout()
    fig.savefig(FIG / "ck_evolucao.png", dpi=150)
    plt.close(fig)


def plot_ck_boxplots(ck, releases):
    """Distribuição de cada métrica por release (outliers ocultos para legibilidade)."""
    fig, axes = plt.subplots(len(METRICS), 1, figsize=(14, 3.2 * len(METRICS)))
    for ax, m in zip(axes, METRICS):
        data = [ck.loc[ck["release"] == r, m].dropna() for r in releases]
        ax.boxplot(data, positions=range(len(releases)), showfliers=False)
        ax.set_title(LABELS[m])
        setup_xaxis(ax, releases)
    fig.tight_layout()
    fig.savefig(FIG / "ck_boxplots.png", dpi=150)
    plt.close(fig)


def plot_size(stats, releases):
    """Tamanho do projeto: número de classes e LOC total."""
    fig, ax1 = plt.subplots(figsize=(12, 5))
    ax1.plot(stats["classes"], marker="o", ms=3, color="tab:blue")
    ax1.set_ylabel("Número de classes", color="tab:blue")
    ax2 = ax1.twinx()
    ax2.plot(stats["loc_total"], marker="s", ms=3, color="tab:orange")
    ax2.set_ylabel("LOC total", color="tab:orange")
    setup_xaxis(ax1, releases)
    ax1.set_title("Tamanho do projeto por release")
    fig.tight_layout()
    fig.savefig(FIG / "tamanho_projeto.png", dpi=150)
    plt.close(fig)


def codeql_analysis(summary, releases):
    """Estatística dos alertas, gráfico de evolução e contagem por regra."""
    summary[["total", "security", "general"]].describe().to_csv(
        RESULTS / "codeql_stats.csv", float_format="%.3f")

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(summary["total"], marker="o", ms=3, label="total")
    ax.plot(summary["general"], marker="s", ms=3, label="gerais (qualidade)")
    ax.plot(summary["security"], marker="^", ms=4, label="segurança")
    ax.set_title("Alertas do CodeQL por release")
    ax.set_ylabel("Quantidade de alertas")
    setup_xaxis(ax, releases)
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIG / "codeql_alertas.png", dpi=150)
    plt.close(fig)

    rows = []
    for f in (RESULTS / "codeql").glob("*.sarif"):
        run = json.loads(f.read_text())["runs"][0]
        rows += [{"release": f.stem, "rule": r["ruleId"]} for r in run.get("results", [])]
    rules = (pd.DataFrame(rows)
             .pivot_table(index="rule", columns="release", aggfunc="size", fill_value=0)
             .reindex(columns=releases, fill_value=0))
    rules["variacao"] = rules[releases[-1]] - rules[releases[0]]
    rules = rules.sort_values("variacao")
    rules.to_csv(RESULTS / "codeql_rules.csv")
    return rules


def main():
    FIG.mkdir(parents=True, exist_ok=True)
    ck = pd.read_csv(RESULTS / "ck_classes.csv")
    summary = pd.read_csv(RESULTS / "codeql_summary.csv").sort_values("date").reset_index(drop=True)
    releases = summary["release"].tolist()  # ordem cronológica

    stats = ck_stats(ck, releases)
    plot_ck_evolution(stats, releases)
    plot_ck_boxplots(ck, releases)
    plot_size(stats, releases)
    rules = codeql_analysis(summary, releases)

    first, last = stats.iloc[0], stats.iloc[-1]
    print(f"Média das métricas: {short(releases[0])} -> {short(releases[-1])}")
    for m in METRICS:
        a, b = first[f"{m}_mean"], last[f"{m}_mean"]
        print(f"  {m.upper():5} {a:8.2f} -> {b:8.2f}  ({(b - a) / a * 100:+.1f}%)")

    print("\nRegras do CodeQL com maior redução de alertas:")
    print(rules[[releases[0], releases[-1], "variacao"]].head(10).to_string())

    print("\nAlertas de segurança:")
    sec = summary.loc[summary["security"] > 0, "release"].tolist()
    print(f"  presentes em: {', '.join(short(r) for r in sec)}")
    print("\nArquivos gerados em results/ e results/figures/")


if __name__ == "__main__":
    main()