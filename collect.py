"""
Coleta métricas CK e alertas CodeQL para as últimas N releases do jsoup.

Fluxo por release:
  1. checkout da tag (PyDriller)
  2. CK em src/main/java  -> results/ck/<tag>/class.csv
  3. CodeQL em src/main/java -> results/codeql/<tag>.sarif
Releases já processadas são puladas, então dá para interromper e retomar.
"""
import json
import subprocess
from pathlib import Path

import pandas as pd
from pydriller import Git

ROOT = Path(__file__).resolve().parent
TOOLS, WORK, RESULTS = ROOT / "tools", ROOT / "work", ROOT / "results"
REPO_URL = "https://github.com/jhy/jsoup.git"
REPO_DIR = WORK / "jsoup"
N_RELEASES = 30

CK_JAR = TOOLS / "ck.jar"
CODEQL = TOOLS / "codeql" / "codeql"
SUITE = "codeql/java-queries:codeql-suites/java-security-and-quality.qls"
METRICS = ["wmc", "dit", "noc", "cbo", "lcom", "rfc", "loc"]


def run(cmd):
    subprocess.run([str(c) for c in cmd], check=True, stdout=subprocess.DEVNULL)


def list_releases(git):
    """Tags de release ordenadas por data; fica com as N mais recentes."""
    tags = [t for t in git.repo.tags if t.name.startswith("jsoup-")]
    tags.sort(key=lambda t: t.commit.committed_datetime)
    return tags[-N_RELEASES:]


def run_ck(src, tag):
    out = RESULTS / "ck" / tag
    if not (out / "class.csv").exists():
        out.mkdir(parents=True, exist_ok=True)
        # args: projeto, usar jars, arquivos por partição, métricas de variáveis, pasta de saída
        run(["java", "-jar", CK_JAR, src, "false", "0", "false", f"{out}/"])
    df = pd.read_csv(out / "class.csv")
    return df[["class"] + METRICS]


def run_codeql(src, tag):
    sarif = RESULTS / "codeql" / f"{tag}.sarif"
    if not sarif.exists():
        sarif.parent.mkdir(parents=True, exist_ok=True)
        db = WORK / "codeql-db"
        # build-mode=none: analisa o código sem compilar (evita problemas com releases antigas)
        run([CODEQL, "database", "create", db, "--language=java",
             "--build-mode=none", f"--source-root={src}", "--overwrite"])
        run([CODEQL, "database", "analyze", db, SUITE, "--threads=0",
             "--format=sarif-latest", f"--output={sarif}"])
    return count_alerts(sarif)


def count_alerts(sarif):
    """Separa alertas de segurança (regra com tag 'security') dos gerais."""
    run_ = json.loads(sarif.read_text())["runs"][0]
    components = [run_["tool"]["driver"]] + run_["tool"].get("extensions", [])
    tags = {r["id"]: r.get("properties", {}).get("tags", [])
            for c in components for r in c.get("rules", [])}

    counts = {"total": 0, "security": 0, "general": 0, "error": 0, "warning": 0, "note": 0}
    for res in run_.get("results", []):
        counts["total"] += 1
        counts["security" if "security" in tags.get(res["ruleId"], []) else "general"] += 1
        counts[res.get("level", "warning")] += 1
    return counts


def main():
    WORK.mkdir(exist_ok=True)
    if not REPO_DIR.exists():
        run(["git", "clone", REPO_URL, REPO_DIR])

    git = Git(str(REPO_DIR))
    ck_rows, codeql_rows = [], []

    try:
        for i, tag in enumerate(list_releases(git), 1):
            print(f"[{i}/{N_RELEASES}] {tag.name}")
            git.checkout(tag.commit.hexsha)
            src = REPO_DIR / "src" / "main" / "java"
            if not src.exists():
                print("  sem src/main/java, pulando")
                continue

            date = tag.commit.committed_datetime.date().isoformat()

            ck = run_ck(src, tag.name)
            ck.insert(0, "release", tag.name)
            ck.insert(1, "date", date)
            ck_rows.append(ck)

            codeql_rows.append({"release": tag.name, "date": date, **run_codeql(src, tag.name)})
    finally:
        git.reset()  # volta o clone para a branch principal

    pd.concat(ck_rows).to_csv(RESULTS / "ck_classes.csv", index=False)
    pd.DataFrame(codeql_rows).to_csv(RESULTS / "codeql_summary.csv", index=False)
    print("Pronto: results/ck_classes.csv e results/codeql_summary.csv")


if __name__ == "__main__":
    main()
