import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "http://books.toscrape.com/catalogue/category/books_1/index.html"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
if response.status_code != 200:
    print("Erro ao acessar o site")
    exit()

soup = BeautifulSoup(response.text, "lxml")
books = []

for book in soup.select("article.product_pod"):
    title = book.h3.a["title"]
    price = book.select_one("p.price_color").text
    availability = book.select_one("p.availability").text.strip()
    books.append({
        "Título": title,
        "Preço": price,
        "Disponibilidade": availability
    })

df = pd.DataFrame(books)
df.to_csv("books.csv", index=False, encoding="utf-8-sig")
print("Arquivo books.csv criado com sucesso!")
print(f"{len(books)} livros coletados.")
