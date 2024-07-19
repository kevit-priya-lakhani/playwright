
from playwright.sync_api import sync_playwright
import time
from playwright_stealth import stealth_sync
import re



playwright=sync_playwright().start()


browser=playwright.chromium.launch(headless=False, slow_mo=500)

extra_headers = {
    'Sec-Ch-Ua':
    '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'Sec-Ch-Ua-Mobile':
    '?0',
    'Sec-Ch-Ua-Platform':
    "Linux",
    'Sec-Fetch-Dest':
    'empty',
    'Sec-Fetch-Mode':
    'cors',
    'Sec-Fetch-Site':
    'same-site',
    }

user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0'

context = browser.new_context(extra_http_headers = extra_headers,user_agent=user_agent)
page = context.new_page()
stealth_sync(page)



site_user={'Home':'https://www.delta.nl/','Companies':'https://www.delta.nl/zakelijk/'}
main_menu_last=[4,5]

#loop for at home and companies sites

for j in range(2):

    user_type_name=list(site_user.keys())[j]
    user_type_url=list(site_user.values())[j]
    page.goto(user_type_url)

    url_main='https://www.delta.nl/'

    # Scrape Home Page content

    page.wait_for_selector('#vuejs')
    home_page_text=page.locator('#vuejs').all_inner_texts()
    f=open(f'Scraped Data/{user_type_name}/{page.title()}','w')
    f.write(home_page_text[0])
    f.close()

    core_menu=[]

    for i in range(1,main_menu_last[j]):
        main_link=page.locator(f'#coreMenu > li:nth-child({i})')
        main_link.hover()

        sub_links=main_link.text_content().split("\n")  #store sub links into a list
        sub_links=list(filter(lambda a: a != '', sub_links))
        # print(sub_links)
        core_menu.append(sub_links[0])

        visited=[]

        for link in sub_links:
            elements = page.locator(f"text={link}").all()# elements.
            
            for element in elements:    # Iterate through each element and get the href attribute
                href = element.get_attribute('href')

                if href:    # Ensure href is not None
                    if href not in visited:  #if link is not already visited 
                        main_link.hover()
                        element.hover()
                        if re.match(r'https:.*',href):  #if href is of 'https://' format, directly go to link
                            page.goto(href)
                            print("url: ",href)
                            visited.append(href)
                            break

                        page.goto(url_main + href)
                        text=page.locator(".base").all_inner_texts() # scrape text of entire page
                        page_title=page.title() 

                        if len(text)>0:     #if the text content is available 
                            f=open(f'Scraped Data/{user_type_name}/{core_menu[i-1]}/{page_title}','w') #create new file and append contents
                            f.write(text[0])
                        else:
                            page.goto(user_type_url)    # else go back 

                        visited.append(url_main + href)
                        print("url: ",url_main + href)
                        break  
