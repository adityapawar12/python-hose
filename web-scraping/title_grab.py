import requests
import bs4

result = requests.get("https://adityapawar12.github.io/my-website-v/")
print(result.text)
print(type(result))

soup = bs4.BeautifulSoup(result.text,'lxml')
print(soup.select('title'))
site_paragraphs = soup.select('p')

print(type(site_paragraphs))
print(site_paragraphs)
print(site_paragraphs[0].get_text())
