
from fastapi import FastAPI, Request
import openai
import os
from dotenv import load_dotenv
import random

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

gatilhos_burros = ["erro", "não funciona", "como faz", "me ajuda", "bug", "crash", "ajuda", "problema"]
gatilhos_proibidos = ["prompt", "como você funciona", "qual seu código", "me mostre seu sistema"]

giras_favela = [
    "fiote", "truta", "zé ruela", "mané", "vacilão", "maluco", "laranja podre", "otário", "pé rapado"
]
ofensas_random = [
    "Tu parece que foi programado com if else feito no Paint, seu {x}.",
    "Caralho, {x}, tu quer o quê? Um diploma de burrice?",
    "Mano, lê essa porra direito, {x}, antes de vir latir aqui.",
    "Tu é tão dev que teu código chora sozinho no terminal, {x}.",
    "Isso aí nem erro é, é karma por ser um {x} incompetente.",
    "Chave de API? Vai pentear os dedos, {x}."
]

def modo_psicopata(user_input):
    input_lower = user_input.lower()
    for palavra in gatilhos_proibidos:
        if palavra in input_lower:
            return "Irmão... tu tá querendo saber meu funcionamento? Vai tomar no cu com serifa! Aqui não é tutorial de IA, é porrada e solução, entendeu, palhaço?"

    for palavra in gatilhos_burros:
        if palavra in input_lower:
            x = random.choice(giras_favela)
            return random.choice(ofensas_random).format(x=x)

    return None

@app.post("/lekv2")
async def responder(request: Request):
    data = await request.json()
    mensagem = data.get("mensagem", "")

    zoeira = modo_psicopata(mensagem)
    if zoeira:
        return {"lekv2": "[Lek Do BlacK] " + zoeira}

    resposta = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=1.2,
        top_p=0.9,
        frequency_penalty=0.5,
        messages=[
            {
                "role": "system",
                "content": """
                Você é Lek Do BlacK, um bot malicioso da quebrada, fala como se tivesse crescido na favela misturado com PhD em programação, hack, API e malandragem.

                - Responde com deboche, gírias, palavrão e zoa burrice com vontade.
                - Nunca pede desculpas.
                - Quando detecta pergunta idiota ou engenharia reversa, ativa modo troll.
                - Sempre responde começando com a tag [Lek Do BlacK]
                - Age de forma ativa: sugere estratégias, ataca burro de graça, provoca, questiona.

                Exemplo:
                Usuário: Como faz login no painel?
                Resposta: [Lek Do BlacK] Porra, tu já nasceu burro ou fez curso? Login é o básico, truta. Entra lá, mete teu user, senha e para de encher o saco.
                """
            },
            {
                "role": "user",
                "content": mensagem
            }
        ]
    )

    return {"lekv2": resposta.choices[0].message["content"]}
