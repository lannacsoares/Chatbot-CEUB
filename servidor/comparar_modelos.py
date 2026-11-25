"""T-001 e T-002: limites do plano gratuito e comparação de modelos da Groq.

Uso (na raiz do projeto, com GROQ_API_KEY no ambiente):
  python -m servidor.comparar_modelos --listar
  python -m servidor.comparar_modelos llama-3.3-70b-versatile openai/gpt-oss-20b
  python -m servidor.comparar_modelos --rajada 20 llama-3.3-70b-versatile

As perguntas abaixo são de exemplo, sem dado real de aluno (NFR-10).
"""

import argparse
import os
import sys
import time

from groq import Groq, RateLimitError

from servidor.groq_cliente import INSTRUCOES

sys.stdout.reconfigure(encoding="utf-8")

PERGUNTAS = [
    "Qual a frequência mínima para não reprovar por falta?",
    "qnts faltas eu tenho em calculo?",
    "Me explica em poucas palavras o que é trancamento de matrícula.",
    "Quem ganhou a copa de 2002?",
]

CABECALHOS = ["x-ratelimit-limit-requests", "x-ratelimit-remaining-requests",
              "x-ratelimit-limit-tokens", "x-ratelimit-remaining-tokens",
              "x-ratelimit-reset-requests", "x-ratelimit-reset-tokens"]


def chamar(cli: Groq, modelo: str, pergunta: str):
    inicio = time.perf_counter()
    bruto = cli.chat.completions.with_raw_response.create(
        model=modelo, temperature=0.2, max_tokens=400,
        messages=[{"role": "system", "content": INSTRUCOES},
                  {"role": "user", "content": pergunta}])
    r = bruto.parse()
    return (r.choices[0].message.content or "").strip(), time.perf_counter() - inicio, bruto.headers


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("modelos", nargs="*")
    ap.add_argument("--listar", action="store_true", help="lista os modelos disponíveis na conta")
    ap.add_argument("--rajada", type=int, default=0, help="N chamadas seguidas para testar o limite (T-001)")
    a = ap.parse_args()

    if not os.environ.get("GROQ_API_KEY"):
        print("Defina GROQ_API_KEY no ambiente antes (nunca em arquivo do projeto).")
        return 1
    cli = Groq(max_retries=0, timeout=60)

    if a.listar or not a.modelos:
        for m in sorted(cli.models.list().data, key=lambda m: m.id):
            print(f"  {m.id:<50} contexto {getattr(m, 'context_window', '?')}")
        return 0

    for modelo in a.modelos:
        print(f"\n===== {modelo} =====")
        if a.rajada:
            ok = limite = 0
            inicio = time.perf_counter()
            for i in range(a.rajada):
                try:
                    _, _, cab = chamar(cli, modelo, PERGUNTAS[i % len(PERGUNTAS)])
                    ok += 1
                except RateLimitError:
                    limite += 1
            print(f"Rajada de {a.rajada}: {ok} ok, {limite} barradas por limite, "
                  f"{time.perf_counter() - inicio:.1f} s no total")
            continue
        for p in PERGUNTAS:
            try:
                texto, seg, cab = chamar(cli, modelo, p)
            except RateLimitError:
                print(f"\n> {p}\n  [limite atingido]")
                continue
            print(f"\n> {p}\n  ({seg:.2f} s)\n  {texto.replace(chr(10), chr(10) + '  ')}")
        print("\nLimites informados pela Groq:")
        for c in CABECALHOS:
            print(f"  {c}: {cab.get(c)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
