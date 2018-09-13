def create_event_test():
	from selenium import webdriver
	from faker import Faker
	import config

	create_event = webdriver.Firefox()
	create_event.get('https://secure-garden-12181.herokuapp.com')

	create_event.find_element_by_link_text('Login').click()
	login = create_event.find_element_by_name("username")
	password = create_event.find_element_by_name("password")
	login.send_keys(config.VIA_Username)
	password.send_keys(config.VIA_Password)

	create_event.find_element_by_name('login').click()
	create_event.find_element_by_link_text('Create Event').click()
	data = Faker()
	event = [data.sentence(),f'3454 {data.word()} Ave N', data.city(), data.state(), 55422, 45]

	index = 0
	for x in range(1,7):
		field = create_event.find_element_by_xpath(f"//form[@id='msform']/fieldset/input[{x}]")
		field.send_keys(event[index])
		index += 1

	next_button = create_event.find_element_by_xpath("//form[@id='msform']/fieldset[1]/input[@class='next action-button']")
	next_button.click()

	description = create_event.find_element_by_xpath("//form[@id='msform']/fieldset[2]/textarea[@id='inputDescription']")
	description.send_keys(event[0])

	create_event.implicitly_wait(2)
	
	next_button2 = create_event.find_element_by_xpath("//form/fieldset[2]/input[2]")
	create_event.implicitly_wait(5)
	next_button2.click()
	# create_event.quit()

create_event_test()