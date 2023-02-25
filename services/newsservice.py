#newssservice.py
# @author: Ethan Hu and Amol Budhiraja

from bs4 import BeautifulSoup
import urllib.request

def news_service(app):
    """News Feature Routes"""

    @app.route("/news/<string:title>", methods=["GET"])
    def newstitle(title: str) -> str:
        title = title.upper()
        return f"<p>News Title: {title}!</p>"

    @app.route("/news", methods=["GET"])
    def news():
        request = urllib.request.Request('https://news.berkeley.edu/all-news/', headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'})
        source = urllib.request.urlopen(request).read()
        soup = BeautifulSoup(source, 'html.parser')
        
        title_list = soup.find_all('a', {'class': 'post-title'})
        articles = []
        for title in title_list:
            article_url = title.get("href")
            article_title = title.get("title")
            article = (article_title, article_url)
            articles.append(article)

        # caption_list = soup.find_all('div', {'class': 'caption'})
        # captions = []
        # for caption in caption_list:
        #     captions.append(str(caption.contents[2].strip()))

        return articles

