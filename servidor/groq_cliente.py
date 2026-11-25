"""Chamada à Groq (AI-01, D-001). Só escreve a resposta.

Variáveis de ambiente:
- GROQ_API_KEY (obrigatória): nunca em arquivo do projeto (NFR-05).
- GROQ_MODELO (opcional): o modelo escolhido em T-002.
"""

import os

from groq import APIStatusError, Groq, RateLimitError

MODELO_PADRAO = "openai/gpt-oss-120b"  # escolhido em T-002 (2026-11-25)

INSTRUCOES = (
    "Você é o assistente de dúvidas dos alunos do UniCEUB (CEUB), em Brasília. "
    "Responda sempre em português do Brasil, de forma curta e clara. "
    "Você só responde e orienta; nunca diz que executou ações no Espaço Aluno. "
    "Nesta versão você ainda NÃO tem acesso aos documentos oficiais da "
    "instituição nem ao Espaço Aluno do aluno. Se a pergunta depender de uma "
    "regra específica do UniCEUB ou de dados do aluno, diga que não tem "
    "conteúdo suficiente para responder com certeza e oriente a conferir no "
    "Espaço Aluno ou na secretaria. Nunca invente números, prazos ou regras."
)


class ErroGroq(Exception):
    def __init__(self, status: int, mensagem: str):
        self.status, self.mensagem = status, mensagem


def modelo_atual() -> str:
    return os.environ.get("GROQ_MODELO", MODELO_PADRAO)


def _chave() -> str | None:
    """Lê GROQ_API_KEY do ambiente; no Windows, também das variáveis de
    usuário (setx), para funcionar em terminais abertos antes do setx."""
    chave = os.environ.get("GROQ_API_KEY")
    if not chave and os.name == "nt":
        try:
            import winreg
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as k:
                chave, _ = winreg.QueryValueEx(k, "GROQ_API_KEY")
        except OSError:
            chave = None
    return chave or None


def _cliente() -> Groq:
    chave = _chave()
    if not chave:
        raise ErroGroq(503, "A chave da Groq não está configurada no servidor (GROQ_API_KEY).")
    return Groq(api_key=chave, max_retries=1, timeout=30)


def responder(pergunta: str, modelo: str | None = None) -> tuple[str, str]:
    modelo = modelo or modelo_atual()
    cliente = _cliente()  # fora do try: sem chave, o erro 503 sai com a mensagem certa
    try:
        r = cliente.chat.completions.create(
            model=modelo,
            messages=[{"role": "system", "content": INSTRUCOES},
                      {"role": "user", "content": pergunta}],
            temperature=0.2,
            max_tokens=600,
        )
    except RateLimitError:
        raise ErroGroq(429, "Limite do plano gratuito da Groq atingido. Tente de novo em instantes.")
    except APIStatusError as e:
        raise ErroGroq(502, f"A Groq recusou o pedido (código {e.status_code}).")
    except Exception as e:  # rede, tempo esgotado
        raise ErroGroq(502, f"Não foi possível falar com a Groq ({type(e).__name__}).")
    return (r.choices[0].message.content or "").strip(), modelo
