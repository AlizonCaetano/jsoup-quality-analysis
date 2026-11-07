# Evolução release a release

Janela analisada: 1.14.3 a 1.23.2 (20 releases).

## 1.14.3 (2021-09-30)

Primeira release da janela: serve de base, sem comparação.

**Tamanho:** 247 classes, 17083 LOC

| Métrica | Mediana | Δ | Média | Δ |
|---|---|---|---|---|
| WMC | 6.00 | - | 15.89 | - |
| DIT | 1.00 | - | 2.00 | - |
| NOC | 0.00 | - | 0.36 | - |
| CBO | 3.00 | - | 5.03 | - |
| LCOM | 0.00 | - | 75.29 | - |
| RFC | 6.00 | - | 12.19 | - |
| LOC | 22.00 | - | 69.16 | - |

**CodeQL:** 257 alertas (0 de segurança), 15.04 por KLOC

**Explicação (preencher com o changelog do jsoup):** 

---

## 1.15.1 (2022-05-15)

**Tamanho:** 250 classes (+3), 17207 LOC (+124)

| Métrica | Mediana | Δ | Média | Δ |
|---|---|---|---|---|
| WMC | 5.50 | -0.50 | 15.88 | -0.01 |
| DIT | 1.00 | = | 2.01 | +0.02 |
| NOC | 0.00 | = | 0.39 | +0.02 |
| CBO | 3.00 | = | 5.01 | -0.02 |
| LCOM | 0.00 | = | 76.88 | +1.60 |
| RFC | 5.00 | -1.00 | 12.12 | -0.08 |
| LOC | 22.00 | = | 68.83 | -0.33 |

**CodeQL:** 245 alertas (0 de segurança), 14.24 por KLOC, variação -12

- Regras que aumentaram: `java/internal-representation-exposure` (+1)
- Regras que diminuíram: `java/missing-override-annotation` (-11), `java/missing-clone-method` (-1), `java/unused-parameter` (-1)
- Classes novas (5): org.jsoup.helper.Consumer, org.jsoup.select.Evaluator$ContainsWholeOwnText, org.jsoup.select.Evaluator$ContainsWholeText, org.jsoup.select.Evaluator$MatchesWholeOwnText, org.jsoup.select.Evaluator$MatchesWholeText
- Classes removidas (2): org.jsoup.nodes.Element$Anonymous2, org.jsoup.safety.Whitelist

**Explicação (preencher com o changelog do jsoup):** 

---

## 1.15.2 (2022-07-04)

**Tamanho:** 252 classes (+2), 17509 LOC (+302)

| Métrica | Mediana | Δ | Média | Δ |
|---|---|---|---|---|
| WMC | 6.00 | +0.50 | 16.08 | +0.20 |
| DIT | 1.00 | = | 2.00 | -0.01 |
| NOC | 0.00 | = | 0.38 | -0.00 |
| CBO | 3.00 | = | 5.03 | +0.02 |
| LCOM | 0.00 | = | 80.38 | +3.50 |
| RFC | 5.00 | = | 12.20 | +0.09 |
| LOC | 22.00 | = | 69.48 | +0.65 |

**CodeQL:** 246 alertas (0 de segurança), 14.05 por KLOC, variação +1

- Regras que aumentaram: `java/missing-case-in-switch` (+1)
- Classes novas (2): org.jsoup.nodes.Range, org.jsoup.nodes.Range$Position

**Explicação (preencher com o changelog do jsoup):** 

---

## 1.15.3 (2022-08-24)

**Tamanho:** 253 classes (+1), 17547 LOC (+38)

| Métrica | Mediana | Δ | Média | Δ |
|---|---|---|---|---|
| WMC | 6.00 | = | 16.08 | -0.00 |
| DIT | 1.00 | = | 2.02 | +0.01 |
| NOC | 0.00 | = | 0.38 | -0.00 |
| CBO | 3.00 | = | 5.02 | -0.00 |
| LCOM | 0.00 | = | 80.30 | -0.08 |
| RFC | 5.00 | = | 12.24 | +0.03 |
| LOC | 22.00 | = | 69.36 | -0.12 |

