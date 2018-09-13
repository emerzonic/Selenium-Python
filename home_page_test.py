
def landing_page_test():
	from selenium import webdriver

	landing_page = webdriver.Firefox()
	landing_page.get('https://secure-garden-12181.herokuapp.com')
	return landing_page

landing_page_test()