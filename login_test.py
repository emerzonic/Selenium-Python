def login_test():
	from selenium import webdriver
	import config

	login_test = webdriver.Firefox()
	login_test.get('https://secure-garden-12181.herokuapp.com')
	login_test.find_element_by_link_text('Login').click()
	
	login = login_test.find_element_by_name("username")
	password = login_test.find_element_by_name("password")
	login.send_keys(config.VIA_Username)
	password.send_keys(config.VIA_Password)

	login_test.find_element_by_name('login').click()
	# login_test.quit()

login_test()