**CodeQL:** 246 alertas (0 de segurança), 14.02 por KLOC, variação =

- Classes novas (1): org.jsoup.helper.ValidationException

**Explicação (preencher com o changelog do jsoup):** 

---

## 1.15.4 (2023-02-18)

**Tamanho:** 252 classes (-1), 17579 LOC (+32)

| Métrica | Mediana | Δ | Média | Δ |
|---|---|---|---|---|
| WMC | 6.00 | = | 16.17 | +0.09 |
| DIT | 1.00 | = | 2.02 | +0.00 |
| NOC | 0.00 | = | 0.38 | +0.00 |
| CBO | 3.00 | = | 5.04 | +0.01 |
| LCOM | 0.00 | = | 81.59 | +1.29 |
| RFC | 5.50 | +0.50 | 12.37 | +0.13 |
| LOC | 22.00 | = | 69.76 | +0.40 |

**CodeQL:** 237 alertas (0 de segurança), 13.48 por KLOC, variação -9

- Regras que aumentaram: `java/confusing-method-signature` (+2)
- Regras que diminuíram: `java/missing-override-annotation` (-11)
- Classes removidas (1): org.jsoup.select.Collector$Accumulator

**Explicação (preencher com o changelog do jsoup):** 

---

## 1.16.1 (2023-04-29)

**Tamanho:** 253 classes (+1), 17661 LOC (+82)

| Métrica | Mediana | Δ | Média | Δ |
|---|---|---|---|---|
| WMC | 6.00 | = | 16.24 | +0.07 |
| DIT | 1.00 | = | 2.02 | -0.00 |
| NOC | 0.00 | = | 0.38 | -0.00 |
| CBO | 3.00 | = | 5.05 | +0.02 |
| LCOM | 0.00 | = | 82.58 | +1.00 |
| RFC | 6.00 | +0.50 | 12.36 | -0.00 |
| LOC | 22.00 | = | 69.81 | +0.05 |

**CodeQL:** 150 alertas (0 de segurança), 8.49 por KLOC, variação -87

- Regras que diminuíram: `java/missing-override-annotation` (-84), `java/confusing-method-signature` (-2), `java/internal-representation-exposure` (-1)
- Classes novas (1): org.jsoup.helper.UrlBuilder

**Explicação (preencher com o changelog do jsoup):** 

---

## 1.16.2 (2023-10-20)

**Tamanho:** 252 classes (-1), 18155 LOC (+494)

| Métrica | Mediana | Δ | Média | Δ |
|---|---|---|---|---|
| WMC | 6.00 | = | 16.77 | +0.52 |
| DIT | 1.00 | = | 2.03 | +0.02 |
| NOC | 0.00 | = | 0.39 | +0.01 |
| CBO | 3.00 | = | 5.12 | +0.06 |
| LCOM | 0.00 | = | 86.71 | +4.13 |
| RFC | 6.00 | = | 12.73 | +0.36 |
| LOC | 23.00 | +1.00 | 72.04 | +2.24 |

**CodeQL:** 151 alertas (0 de segurança), 8.32 por KLOC, variação +1

- Regras que aumentaram: `java/class-name-matches-super-class` (+1)
- Classes novas (2): org.jsoup.nodes.Element$TextAccumulator, org.jsoup.select.StructuralEvaluator$ImmediateParentRun
- Classes removidas (3): org.jsoup.helper.Consumer, org.jsoup.internal.StringUtil$Anonymous1, org.jsoup.nodes.Element$Anonymous1

**Explicação (preencher com o changelog do jsoup):** 

---

## 1.17.1 (2023-11-27)

**Tamanho:** 261 classes (+9), 18703 LOC (+548)

