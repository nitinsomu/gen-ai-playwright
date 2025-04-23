from bs4 import BeautifulSoup

def sanitize_html(dom_snapshot):
    """
    Sanitizes the given DOM snapshot by removing unnecessary tags.

    Args:
        dom_snapshot (str): The HTML content as a string.

    Returns:
        str: The sanitized HTML content.
    """
    # Parse the HTML content
    soup = BeautifulSoup(dom_snapshot, 'html.parser')

    # Define tags to remove
    unnecessary_tags = ['script', 'style', 'meta', 'link']

    # Remove unnecessary tags
    for tag in unnecessary_tags:
        for element in soup.find_all(tag):
            element.decompose()

    # Return the sanitized HTML as a string
    return str(soup)