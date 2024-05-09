# Import the required packages
import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
response = requests.get("https://news.ycombinator.com/")
# Get the text content of the response
yc_web_page = response.text

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(yc_web_page, 'html.parser')

# Initialize lists to store the titles and links of the articles
article_titles = []
article_links = []

# Find all the span tags with class "titleline"
for article_tag in soup.find_all(name="span", class_="titleline"):
    # Get the text of the tag (the title of the article) and append it to the list
    article_titles.append(article_tag.getText())
    # Find the href attribute of the a tag within the span tag (the link of the article) and append it to the list
    article_links.append(article_tag.find("a")["href"])

# Initialize a list to store the upvotes of the articles
article_upvotes = []

# Find all the td tags with class "subtext"
for article in soup.find_all(name="td", class_="subtext"):
    # If the span tag with class "score" doesn't exist within the td tag, append 0 to the list
    if article.span.find(class_="score") is None:
        article_upvotes.append(0)
    # Otherwise, get the text of the span tag, split it to get the number of upvotes, convert it to an integer and append it to the list
    else:
        article_upvotes.append(int(article.span.find(class_="score").contents[0].split()[0]))

# Find the index of the article with the most upvotes
max_points_index = article_upvotes.index(max(article_upvotes))

# Print the title, number of upvotes and link of the article with the most upvotes
print(
    f"{article_titles[max_points_index]}, "
    f"{article_upvotes[max_points_index]} points, "
    f"available at: {article_links[max_points_index]}."
)