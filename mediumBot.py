from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

'''TODO: 
    -clean up the text file
        --get rid of the medium stuff (stored  in <p> as well)
        --get rid of the stuff about the author
    -locate the text file
    -run the prediction on the text file
'''
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(
    '/Library/Python/2.7/site-packages/chromedriver', chrome_options=options)
url = "https://medium.com/topic/editors-picks"
driver.get(url)

n = 35
rangeNum = 400

url = "https://medium.com/topic/editors-picks"
driver.get(url)

SCROLL_PAUSE_TIME = 0.5

#fails at 26

for i in range(0, rangeNum):
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    article = driver.find_element_by_xpath('//*[@id = "root"]/div/section/section[1]/div[3]/div/div[1]/section[' + str(i+1) + ']/div/section/div[1]/div[1]/div/h3/a').click()
    driver.execute_script(
        "return document.body.scrollHeight")
    driver.implicitly_wait(7)
    articleURL = driver.current_url


    title = driver.find_element_by_css_selector('h1').text
    print(title)    

    url = "https://outline.com/"
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="source"]').send_keys(articleURL)
    driver.find_element_by_xpath(
        '/html/body/outline-app/outline-landing/div/div/form/div[2]/button').click()
  
    driver.implicitly_wait(15)
    increment = 1
    with open('articlesMain.txt', 'a+') as text_file:
        while(True):
            try:
                currentItem = driver.find_element_by_xpath('/html/body/outline-app/outline-article/div[2]/div/raw/p[' + str(increment) + ']').text
                text_file.write(currentItem)
                increment += 1
            except:
                break
    print(str(i+1) + "/" + str(rangeNum))
    driver.execute_script("window.history.go(-2)")

driver.quit()
