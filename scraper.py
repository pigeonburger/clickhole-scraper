import re
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'
}

def get_total_article_pages():
    r = requests.get('https://www.clickhole.com/page/1', headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    last_page_number = soup.find('div', class_='nav-links').find_all('a')[-2].text.replace(',', '')
    return int(last_page_number)

def get_article_content(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    article_content = soup.find('div', class_='post-content')
    title = soup.find('h1', class_='post-title').encode_contents().decode('utf-8')
    article_content = [re.sub('<[^<]+?>', '', i.encode_contents().decode('utf-8')) for i in article_content.find_all('p')]
    article_content.insert(0, title)
    return '\n\n'.join(article_content)

def get_article_urls(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    article_links = soup.find_all('div', class_='post-header')
    article_links = [i.find('h2', class_='post-title').find('a')['href'] for i in article_links]
    return article_links

def main():
    num_pages = get_total_article_pages()
    num_articles = num_pages * 7
    print(f'Scraping {num_articles} articles....')

    for i in range(1, num_pages+1):
        url = f'https://www.clickhole.com/page/{i}'
        article_urls = get_article_urls(url)
        for url in article_urls:
            content = get_article_content(url)
            with open('clickholecontent.txt', 'a+', encoding='utf-8') as contentfile:
                contentfile.write('<|startoftext|>'+content+'<|endoftext|>\n')
            article_number = (article_urls.index(url) + 1) + (i-1) * 7
            print(f'Scraping article {article_number} of {num_articles}.....', end='\r')

    print('\nDone scraping.')

print('Clickhole Article Scraper')
print('By Pigeonburger <https://github.com/pigeonburger>, 2021')
print('--------------------------')
main()
