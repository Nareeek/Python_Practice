from selenium import webdriver

browser = webdriver.Chrome()

'''
browser.get('chrome://settings/content/siteDetails?site=https%3A%2F%2Fok.ru')

flash_icon = browser.find_element_by_css_selector('select')
flash_icon.click()
'''

try:    
    browser.get('https://ok.ru/')
    
    emailElem = browser.find_element_by_id('field_email')
    emailElem.send_keys('+37455209292')
    passwordElem = browser.find_element_by_id('field_password')
    passwordElem.send_keys('Htconex999!')
    passwordElem.submit()

    browser.get('https://ok.ru/game/lov')


except:
    print('Exception happened.')


#browser.quit()

