import os
import requests
from bs4 import BeautifulSoup
from EnvBox import EnvBox
from tqdm import tqdm


def save(article, page_number):
    for article_number, article in enumerate(article):
        file = open(
            file=env.FILE_OUTPUT_PATH.format(
                page_number=page_number,
                article_number=article_number
            ),
            mode='w',
            encoding='utf-8'
        )
        file.write(article)
        file.close()


def get_links(homepage_url: str):
    homepage = requests.get(homepage_url)
    soup = BeautifulSoup(homepage.content, 'html.parser')

    return [
        link.attrs['href']
        for link
        in soup.select(env.POSITION_OF_LINKS_CSS)
    ]


def main():
    loading_page_bar = tqdm(
        range(env.LAST_PAGE + 1),
        desc='page',
        colour='green',
    )

    for page_number in range(0, env.LAST_PAGE + 1):
        articles = []
        url = env.POLKI_URL_TEMP.format(page_number=page_number)
        links = get_links(url)

        loading_article_bar = tqdm(
            range(len(links)),
            desc='articule',
            colour='blue',
            leave=False
        )

        for link in links:
            page = requests.get(link)
            soup = BeautifulSoup(page.content, 'html.parser')

            lines = []
            for paragraph in soup.select('article p')[:-1]:
                lines.append(paragraph.text)

            articles.append(''.join(lines))
            loading_article_bar.update()

        save(articles, page_number)

        loading_article_bar.close()
        loading_page_bar.update()
    loading_page_bar.close()


if __name__ == '__main__':
    env = EnvBox()
    options = ['--headless']

    if not os.path.isdir(env.OUTPUT_DIR):
        os.makedirs(env.OUTPUT_DIR)

    main()
