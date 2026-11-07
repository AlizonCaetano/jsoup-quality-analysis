# Análise da qualidade do código do jsoup

Scripts e resultados do trabalho da disciplina QUA, Qualidade de Software (Engenharia de Software). O trabalho mede a evolução da qualidade do jsoup em 20 releases, da 1.14.3 à 1.23.2, com as métricas CK e com os alertas do CodeQL.

Autor: Alison Caetano

## O que tem aqui

- `setup.sh`: instala JDK 17, Maven, CK e CodeQL (em `tools/`) e cria o ambiente Python (`.venv/`).
- `collect.py`: para cada uma das 20 releases, faz o checkout da tag com o PyDriller e roda o CK e o CodeQL sobre `src/main/java`. Gera `results/ck_classes.csv` e `results/codeql_summary.csv`.
- `analyze.py`: estatística descritiva e gráficos. Gera `results/ck_stats.csv`, `results/codeql_stats.csv`, `results/codeql_rules.csv` e as figuras em `results/figures/`.
- `per_release.py`: variação release a release (`results/por_release.md`), alertas por mil linhas (`results/comparativo_codeql.csv`) e a figura de alertas por KLOC.

## Como reproduzir

```bash
./setup.sh
.venv/bin/python collect.py      # demora, e pula releases já processadas
.venv/bin/python analyze.py
.venv/bin/python per_release.py
```

Testado em Ubuntu (WSL), com OpenJDK 17.0.20, Python 3.10.12 e Maven.

## Versões das ferramentas

- CodeQL CLI 2.27.1
- CK, commit 8a1ef91 (29/04/2026): https://github.com/mauricioaniche/ck
- PyDriller, instalado pelo `requirements.txt`

## Decisões de metodologia

- Releases: as 20 tags mais recentes do jsoup com prefixo `jsoup-`, ordenadas pela data do commit da tag, de `jsoup-1.14.3` a `jsoup-1.23.2`.
- Código analisado: só `src/main/java`, sem os testes.
- CK: uma linha por classe, incluindo classes internas e anônimas. O LCOM é a versão original da ferramenta.
- CodeQL: suíte `java-security-and-quality`, sem compilar o projeto (`--build-mode=none`), com 2 threads e 4 GB de memória. Um alerta é de segurança quando a regra tem a tag `security`.

## Resultados

Tudo fica em `results/`. As pastas `results/ck` e `results/codeql` também guardam as saídas brutas de 10 releases mais antigas (1.10.2 a 1.14.2), de uma coleta preliminar com 30 releases. Elas não entram nas tabelas nem nas figuras.

## Uso de IA

Os scripts foram escritos com ajuda do Claude (Anthropic). O artigo do trabalho descreve o que foi feito pela IA e o que foi feito pelo autor.
