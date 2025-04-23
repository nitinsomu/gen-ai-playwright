from playwright.sync_api import Page

def get_page_dom(page: Page) -> str:
    """
    Returns the DOM of the given Playwright page object.

    Args:
        page (Page): The Playwright page object.

    Returns:
        str: The DOM of the page as a string.
    """
    return page.content()