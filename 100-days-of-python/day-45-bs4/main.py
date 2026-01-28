# from bs4 import BeautifulSoup
# # import lxml

# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")

# # soup = BeautifulSoup(contents, "lxml")

# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup)
# # print(soup.prettify())
# # print(soup.a)
# # print(soup.li)
# # print(soup.p)

# all_anchor_tags = soup.find_all(name="a") 
# print(all_anchor_tags)


# # All of the anchor tags

# # print(all_anchor_tags)

# #If I only want the texts of the anchor tag
# for tag in all_anchor_tags:
#     print(tag.getText())


# #If I only want the links of the anchor tag
# for tag in all_anchor_tags:
#     print(tag.get("href"))


# # Getting a heading(h1) and the ID(name) that matches
# heading = soup.find(name="h1", id="name")
# print(heading)

# # Getting the class attribute(The reason for using the class_ is because class is a reserved word in Python)
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.getText())
# print(section_heading.name)
# print(section_heading.get("class"))



# # Getting company URL inside the paragraph tag
# company_url = soup.select_one(selector="p a")
# print(company_url)


# # Using the class or the ID in the CSS selector
# name = soup.select_one(selector="#name")
# print(name)

# # If I want to select all the heading elements
# headings = soup.select(".heading")
# print(headings)

## Scraping a website
#Easy 
# -------------------------------------------------
## Scraping a website
#Easy Mode
from bs4 import BeautifulSoup
import requests

response =requests.get("https://appbrewery.github.io/news.ycombinator.com/")

# print(response.text)

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title)

# article_tag = soup.find(name="a", class_="storylink")
articles = soup.find_all(name="a", class_="storylink")
article_texts =[]
article_links =[]
# print(article_tag.getText())
for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    article_links.append(article_link)


# article_text = article_tag.getText()
# article_link = article_tag.get("href")
# article_upvote = soup.find(name="span", class_="score")
# article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]



# print(article_text)
# print(article_link)
# print(article_upvote.getText())
# print(article_texts)
# print(article_links)
# print(article_upvotes)
# print(article_upvotes[0].split()[0])

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])

# print(article_texts)
# print(article_links)
# print(article_upvotes)