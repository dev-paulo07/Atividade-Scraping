# README.md

## 1. What (O que é?)

Um projeto em Python para coletar automaticamente dados públicos do site [Books to Scrape](http://books.toscrape.com), usando web scraping com **BeautifulSoup**, tratando os dados com **Pandas** e exportando-os para um arquivo `.csv`.

## 2. Why (Por que?)

Praticar automação de coleta de dados com Python, manipulação com Pandas e organização em um formato de fácil consulta. Esse tipo de solução pode ser usado em projetos de análise de dados, relatórios ou dashboards.

## 3. Who (Quem participa?)

* Desenvolvedores iniciantes ou intermediários que querem aprender scraping, automação e análise de dados.
* Usuários que desejam consultar listas de livros atualizadas.

## 4. Where (Onde será usado?)

* O script pode ser executado em **Windows e Linux**.
* Os resultados ficam disponíveis em um arquivo `.csv` que pode ser usado em qualquer planilha ou software de análise.

## 5. When (Quando usar?)

* Sempre que for necessário coletar informações públicas de forma automatizada.
* Ideal para consultas rápidas sobre tendências de livros ou estudo de dados literários.

## 6. How (Como funciona?)

1. O usuário **clona o repositório** no GitHub.
2. Instala as dependências:

```bash
pip install -r requirements.txt
```

3. Executa o script principal:

```bash
python main.py
```

4. O programa acessa o site **Books to Scrape**, coleta os dados dos livros, organiza com **Pandas** e salva no arquivo `books.csv`.