| Métrica | Mediana | Δ | Média | Δ |
|---|---|---|---|---|
| WMC | 6.00 | = | 16.75 | -0.02 |
| DIT | 1.00 | = | 2.02 | -0.01 |
| NOC | 0.00 | = | 0.39 | -0.01 |
| CBO | 3.00 | = | 5.05 | -0.07 |
| LCOM | 0.00 | = | 86.48 | -0.23 |
| RFC | 6.00 | = | 12.73 | +0.01 |
| LOC | 23.00 | = | 71.66 | -0.38 |

**CodeQL:** 56 alertas (0 de segurança), 2.99 por KLOC, variação -95

- Regras que aumentaram: `java/unused-parameter` (+6), `java/non-sync-override` (+2)
- Regras que diminuíram: `java/missing-override-annotation` (-103)
- Classes novas (10): org.jsoup.helper.AuthenticationHandler, org.jsoup.helper.AuthenticationHandler$AuthShim, org.jsoup.helper.AuthenticationHandler$GlobalHandler, org.jsoup.helper.RequestAuthenticator, org.jsoup.helper.RequestAuthenticator$Context ...
- Classes removidas (1): org.jsoup.select.Collector$FirstFinder

**Explicação (preencher com o changelog do jsoup):** 

---

## 1.17.2 (2023-12-29)

**Tamanho:** 261 classes (+0), 18743 LOC (+40)

| Métrica | Mediana | Δ | Média | Δ |
|---|---|---|---|---|
| WMC | 6.00 | = | 16.78 | +0.03 |
| DIT | 1.00 | = | 2.02 | = |
| NOC | 0.00 | = | 0.39 | = |
| CBO | 3.00 | = | 5.08 | +0.03 |
| LCOM | 0.00 | = | 87.78 | +1.30 |
| RFC | 6.00 | = | 12.81 | +0.08 |
| LOC | 23.00 | = | 71.81 | +0.15 |

**CodeQL:** 55 alertas (0 de segurança), 2.93 por KLOC, variação -1

- Regras que diminuíram: `java/missing-override-annotation` (-1)

**Explicação (preencher com o changelog do jsoup):** 

---

## 1.18.1 (2024-07-10)

**Tamanho:** 265 classes (+4), 19083 LOC (+340)

| Métrica | Mediana | Δ | Média | Δ |
|---|---|---|---|---|
| WMC | 6.00 | = | 16.83 | +0.06 |
| DIT | 1.00 | = | 1.99 | -0.03 |
| NOC | 0.00 | = | 0.38 | -0.01 |
| CBO | 3.00 | = | 5.15 | +0.08 |
| LCOM | 0.00 | = | 88.40 | +0.61 |
| RFC | 6.00 | = | 12.89 | +0.08 |
| LOC | 23.00 | = | 72.01 | +0.20 |

**CodeQL:** 50 alertas (0 de segurança), 2.62 por KLOC, variação -5

- Regras que aumentaram: `java/input-resource-leak` (+1)
- Regras que diminuíram: `java/unused-parameter` (-3), `java/non-sync-override` (-2), `java/missing-override-annotation` (-1)
- Classes novas (6): org.jsoup.Progress, org.jsoup.helper.DataUtil$CharsetDoc, org.jsoup.internal.Functions, org.jsoup.parser.StreamParser, org.jsoup.parser.StreamParser$ElementIterator ...
- Classes removidas (2): org.jsoup.internal.ConstrainableInputStream, org.jsoup.select.StructuralEvaluator$ImmediateParent

**Explicação (preencher com o changelog do jsoup):** 

---

## 1.18.2 (2024-11-27)

**Tamanho:** 266 classes (+1), 19247 LOC (+164)

| Métrica | Mediana | Δ | Média | Δ |
|---|---|---|---|---|
| WMC | 6.00 | = | 17.03 | +0.20 |
| DIT | 1.00 | = | 1.99 | +0.00 |
| NOC | 0.00 | = | 0.38 | -0.00 |
| CBO | 3.00 | = | 5.23 | +0.07 |
| LCOM | 0.00 | = | 88.61 | +0.21 |
| RFC | 6.00 | = | 13.03 | +0.14 |
| LOC | 23.00 | = | 72.36 | +0.35 |

