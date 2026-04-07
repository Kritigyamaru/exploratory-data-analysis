import time         #for delays
import pandas as pd  
from selenium import webdriver          #controls Chrome browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

URL = "https://hamrobazaar.com/category/mobile-phone-handsets/0618E1EF-00AF-4EAC-8E07-4978A2C7BB5E/2A2C15D9-9A08-4E77-A292-F8AD803C2490"
driver.get(URL)
time.sleep(2)

scraped_data = []
visited_links = set()

def scroll_down():
    driver.execute_script("window.scrollBy(0, 900);")
    time.sleep(1.2)

def get_all_cards():
    cards = driver.find_elements(By.CSS_SELECTOR, ".card-product-linear")
    return cards


def scrape_detail_page(link):
    driver.execute_script("window.open(arguments[0]);", link)
    time.sleep(1)

    driver.switch_to.window(driver.window_handles[-1])

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".title--normal.page--title.pname"))
        )

        title = driver.find_element(By.CSS_SELECTOR, ".title--normal.page--title.pname").text
        desc = driver.find_element(By.CLASS_NAME, "ad--desc").text

        data = {
            "Title": title,
            "Description": desc,
            "URL": link
        }

        features = driver.find_elements(By.CLASS_NAME, "feature__item")
        for f in features:
            key = f.find_element(By.CLASS_NAME, "label").text
            value = f.find_element(By.CLASS_NAME, "label__desc").text
            data[key] = value

    except:
        data = None

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    return data

max_items = 100
scrolls_without_new_items = 0

while len(scraped_data) < max_items and scrolls_without_new_items < 10:

    cards = get_all_cards()
    print(f"Found {len(cards)} product cards on screen")

    new_items_found = False

    for card in cards:

        
        titles = card.find_elements(By.CSS_SELECTOR, ".product-title")
        if len(titles) == 0:
            continue

        link = card.find_element(By.CSS_SELECTOR, ".nameAndDropdown a").get_attribute("href")

        if link in visited_links:
            continue

        visited_links.add(link)
        new_items_found = True

        print("Scraping:", link)
        data = scrape_detail_page(link)

        if data:
            scraped_data.append(data)

        if len(scraped_data) >= max_items:
            break

    if not new_items_found:
        scrolls_without_new_items += 1
    else:
        scrolls_without_new_items = 0

    scroll_down()


df = pd.DataFrame(scraped_data)
df.to_csv("hamrobazaar_scraped_mobiles.csv", index=False)

print(f"\nScraped {len(scraped_data)} items.")
driver.quit()
