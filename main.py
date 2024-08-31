import requests
import bs4
from fake_headers import Headers

def get_fake_headers():
    return Headers(browser='chrome', os='win').generate()

def main(keywords):    
    response = requests.get('https://habr.com/ru/articles/',
                            headers=get_fake_headers())
    soup = bs4.BeautifulSoup(response.text, features='lxml')
    article_list = soup.findAll(
        class_='tm-article-snippet tm-article-snippet'
        )
    for article in article_list: 
        body = article.find(
            class_='tm-article-body tm-article-snippet__lead'
            ).text                      
        found_words = [word for word in keywords
                       if body.lower().find(word) != -1]        
        if found_words:    
            date = article.find('time')['datetime']        
            title = article.find(class_='tm-title tm-title_h2').text            
            link = article.find('a', class_='tm-title__link')['href']
            print(f'<{date}> - <{title}> - <https://habr.com{link}>')   

if __name__ == "__main__":
    KEYWORDS = ['дизайн', 'фото', 'web', 'python']
    main(KEYWORDS)