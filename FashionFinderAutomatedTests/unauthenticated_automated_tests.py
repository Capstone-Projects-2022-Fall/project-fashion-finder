from selenium import webdriver
from unittest import TestCase
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
class UnauthenticatedAutomatedTest(TestCase):
	def setUp(self):
		chrome_options = Options()
		chrome_options.add_argument("--headless")

		self.driver = webdriver.Chrome(options=chrome_options)



	def test_google(self):
		driver = self.driver
		driver.get('http://google.com')

	def test_home_page(self):
		driver = self.driver
		driver.get('http://localhost:8000')

		uri = driver.current_url.split('/')[-1]
		assert uri == ''

	def test_home_page_attempt_upload(self):
		driver = self.driver
		driver.get('http://localhost:8000')

		uri = driver.current_url.split('/')[-1]
		assert uri == ''

		# Find upload button
		upload_elem = driver.find_element(By.XPATH,'//*[@id="root"]/header/nav/ul/li[1]/a' )
		upload_elem.click()
		uri = driver.current_url.split('/')[-2]
		assert uri == 'login'

	def test_attempt_login(self):
		driver = self.driver
		driver.get('http://localhost:8000')
		
		login_elem = driver.find_element(By.XPATH, '//*[@id="root"]/header/nav/ul/li[2]/a')
		login_elem.click()

		uri = driver.current_url.split('/')[-2]
		assert uri == 'login'

		un_elem = driver.find_element(By.XPATH, '//*[@id="username-input"]')
		un_elem.send_keys('mk9')

		pw_elem = driver.find_element(By.XPATH, '//*[@id="password-input"]')
		pw_elem.send_keys('mk9')

		submit_elem = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form/input[2]')
		submit_elem.click()

		assert driver.current_url == 'http://localhost:8000/'

		csrftoken = driver.get_cookie('csrftoken')
		assert csrftoken != None
	
	def test_attempt_register(self):
		driver = self.driver
		driver.get('http://localhost:8000')
		
		register_elem = driver.find_element(By.XPATH, '//*[@id="root"]/header/nav/ul/li[3]/a')
		register_elem.click()

		un_xpath = '//*[@id="username-input"]'
		email_xpath = '//*[@id="email-input"]'
		fname_xpath = '//*[@id="fname-input"]'
		lname_xpath = '//*[@id="lname-input"]'
		pw_xpath = '//*[@id="password-input"]'
		pw_confirm_xpath = '//*[@id="confirm-input"]'
		submit_xpath = '//*[@id="root"]/div/div[2]/form/input[2]'
		
		un_elem = driver.find_element(By.XPATH, un_xpath)
		email_elem = driver.find_element(By.XPATH, email_xpath)
		fname_elem = driver.find_element(By.XPATH, fname_xpath)
		lname_elem = driver.find_element(By.XPATH, lname_xpath)
		pw_elem = driver.find_element(By.XPATH, pw_xpath)
		pw_confirm_elem = driver.find_element(By.XPATH, pw_confirm_xpath)
		submit_elem = driver.find_element(By.XPATH, submit_xpath)
		
		test_user_id = random.choice(range(0,10000,1))

		un_elem.send_keys('TestUser' + str(test_user_id))
		email_elem.send_keys('test_user_' + str(test_user_id) + '@gmail.com')
		fname_elem.send_keys('TestUserFName')
		lname_elem.send_keys('TestUserLName')
		pw_elem.send_keys('ExamplePassword1!')
		pw_confirm_elem.send_keys('ExamplePassword1!')
		submit_elem.click()

		assert driver.current_url == 'http://localhost:8000/'