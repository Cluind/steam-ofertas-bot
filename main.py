import requests
import time

BOT_TOKEN = "8468389556:AAHgiBSlLQyk6Y2Kj6ppjX_RwI8BhyZ3nOY"
CANAL_ID = "@ClyindOfertas"

def enviar_mensagem(texto):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CANAL_ID, "text": texto, "parse_mode": "HTML"}
    requests.post(url, data=data)

def buscar_ofertas():
    url = "https://store.steampowered.com/api/featuredcategories/"
    r = requests.get(url).json()
    ofertas = []
    for item in r["specials"]["items"]:
        desconto = item["discount_percent"]
        if desconto >= 70:
            nome = item["name"]
            preco = item["final_price"] / 100
            link = item["store_url"]
            ofertas.append(f"🔥 <b>{nome}</b> - {desconto}% OFF\n💰 R${preco:.2f}\n🔗 {link}")
    return ofertas

while True:
    ofertas = buscar_ofertas()
    for o in ofertas:
        enviar_mensagem(o)
    time.sleep(3600)