**CodeQL:** 40 alertas (0 de segurança), 2.08 por KLOC, variação -10

- Regras que aumentaram: `java/ignored-error-status-of-call` (+2), `java/non-sync-override` (+2), `java/unused-parameter` (+2)
- Regras que diminuíram: `java/missing-override-annotation` (-15), `java/missing-case-in-switch` (-1)
- Classes novas (2): org.jsoup.internal.SimpleBufferedInput, org.jsoup.internal.SoftPool
- Classes removidas (1): org.jsoup.helper.DataUtil$BomCharset

**Explicação (preencher com o changelog do jsoup):** 

---

## 1.18.3 (2024-12-02)

**Tamanho:** 266 classes (+0), 19247 LOC (+0)

| Métrica | Mediana | Δ | Média | Δ |
|---|---|---|---|---|
| WMC | 6.00 | = | 17.05 | +0.02 |
| DIT | 1.00 | = | 1.99 | = |
| NOC | 0.00 | = | 0.38 | = |
| CBO | 3.00 | = | 5.23 | = |
| LCOM | 0.00 | = | 88.61 | = |
| RFC | 6.00 | = | 13.03 | = |
| LOC | 23.00 | = | 72.36 | = |

**CodeQL:** 40 alertas (0 de segurança), 2.08 por KLOC, variação =


**Explicação (preencher com o changelog do jsoup):** 

---

## 1.19.1 (2025-03-04)

**Tamanho:** 270 classes (+4), 19483 LOC (+236)

| Métrica | Mediana | Δ | Média | Δ |
|---|---|---|---|---|
| WMC | 6.00 | = | 17.08 | +0.03 |
| DIT | 1.00 | = | 1.98 | -0.01 |
| NOC | 0.00 | = | 0.38 | -0.00 |
| CBO | 3.00 | = | 5.29 | +0.06 |
| LCOM | 0.00 | = | 90.46 | +1.85 |
| RFC | 6.00 | = | 13.06 | +0.03 |
| LOC | 23.00 | = | 72.16 | -0.20 |

**CodeQL:** 37 alertas (0 de segurança), 1.90 por KLOC, variação -3

- Regras que aumentaram: `java/confusing-method-signature` (+2), `java/unused-parameter` (+1)
- Regras que diminuíram: `java/missing-override-annotation` (-5), `java/class-name-matches-super-class` (-1)
- Classes novas (6): org.jsoup.helper.RequestDispatch, org.jsoup.helper.RequestExecutor, org.jsoup.helper.UrlConnectionExecutor, org.jsoup.parser.Token$XmlDecl, org.jsoup.parser.TokeniserState$Anonymous68 ...
- Classes removidas (2): org.jsoup.UncheckedIOException, org.jsoup.select.StructuralEvaluator$Parent

**Explicação (preencher com o changelog do jsoup):** 

---

## 1.20.1 (2025-04-29)

**Tamanho:** 275 classes (+5), 19895 LOC (+412)

| Métrica | Mediana | Δ | Média | Δ |
|---|---|---|---|---|
| WMC | 6.00 | = | 17.25 | +0.18 |
| DIT | 1.00 | = | 1.98 | -0.00 |
| NOC | 0.00 | = | 0.38 | +0.00 |
| CBO | 3.00 | = | 5.44 | +0.15 |
| LCOM | 0.00 | = | 93.49 | +3.03 |
| RFC | 6.00 | = | 13.23 | +0.17 |
| LOC | 23.00 | = | 72.35 | +0.19 |

**CodeQL:** 36 alertas (1 de segurança), 1.81 por KLOC, variação -1

- Regras que aumentaram: `java/unreleased-lock` (+1)
- Regras que diminuíram: `java/missing-clone-method` (-1), `java/unused-parameter` (-1)
- Classes novas (6): org.jsoup.nodes.Printer, org.jsoup.nodes.Printer$Outline, org.jsoup.nodes.Printer$Pretty, org.jsoup.parser.CharacterReader$CharPredicate, org.jsoup.parser.TagSet ...
- Classes removidas (1): org.jsoup.nodes.Node$OuterHtmlVisitor

