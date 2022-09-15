from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re
from logger import parametrized_logger

KEYWORDS = ['дизайн', 'фото', 'цикл', 'python']


@parametrized_logger(path='log.txt')
def find_word_in_paragraph(content, keyword):
    return re.search(keyword, content)


if __name__ == '__main__':
    driver = webdriver.Chrome('./chromedriver_folder/chromedriver')
    driver.get('http://www.habr.com/ru/all')
    page = driver.find_element(By.ID, 'app').get_attribute('innerHTML')
    driver.quit()
    soup = BeautifulSoup(page, 'html.parser')
    articles = soup.find_all(class_='tm-article-snippet')
    for article in articles:
        date = article.find_all('time')
        heading_section = article.find_all('h2')
        heading = heading_section[0].find_all('span')
        link = article.find_all('a')
        paragraphs = soup.find_all('p')
        show_article = False
        for paragraph in paragraphs:
            text = paragraph.text
            for word in KEYWORDS:
                if find_word_in_paragraph(text, word):
                    show_article = True
        if show_article:
            print(date[0].text, heading[0].text, link[2]['href'])
