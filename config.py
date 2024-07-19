# config.py

from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync

def setup_playwright():
    """Sets up Playwright browser with specific configuration."""
    playwright = sync_playwright().start()
    
    browser = playwright.chromium.launch(headless=False, slow_mo=500)

    extra_headers = {
        'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': "Linux",
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
    }

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0'

    context = browser.new_context(extra_http_headers=extra_headers, user_agent=user_agent)
    page = context.new_page()
    stealth_sync(page)

    return browser, context, page

def get_site_user():
    """Returns the URLs to be scraped."""
    return {
        'Home': 'https://www.delta.nl/',
        'Companies': 'https://www.delta.nl/zakelijk/'
    }

def get_main_menu_last():
    """Returns the number of main menu items for each site."""
    return [4, 5]