**Explicação (preencher com o changelog do jsoup):** 

---

## 1.21.1 (2025-06-23)

**Tamanho:** 285 classes (+10), 20400 LOC (+505)

| Métrica | Mediana | Δ | Média | Δ |
|---|---|---|---|---|
| WMC | 7.00 | +1.00 | 17.05 | -0.20 |
| DIT | 1.00 | = | 2.03 | +0.05 |
| NOC | 0.00 | = | 0.41 | +0.03 |
| CBO | 3.00 | = | 5.53 | +0.10 |
| LCOM | 0.00 | = | 93.18 | -0.31 |
| RFC | 6.00 | = | 13.14 | -0.09 |
| LOC | 23.00 | = | 71.58 | -0.77 |

**CodeQL:** 35 alertas (1 de segurança), 1.72 por KLOC, variação -1

- Regras que aumentaram: `java/confusing-method-signature` (+2)
- Regras que diminuíram: `java/input-resource-leak` (-1), `java/missing-override-annotation` (-1), `java/unused-parameter` (-1)
- Classes novas (11): org.jsoup.internal.QuietAppendable, org.jsoup.internal.QuietAppendable$BaseAppendable, org.jsoup.internal.QuietAppendable$BaseAppendable$Action, org.jsoup.internal.QuietAppendable$StringBuilderAppendable, org.jsoup.internal.SimpleStreamReader ...
- Classes removidas (1): org.jsoup.helper.ChangeNotifyingArrayList

**Explicação (preencher com o changelog do jsoup):** 

---

## 1.21.2 (2025-08-25)

**Tamanho:** 285 classes (+0), 20521 LOC (+121)

| Métrica | Mediana | Δ | Média | Δ |
|---|---|---|---|---|
| WMC | 7.00 | = | 17.21 | +0.15 |
| DIT | 1.00 | = | 2.03 | = |
| NOC | 0.00 | = | 0.41 | = |
| CBO | 3.00 | = | 5.54 | +0.00 |
| LCOM | 0.00 | = | 93.95 | +0.77 |
| RFC | 6.00 | = | 13.16 | +0.02 |
| LOC | 23.00 | = | 72.00 | +0.42 |

**CodeQL:** 36 alertas (1 de segurança), 1.75 por KLOC, variação +1

- Regras que aumentaram: `java/missing-clone-method` (+1)

**Explicação (preencher com o changelog do jsoup):** 

---

## 1.22.1 (2026-01-01)

**Tamanho:** 290 classes (+5), 20768 LOC (+247)

| Métrica | Mediana | Δ | Média | Δ |
|---|---|---|---|---|
| WMC | 6.00 | -1.00 | 17.15 | -0.06 |
| DIT | 1.00 | = | 2.02 | -0.01 |
| NOC | 0.00 | = | 0.41 | -0.00 |
| CBO | 3.50 | +0.50 | 5.52 | -0.01 |
| LCOM | 0.00 | = | 93.68 | -0.27 |
| RFC | 6.00 | = | 13.14 | -0.02 |
| LOC | 23.00 | = | 71.61 | -0.39 |

**CodeQL:** 35 alertas (1 de segurança), 1.69 por KLOC, variação -1

- Regras que aumentaram: `java/unused-parameter` (+1)
- Regras que diminuíram: `java/non-sync-override` (-2)
- Classes novas (5): org.jsoup.helper.Re2jRegex, org.jsoup.helper.Re2jRegex$Re2jMatcher, org.jsoup.helper.Regex, org.jsoup.helper.Regex$JdkMatcher, org.jsoup.helper.Regex$Matcher

**Explicação (preencher com o changelog do jsoup):** 

---

## 1.22.2 (2026-04-20)

**Tamanho:** 291 classes (+1), 20997 LOC (+229)

