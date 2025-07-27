import requests
from bs4 import BeautifulSoup

your_url='URL_HERE'

headers = {'User-Agents':'YOUR USER AGENT HERE'}

response = requests.get(url=your_url,headers=headers)

response.encoding ='utf-8'

def Scraper():
    soup = BeautifulSoup(response.text, 'html.parser')

    news_article = soup.find('article', attrs={'data-testid':'content-post'})

    article_title = news_article.header.span.h3.span.span.text

    paragraph_tags = news_article.find_all('p')

    figure_tags = news_article.figure.div.span.img

    paragraph_contents = f""

    for x in paragraph_tags:
        paragraph_contents= f"{paragraph_contents}\n\n{x.text}"

    figure_src = figure_tags['src']

    download_response = requests.get(url=figure_src)

    with open('image.jpg', 'wb') as f:
        f.write(download_response.content)     
    print("Succesfully Scraped your target!!!")
    return article_title,paragraph_contents