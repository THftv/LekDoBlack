
# Lek Do BlacK - API Sarcástica da Quebrada

Um bot que não tem paciência com burrice e responde com gírias, deboche e uma pitada de ódio.

## Como rodar localmente

1. Clone o projeto ou baixe o ZIP:

```bash
git clone https://github.com/seu-usuario/lekv2.git
cd lekv2
```

2. Instale os pacotes:

```bash
pip install -r requirements.txt
```

3. Configure sua chave OpenAI:

```bash
cp .env.example .env
# edite o arquivo .env e coloque sua chave real
```

4. Rode o servidor:

```bash
uvicorn main:app --reload
```

A API estará em: `http://127.0.0.1:8000/lekv2`

## Deploy na Railway

- Conecte esse projeto ao Railway
- Adicione a variável de ambiente `OPENAI_API_KEY`
- Comando de start: `uvicorn main:app --host 0.0.0.0 --port $PORT`
