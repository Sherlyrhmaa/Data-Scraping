from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/kompas-food")
def Kompas():
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

    return render_template("kompas.html", berita=berita)

@app.route("/liputan6-kuliner")
def Liputan6():
    url = "https://www.liputan6.com/tag/kuliner"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    food_articles = soup.find_all('article', class_='articles--iridescent-list--item')

    berita = []
    seen_titles = set()
    for article in food_articles:
        title = article.find('h4', class_='articles--iridescent-list--text-item__title').text.strip()
        if title in seen_titles:
            continue
        seen_titles.add(title)
        link = article.find('a', class_='ui--a articles--iridescent-list--text-item__title-link')['href']
        image_tag = article.find('img', class_='articles--iridescent-list--text-item__figure-image-img')
        image_url = image_tag['src'] if image_tag else ""
        berita.append({
            'title': title,
            'image': image_url,
            'link': link
        })

    return render_template('liputan6.html', berita=berita)

@app.route("/tribunnews-food")
def Tribunnews():
    url = "https://www.tribunnews.com/travel/kuliner"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    food_articles = soup.find_all('li', class_='p1520 art-list pos_rel')

    berita = []
    seen_titles = set()
    for article in food_articles:
        title_tag = article.find('h3')
        if not title_tag:
            continue
        title = title_tag.text.strip()
        if title in seen_titles:
            continue
        seen_titles.add(title)
        link = article.find('a')['href']
        image_tag = article.find('img')
        image = image_tag['src'] if image_tag else ""
        berita.append({"title": title, "link": link, "image": image})

    return render_template("tribunnews.html", berita=berita)

if __name__ == "__main__":
    app.run(debug=True)