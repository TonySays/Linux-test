
import requests
from bs4 import BeautifulSoup


result = requests.get("https://coinyuppie.com")

# print(result.headers)


src = result.content

# print(src)


soup = BeautifulSoup(src,'lxml')

links = soup.find_all("a")

print(links)
print("\n")
