"""
Material para explicar cada release e comparar a evolução dos defeitos.

Gera em results/:
  por_release.md           uma seção por release, com a variação em relação à anterior
  comparativo_codeql.csv   alertas totais, de segurança e por mil linhas (KLOC)
  figures/codeql_por_kloc.png
O script mostra O QUE mudou. O POR QUÊ vem do changelog do jsoup (https://jsoup.org/news/).
"""
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"
FIG = RESULTS / "figures"
METRICS = ["wmc", "dit", "noc", "cbo", "lcom", "rfc", "loc"]


def short(release):
    return release.replace("jsoup-", "")


def delta(value, digits=2):
    if pd.isna(value) or value == 0:
        return "="
    return f"{value:+.{digits}f}"


def rule_counts(release):
    sarif = RESULTS / "codeql" / f"{release}.sarif"
    run = json.loads(sarif.read_text())["runs"][0]
    ids = [r["ruleId"] for r in run.get("results", [])]
    return pd.Series(ids, dtype="object").value_counts()


def build_comparison(ck, summary, releases):
    size = ck.groupby("release").agg(classes=("class", "count"), loc_total=("loc", "sum"))
    out = summary.join(size, on="release")
    out["alertas_por_kloc"] = out["total"] / (out["loc_total"] / 1000)
    out["delta_total"] = out["total"].diff()
    out["delta_por_kloc"] = out["alertas_por_kloc"].diff()
    out.to_csv(RESULTS / "comparativo_codeql.csv", index=False, float_format="%.3f")
    return out


def plot_per_kloc(comp, releases):
    fig, ax1 = plt.subplots(figsize=(12, 5))
    ax1.plot(comp["total"], marker="o", ms=3, color="tab:blue")
    ax1.set_ylabel("Alertas (absoluto)", color="tab:blue")
    ax2 = ax1.twinx()
    ax2.plot(comp["alertas_por_kloc"], marker="s", ms=3, color="tab:red")
    ax2.set_ylabel("Alertas por KLOC", color="tab:red")
    ax1.set_xticks(range(len(releases)))
    ax1.set_xticklabels([short(r) for r in releases], rotation=60, fontsize=7)
    ax1.grid(alpha=0.3)
    ax1.set_title("Alertas do CodeQL: absoluto vs. normalizado pelo tamanho")
    fig.tight_layout()
    fig.savefig(FIG / "codeql_por_kloc.png", dpi=150)
    plt.close(fig)


def release_section(i, r, comp, med, mean, rules, classes, releases):
    row, prev = comp.iloc[i], (releases[i - 1] if i else None)
    lines = [f"## {short(r)} ({row['date']})", ""]

    if prev is None:
        lines += ["Primeira release da janela: serve de base, sem comparação.", ""]
    d_cls = f" ({int(row['classes'] - comp.iloc[i-1]['classes']):+d})" if prev else ""
    d_loc = f" ({int(row['loc_total'] - comp.iloc[i-1]['loc_total']):+d})" if prev else ""
    lines += [f"**Tamanho:** {int(row['classes'])} classes{d_cls}, {int(row['loc_total'])} LOC{d_loc}", ""]

    lines += ["| Métrica | Mediana | Δ | Média | Δ |", "|---|---|---|---|---|"]
    for m in METRICS:
        dm = delta(med.loc[r, m] - med.loc[prev, m]) if prev else "-"
        da = delta(mean.loc[r, m] - mean.loc[prev, m]) if prev else "-"
        lines.append(f"| {m.upper()} | {med.loc[r, m]:.2f} | {dm} | {mean.loc[r, m]:.2f} | {da} |")
    lines.append("")

    lines += [f"**CodeQL:** {int(row['total'])} alertas ({int(row['security'])} de segurança), "
              f"{row['alertas_por_kloc']:.2f} por KLOC"
              + (f", variação {delta(row['delta_total'], 0)}" if prev else ""), ""]

    if prev:
        diff = rules[r].sub(rules[prev], fill_value=0)
        up, down = diff[diff > 0].nlargest(3), diff[diff < 0].nsmallest(3)
        if len(up):
            lines.append("- Regras que aumentaram: " + ", ".join(f"`{k}` (+{int(v)})" for k, v in up.items()))
        if len(down):
            lines.append("- Regras que diminuíram: " + ", ".join(f"`{k}` ({int(v)})" for k, v in down.items()))
        added, removed = sorted(classes[r] - classes[prev]), sorted(classes[prev] - classes[r])
        if added:
            lines.append(f"- Classes novas ({len(added)}): " + ", ".join(added[:5]) + (" ..." if len(added) > 5 else ""))
        if removed:
            lines.append(f"- Classes removidas ({len(removed)}): " + ", ".join(removed[:5]) + (" ..." if len(removed) > 5 else ""))
        lines.append("")

    lines += ["**Explicação (preencher com o changelog do jsoup):** ", "", "---", ""]
    return lines


def final_comparison(comp, med, releases):
    a, b = releases[0], releases[-1]
    lines = [f"## Comparativo final: {short(a)} -> {short(b)}", "",
             "| Indicador | Início | Fim | Variação |", "|---|---|---|---|"]
    for m in METRICS:
        x, y = med.loc[a, m], med.loc[b, m]
        var = f"{(y - x) / x * 100:+.1f}%" if x else "n/a (base 0)"
        lines.append(f"| {m.upper()} (mediana) | {x:.2f} | {y:.2f} | {var} |")
    for col, name in [("total", "Alertas totais"), ("alertas_por_kloc", "Alertas por KLOC"),
                      ("security", "Alertas de segurança")]:
        x, y = comp.iloc[0][col], comp.iloc[-1][col]
        var = f"{(y - x) / x * 100:+.1f}%" if x else "n/a"
        lines.append(f"| {name} | {x:.2f} | {y:.2f} | {var} |")
    return lines


def main():
    FIG.mkdir(parents=True, exist_ok=True)
    ck = pd.read_csv(RESULTS / "ck_classes.csv")
    summary = pd.read_csv(RESULTS / "codeql_summary.csv").sort_values("date").reset_index(drop=True)
    releases = summary["release"].tolist()

    comp = build_comparison(ck, summary, releases)
    plot_per_kloc(comp, releases)

    med = ck.groupby("release")[METRICS].median()
    mean = ck.groupby("release")[METRICS].mean()
    rules = {r: rule_counts(r) for r in releases}
    classes = ck.groupby("release")["class"].apply(set)

    lines = ["# Evolução release a release", "",
             f"Janela analisada: {short(releases[0])} a {short(releases[-1])} ({len(releases)} releases).", ""]
    for i, r in enumerate(releases):
        lines += release_section(i, r, comp, med, mean, rules, classes, releases)
    lines += final_comparison(comp, med, releases)

    (RESULTS / "por_release.md").write_text("\n".join(lines), encoding="utf-8")
    print("Gerados: results/por_release.md, results/comparativo_codeql.csv, figures/codeql_por_kloc.png")


if __name__ == "__main__":
    main()