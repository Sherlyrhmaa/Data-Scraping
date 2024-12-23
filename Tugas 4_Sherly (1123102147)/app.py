from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/kompas-food")
def KompasFood():
    url = "https://www.kompas.com/food"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    food_articles = soup.find_all('div', class_='foodLatest__item clearfix')

    berita = []
    seen_titles = set()
    for article in food_articles:
        title = article.find('h3').text.strip()
        if title in seen_titles:
            continue
        seen_titles.add(title)
        link = article.find('a')['href']
        image_tag = article.find('img')
        image = image_tag['src'] if image_tag else ""
        berita.append({"title": title, "link": link, "image": image})

    return render_template("food.html", berita=berita)

if __name__ == "__main__":
    app.run(debug=True)
