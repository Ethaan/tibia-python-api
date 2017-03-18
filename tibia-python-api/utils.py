import re
from urlparse import urlparse

def encodeString(str):
    return str.encode('ascii', 'ignore')

def camelize(str):
    components = str.split(' ')
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0] + "".join(x.title() for x in components[1:])

def isUrl(url):
    parserResponse = urlparse(url)
    return not parserResponse.scheme and not parserResponse.netloc == ''
