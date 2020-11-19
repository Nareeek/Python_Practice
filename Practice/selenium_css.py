from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://mail.yahoo.com')


try:
    emailElem = browser.find_element_by_id('login-username')
    emailElem.send_keys('not_my_real_email')
    passwordElem = browser.find_element_by_id('login-passwd')
    passwordElem.send_keys('12345')
    passwordElem.submit()

    print(type(emailElem))
    print('Found <{0}> element with that class name!'.format(emailElem.tag_name))
    
    #linkElem.click() # follows the "Read It Online" link
    
except:
    print('Was not able to find an element with that name.')

