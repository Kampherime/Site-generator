import re

# markdown links look like this [text](link)

# markdown images look like this ![text](image) 

# the regex for markdown links would look as follows: r'\[(.*?)\]\((.*?)\)'

# the regex for markdown images would look as follows: r'!\[(.*?)\]\((.*?)\)'

def extract_markdown_images(text):
    images_tuples = re.findall(r'!\[(.*?)\]\((.*?)\)', text)
    return images_tuples

def extract_markdown_links(text):
    links_tuples = re.findall(r' \[(.*?)\]\((.*?)\)', text)
    return links_tuples
