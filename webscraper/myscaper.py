import pandas
import requests
from bs4 import BeautifulSoup

# Getting the webpage
webpage = requests.get("http://quotes.toscrape.com/")

# Loading the content
content = webpage.content

# Parsing the content
result = BeautifulSoup(content, 'html.parser')
# print(result.prettify())

# Identifying the products on the page by the div tag and the class name
quotes_full = result.find_all("div", {"class": "quote"})


# Creating a list for each of the desired piece of information
quotes = []
author = []

# print(quotes_full)

# Iterating over the list of products and extracting the necessary info
for quote in quotes_full:
    print(quote)
    quotes.append(quote.span.string)
    author.append(quote.small.string)


# print(names, len(names))
# print(links, len(links))
# print(prices, len(prices))

data = list(zip(quotes, author))

# Creating the Pandas dataframe
d = pandas.DataFrame(data, columns=['Quote', 'Author'])

# Writing the dataframe to a new Excel file
try:
    d.to_excel("Quotes.xlsx")

except:
    print("\nSomething went wrong! Please check your code.")

else:
    print("\nWeb data successfully written to Excel.")

finally:
    print("\nQuitting the program. Bye!")

# End of program
