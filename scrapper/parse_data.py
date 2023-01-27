from bs4 import BeautifulSoup


def parser(source, selector):
    """Simple function to parse 
    response into BS Object.
    This funcion takes into consideration
    the status code 200 (HTTP OK)"""
    if source.status_code == 200:
        soup = BeautifulSoup(source.content, 'html.parser')
        #Using the select to select based on CSS selectors.
        return soup.select(selector)
    else:
        return False
