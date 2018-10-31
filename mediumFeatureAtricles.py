from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(
    '/Library/Python/2.7/site-packages/chromedriver')
url = "https://medium.com/topic/editors-picks"
driver.get(url)

titleList = []
n = 1
for i in range(0, 500):
    try:
        article = driver.find_element_by_xpath('//*[@id = "root"]/div/section/section[1]/div[3]/div/div[1]/section[' + str(n) + ']/div/section/div[1]/div[1]/div/h3/a')
        file = open("articles.txt", "w+")
        file.write(article)
    except:
        html = driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        driver.implicitly_wait(7)
        article = driver.find_element_by_xpath(
            '//*[@id = "root"]/div/section/section[1]/div[3]/div/div[1]/section[' + str(n) + ']/div/section/div[1]/div[1]/div/h3/a')
    titleList.append(article.text)
    #go back
    n += 1
    print(n)
    
print(titleList)
print(len(titleList))
driver.quit()
