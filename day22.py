driver=webdriver.chrome()
driver.get("https://www.instagram.com/guvioffical/")

followers_element=driver.find_elements_by_xpath("//a[@href='/guviofficial/followers/']")
followers_count= followers_element.text

following_element=driver.find_elements_by_xpath("//a[@href='/guviofficial/following/']")
followers_count=following_element.text

print("total numbers of folloers:", followers_count)
print("total number of following:", followers_count)
driver.quit()