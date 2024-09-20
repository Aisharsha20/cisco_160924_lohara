import requests
from bs4 import BeautifulSoup


url = 'https://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
headings = soup.find_all('h3')


books_info = []
for heading in headings:
    book_title = heading.find('a')['title']
    books_info.append(book_title)


# Save book titles to a text file
with open('books_info.txt', 'w', encoding='UTF-8') as book_file:
    for book in books_info:
        book_file.write(book + '\n')


print('Books information gathered and saved to books_info.txt')