import requests
from bs4 import BeautifulSoup

bbc_url='Link-Here'

headers = {'User-Agents':'Your-User-Agent-Here'}

response = requests.get(url=bbc_url,headers=headers)

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

    with open('Image_name', 'wb') as f:
        f.write(download_response.content)     

    return article_title,paragraph_contents