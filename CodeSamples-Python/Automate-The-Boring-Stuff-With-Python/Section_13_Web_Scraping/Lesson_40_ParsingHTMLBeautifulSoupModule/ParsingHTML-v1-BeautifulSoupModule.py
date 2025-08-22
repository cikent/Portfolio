# Web pages are plaintext files formatted as HTML.
# HTML can be parsed with the BeautifulSoup module.
# BeautifulSoup is imported with the name bs4.
# Pass the string with the HTML to the bs4.BeautfiulSoup() function to get a Soup object.
# The Soup object has a select() method that can be passed a string of the CSS selector for an HTML tag.
# You can get a CSS selector string from the browser's developer tools by right-clicking the element and selecting Copy CSS Path.
# The select() method will return a list of matching Element objects.

# Import relelvant modules
import bs4, requests

# Create ProductUrl variables to utilize and DEBUG
toScrapProductUrl = str('https://books.toscrape.com/catalogue/category/books/science_22/index.html')

# Create a function() to obtain the Price for the Automate the Boring Stuff with Python book
def getAmazonPrice(productUrl):
    # Add User Agent Header to emulate a Real User to help bypass getting blocked
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }
    res = requests.get(productUrl, headers=headers)
    res.raise_for_status()

    # Create a Soup Object AND pass the html.parser as the 2nd argument to hide the warning
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # Create an Element Selector for Price
    elems = soup.select('#default > div > div > div > div > section > div:nth-child(2) > ol > li:nth-child(4) > article > div.product_price > p.price_color')
    
    # Return the Price Element Text value
    return elems[0].text.strip()
    
# Create a variable for the Price
price = getAmazonPrice(toScrapProductUrl)

# Print to screen the Price value
print('The price is ' + price)