| Métrica | Mediana | Δ | Média | Δ |
|---|---|---|---|---|
| WMC | 6.00 | = | 17.30 | +0.15 |
| DIT | 1.00 | = | 2.01 | -0.00 |
| NOC | 0.00 | = | 0.41 | -0.00 |
| CBO | 3.00 | -0.50 | 5.52 | -0.00 |
| LCOM | 0.00 | = | 93.74 | +0.06 |
| RFC | 6.00 | = | 13.20 | +0.05 |
| LOC | 23.00 | = | 72.15 | +0.54 |

**CodeQL:** 35 alertas (1 de segurança), 1.67 por KLOC, variação =

- Classes novas (1): org.jsoup.parser.TokeniserState$Anonymous69

**Explicação (preencher com o changelog do jsoup):** 

---

## 1.23.1 (2026-07-30)

**Tamanho:** 297 classes (+6), 21830 LOC (+833)

| Métrica | Mediana | Δ | Média | Δ |
|---|---|---|---|---|
| WMC | 7.00 | +1.00 | 17.73 | +0.44 |
| DIT | 1.00 | = | 1.99 | -0.02 |
| NOC | 0.00 | = | 0.40 | -0.01 |
| CBO | 3.00 | = | 5.54 | +0.01 |
| LCOM | 0.00 | = | 96.23 | +2.49 |
| RFC | 6.00 | = | 13.24 | +0.05 |
| LOC | 23.00 | = | 73.50 | +1.35 |

**CodeQL:** 37 alertas (1 de segurança), 1.69 por KLOC, variação +2

- Regras que aumentaram: `java/deprecated-call` (+2)
- Classes novas (7): org.jsoup.internal.ControllableInputStream$ProgressState, org.jsoup.internal.LineMap, org.jsoup.nodes.LeafNode$TrackedValue, org.jsoup.nodes.NodeInternals, org.jsoup.nodes.Range$Spans ...
- Classes removidas (1): org.jsoup.parser.HtmlTreeBuilderState$Anonymous24

**Explicação (preencher com o changelog do jsoup):** 

---

## 1.23.2 (2026-08-26)

**Tamanho:** 299 classes (+2), 22125 LOC (+295)

| Métrica | Mediana | Δ | Média | Δ |
|---|---|---|---|---|
| WMC | 6.00 | -1.00 | 18.02 | +0.29 |
| DIT | 1.00 | = | 1.99 | -0.01 |
| NOC | 0.00 | = | 0.39 | -0.00 |
| CBO | 3.00 | = | 5.52 | -0.01 |
| LCOM | 0.00 | = | 99.23 | +3.00 |
| RFC | 6.00 | = | 13.43 | +0.19 |
| LOC | 23.00 | = | 74.00 | +0.49 |

**CodeQL:** 38 alertas (1 de segurança), 1.72 por KLOC, variação +1

- Regras que aumentaram: `java/chained-type-tests` (+1)
- Classes novas (2): org.jsoup.internal.NamespaceBindings, org.jsoup.internal.NamespaceBindings$NamespaceChange

**Explicação (preencher com o changelog do jsoup):** 

---

## Comparativo final: 1.14.3 -> 1.23.2

| Indicador | Início | Fim | Variação |
|---|---|---|---|
| WMC (mediana) | 6.00 | 6.00 | +0.0% |
| DIT (mediana) | 1.00 | 1.00 | +0.0% |
| NOC (mediana) | 0.00 | 0.00 | n/a (base 0) |
| CBO (mediana) | 3.00 | 3.00 | +0.0% |
| LCOM (mediana) | 0.00 | 0.00 | n/a (base 0) |
| RFC (mediana) | 6.00 | 6.00 | +0.0% |
| LOC (mediana) | 22.00 | 23.00 | +4.5% |
| Alertas totais | 257.00 | 38.00 | -85.2% |
| Alertas por KLOC | 15.04 | 1.72 | -88.6% |
| Alertas de segurança | 0.00 | 1.00 | n/a |