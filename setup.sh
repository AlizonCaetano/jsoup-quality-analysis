#!/usr/bin/env bash
# Instala tudo que a análise precisa (WSL/Ubuntu). Pode rodar de novo sem problema.
set -euo pipefail

sudo apt update
sudo apt install -y openjdk-17-jdk maven git python3-venv curl

mkdir -p tools

# CK: compila a partir do código-fonte e guarda o jar em tools/ck.jar
if [ ! -f tools/ck.jar ]; then
  git clone --depth 1 https://github.com/mauricioaniche/ck.git tools/ck-src
  (cd tools/ck-src && mvn -q -DskipTests package)
  cp tools/ck-src/target/ck-*-jar-with-dependencies.jar tools/ck.jar
fi

# CodeQL: bundle oficial (CLI + consultas Java)
if [ ! -d tools/codeql ]; then
  curl -L -o tools/codeql.tar.gz \
    https://github.com/github/codeql-action/releases/latest/download/codeql-bundle-linux64.tar.gz
  tar -xzf tools/codeql.tar.gz -C tools
  rm tools/codeql.tar.gz
fi

# Ambiente Python isolado
python3 -m venv .venv
.venv/bin/pip install -q -r requirements.txt

echo "Setup ok."
