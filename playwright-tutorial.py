from tkinter import Radiobutton
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Launch a browser
    browser = playwright.chromium.launch(headless=False , slow_mo=10000)
    # Create a new page
    page = browser.new_page()
    #Visit website
    page.goto("https://bootswatch.com/default")
    
    # docs_button=page.get_by_role('link',name='Docs')
    # docs_button.click()

    # #print the url
    # print("Docs: ",page.url)

    btn = page.get_by_role("button" ,name="Default Button")
    btn.highlight()
    btn.click()

    heading = page.get_by_role("heading",name="Heading 2")
    heading.highlight()
    print(heading.text_content())

    radio_btn = page.get_by_role("radio",name="Option two can be something else and selecting it will deselect option one")
    radio_btn.highlight()
    print(radio_btn.text_content())
    radio_btn.check()

    checkbox = page.get_by_role("checkbox",name="Default checkbox")
    checkbox.highlight()
    print(checkbox.text_content())
    checkbox.check()


    browser.close()

