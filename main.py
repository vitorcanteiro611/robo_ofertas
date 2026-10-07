import os
os.system('cls')

import asyncio

from dotenv import load_dotenv
from telegram import Bot

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

print("TOKEN carregado:", TOKEN is not None)
print("CHAT_ID carregado:", CHAT_ID)


async def enviar_oferta(produto, preco, desconto, link, tipo):

    bot = Bot(token=TOKEN)

    mensagem = f"""
    {tipo}
🔥 OFERTA ENCONTRADA!

🛒 Produto: {produto}
💰 Preço: {preco}
🏷️ Desconto: {desconto}

🔗 Comprar:
{link}
"""

    await bot.send_message(
        chat_id=CHAT_ID,
        text=mensagem
    )

    print("Oferta enviada com sucesso!")


async def main():

    produtos = [
        {
            "nome": "SSD 1TB",
            "preco": "R$ 299,90",
            "desconto": 60,
            "link": "https://exemplo.com"
        },
        {
            "nome": "Mouse Gamer",
            "preco": "R$ 89,90",
            "desconto": 40,
            "link": "https://exemplo.com"
        },
        {
            "nome": "Teclado Mecânico",
            "preco": "R$ 149,90",
            "desconto": 20,
            "link": "https://exemplo.com"
        }
    ]

    for produto in produtos:

        if produto["desconto"] >= 50:

            print(f"🔥 SUPER OFERTA: {produto['nome']}")

            await enviar_oferta(
                produto["nome"],
                produto["preco"],
                produto["desconto"],
                produto["link"],
                "🔥 SUPER OFERTA!"
            )

        elif produto["desconto"] >= 30:

            print(f"✅ BOA OFERTA: {produto['nome']}")

            await enviar_oferta(
                produto["nome"],
                produto["preco"],
                produto["desconto"],
                produto["link"],
                "✅ BOA OFERTA!"
            )

        else:

            print(f"❌ OFERTA IGNORADA: {produto['nome']}")


if __name__ == "__main__":
    asyncio.run(main())