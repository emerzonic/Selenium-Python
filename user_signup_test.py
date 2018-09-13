def user_signup_test():
	from selenium import webdriver
	from faker import Faker

	signup_test = webdriver.Firefox()
	signup_test.get('https://secure-garden-12181.herokuapp.com')
	signup_test.find_element_by_link_text('Create Account').click()
	data = Faker()
	user = [data.first_name(),data.last_name(),data.email(),data.first_name(),"password"]
	
	index = 0
	for x in range(1,6):
		field = signup_test.find_element_by_xpath(f"//form[@id='msform']/fieldset/input[{x}]")
		field.send_keys(user[index])
		index += 1

	submit = signup_test.find_element_by_xpath("//form[@id='msform']/fieldset/input[6]")
	submit.click()
	# signup_test.quit()

user_signup_test()
