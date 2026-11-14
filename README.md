# Análise da qualidade do código do jsoup

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24210245.svg)](https://doi.org/10.5281/zenodo.24210245)

Trabalho da disciplina de Qualidade de Software (QUA) do curso de Engenharia de Software da UDESC CEAVI, com o Prof. Paulo Roberto Farah.

A gente mediu como a qualidade do código do [jsoup](https://github.com/jhy/jsoup) evoluiu em 20 releases, da 1.14.3, de setembro de 2021, até a 1.23.2, de agosto de 2026. A análise usa as métricas CK, os alertas gerais e de segurança do CodeQL e a revisão do CodeRabbit em três pull requests.

**Autores**

- Pedro Henrique Uessler
- Eduardo de Souza Riesemberg Bastos
- Alison Natan Caetano

## Resultados em poucas linhas

- O projeto foi de 247 para 299 classes e de 17,1 mil para 22,1 mil linhas de código.
- A média de quase todas as métricas CK subiu, com destaque para o LCOM1, que cresceu 32%. As medianas ficaram paradas, então a mudança está concentrada em poucas classes grandes.
- Os alertas do CodeQL caíram de 257 para 38, mas 232 deles eram da regra que aponta a falta de `@Override`. Sem essa regra, os alertas subiram de 25 para 38.
- Dos 38 alertas da última release, três eram defeitos reais e viraram pull requests no fork, um deles o único alerta de segurança da janela.

## Pull requests

Os pull requests foram abertos no [fork do jsoup](https://github.com/AlizonCaetano/jsoup), porque o guia de contribuição do projeto original não aceita código feito com ajuda de IA.

| PR                                                  | Defeito corrigido                                                  | Regra do CodeQL                    |
| --------------------------------------------------- | ------------------------------------------------------------------ | ---------------------------------- |
| [#1](https://github.com/AlizonCaetano/jsoup/pull/1) | Trava do request que não era liberada quando uma validação falhava | `unreleased-lock`                  |
| [#2](https://github.com/AlizonCaetano/jsoup/pull/2) | BOM não detectado quando o stream devolve menos bytes que o pedido | `ignored-error-status-of-call`     |
| [#3](https://github.com/AlizonCaetano/jsoup/pull/3) | Seletor `nth-child` com espaço em volta do sinal dava erro         | `uncaught-number-format-exception` |

## Estrutura do repositório

| Arquivo          | O que faz                                                                                   |
| ---------------- | ------------------------------------------------------------------------------------------- |
| `setup.sh`       | Instala JDK 17, Maven, CK e CodeQL em `tools/` e cria o ambiente Python em `.venv/`         |
| `collect.py`     | Faz o checkout de cada release com o PyDriller e roda o CK e o CodeQL sobre `src/main/java` |
| `analyze.py`     | Calcula a estatística descritiva e conta os alertas por regra                               |
| `per_release.py` | Gera a variação release a release e os alertas por mil linhas                               |
| `results/`       | Dados gerados pelos scripts e os gráficos do artigo                                         |

### Dados em `results/`

| Arquivo                                       | Conteúdo                                                                   |
| --------------------------------------------- | -------------------------------------------------------------------------- |
| `ck_classes.csv`                              | Métricas CK de cada classe em cada release                                 |
| `ck_stats.csv`                                | Média, mediana, desvio padrão, mínimo e máximo de cada métrica por release |
| `codeql_summary.csv`                          | Alertas gerais, de segurança e total por release                           |
| `codeql_rules.csv`                            | Alertas de cada regra do CodeQL por release                                |
| `codeql_stats.csv` e `comparativo_codeql.csv` | Resumo dos alertas e alertas por mil linhas                                |
| `por_release.md`                              | Variação de cada métrica de uma release para a outra                       |
| `figures/`                                    | Os 10 gráficos usados no artigo                                            |

As pastas `results/ck` e `results/codeql` guardam também as saídas brutas de 10 releases mais antigas, da 1.10.2 à 1.14.2, que sobraram de uma coleta inicial com 30 releases. Elas não entram nas tabelas nem nos gráficos.

## Como reproduzir

```bash
./setup.sh
.venv/bin/python collect.py
.venv/bin/python analyze.py
.venv/bin/python per_release.py
```

A coleta demora, e o `collect.py` pula as releases que já foram processadas. Tudo foi testado em Ubuntu no WSL, com OpenJDK 17.0.20, Python 3.10.12 e Maven.

## Ferramentas e decisões

- **CK**, commit `8a1ef91`, de 29/04/2026, [mauricioaniche/ck](https://github.com/mauricioaniche/ck). Gera uma linha por classe, contando classes internas e anônimas. A métrica LCOM do CK é a versão original, o LCOM1.
- **CodeQL CLI 2.27.1**, com a suíte `java-security-and-quality`, sem compilar o projeto (`--build-mode=none`). Um alerta conta como de segurança quando a regra tem a tag `security`.
- **PyDriller**, instalado pelo `requirements.txt`.
- **Releases**, as 20 tags mais recentes com prefixo `jsoup-`, ordenadas pela data do commit da tag.
- **Código analisado**, só `src/main/java`, sem os testes.

## Uso de IA

Os scripts e as correções dos pull requests foram escritos com ajuda do Claude, da Anthropic. Todos os comandos foram rodados e conferidos pelos autores.

## Como citar

CAETANO, A. N. **jsoup-quality-analysis**: análise da qualidade do código do jsoup. Versão 1.1.0. Zenodo, 2026. DOI: [10.5281/zenodo.24210245](https://doi.org/10.5281/zenodo.24210245).
