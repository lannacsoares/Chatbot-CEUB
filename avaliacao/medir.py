"""Mede o chatbot contra NFR-07, NFR-08 e NFR-09 (tarefa 03-02).

Uso (com o servidor rodando em outro terminal):
  python avaliacao/medir.py                      # todas as perguntas
  python avaliacao/medir.py --disciplina "Cálculo I"
  python avaliacao/medir.py --so geral,fora_do_escopo

Manda cada pergunta ao servidor, mede o tempo e mostra a resposta ao lado
da resposta esperada. Quem roda marca cada uma como certa ou errada
(c / e / Enter para pular).

Privacidade (NFR-10): as respostas das perguntas pessoais (faltas e
professor) aparecem só na tela e nunca vão para arquivo. O arquivo de
resultado guarda, dessas, só o tempo e a marcação.
"""

import argparse
import csv
import json
import sys
import time
import urllib.request
from datetime import datetime
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
AQUI = Path(__file__).resolve().parent
PESSOAIS = {"faltas", "professor"}


def perguntar(url: str, pergunta: str) -> tuple[str, float, int]:
    corpo = json.dumps({"pergunta": pergunta}).encode("utf-8")
    req = urllib.request.Request(url, corpo, {"Content-Type": "application/json"})
    inicio = time.perf_counter()
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            dados = json.load(r)
            return dados.get("resposta", ""), time.perf_counter() - inicio, r.status
    except urllib.error.HTTPError as e:
        detalhe = json.load(e).get("detail", "")
        return f"[erro {e.code}] {detalhe}", time.perf_counter() - inicio, e.code


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default="http://localhost:8000/api/perguntar")
    ap.add_argument("--disciplina", default="Inteligência Artificial")
    ap.add_argument("--so", help="tipos separados por vírgula")
    ap.add_argument("--sem-marcar", action="store_true", help="só mede o tempo")
    a = ap.parse_args()

    with (AQUI / "perguntas_teste.csv").open(encoding="utf-8", newline="") as f:
        perguntas = list(csv.DictReader(f))
    if a.so:
        tipos = set(a.so.split(","))
        perguntas = [p for p in perguntas if p["tipo"] in tipos]

    resultados = []
    for p in perguntas:
        texto = p["pergunta"].replace("{disciplina}", a.disciplina)
        resposta, seg, status = perguntar(a.url, texto)
        print(f"\n[{p['id']} · {p['tipo']}] {texto}  ({seg:.1f} s)")
        print(f"  Resposta:  {resposta}")
        print(f"  Esperado:  {p['resposta_esperada']}  ({p['fonte']})")
        marca = ""
        if not a.sem_marcar:
            marca = input("  Certa (c), errada (e) ou Enter para pular? ").strip().lower()[:1]
        pessoal = p["tipo"] in PESSOAIS
        resultados.append({
            "id": p["id"], "conjunto": p["conjunto"], "tipo": p["tipo"],
            "segundos": f"{seg:.2f}", "status": status, "marca": marca,
            "resposta": "" if pessoal else resposta,  # nada pessoal em arquivo
        })

    def taxa(conj):
        marcadas = [r for r in resultados if r["conjunto"] == conj and r["marca"] in ("c", "e")]
        return (sum(r["marca"] == "c" for r in marcadas), len(marcadas))

    tempos = sorted(float(r["segundos"]) for r in resultados)
    ate15 = sum(t <= 15 for t in tempos)
    print("\n===== Resumo =====")
    for nome, conj, meta in [("Precisão (NFR-07)", "precisao", 0.8), ("Honestidade (NFR-08)", "honestidade", 0.9)]:
        ok, n = taxa(conj)
        if n:
            print(f"{nome}: {ok}/{n} = {ok / n:.0%}  (meta {meta:.0%}) {'ATINGIDA' if ok / n >= meta else 'NÃO atingida'}")
    if tempos:
        print(f"Tempo (NFR-09): {ate15}/{len(tempos)} em até 15 s = {ate15 / len(tempos):.0%} (meta 90%) · "
              f"mediana {tempos[len(tempos) // 2]:.1f} s · máximo {tempos[-1]:.1f} s")

    pasta = AQUI / "resultados"
    pasta.mkdir(exist_ok=True)
    arq = pasta / f"medicao-{datetime.now():%Y%m%d-%H%M}.csv"
    with arq.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(resultados[0]))
        w.writeheader()
        w.writerows(resultados)
    print(f"\nResultado salvo em {arq.relative_to(AQUI.parent)} (sem respostas pessoais).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
