from selenium import webdriver
from unittest import TestCase
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
import os
class AuthenticatedAutomatedTest(TestCase):
	def setUp(self):

		self.test_images_dir = os.path.join(os.getcwd(), 'images/test')
		chrome_options = Options()
		chrome_options.add_argument("--headless")

		self.driver = webdriver.Chrome(options=chrome_options)
		self.driver.implicitly_wait(10)
		self.driver.get('http://localhost:8000')

		login_elem = self.driver.find_element(By.XPATH, '//*[@id="root"]/header/nav/ul/li[2]/a')
		login_elem.click()

		uri = self.driver.current_url.split('/')[-2]
		assert uri == 'login'

		un_elem = self.driver.find_element(By.XPATH, '//*[@id="username-input"]')
		un_elem.send_keys('mk9')

		pw_elem = self.driver.find_element(By.XPATH, '//*[@id="password-input"]')
		pw_elem.send_keys('mk9')

		submit_elem = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form/input[2]')
		submit_elem.click()


	def test_google(self):
		driver = self.driver
		driver.get('http://google.com')

	def test_home_page(self):
		driver = self.driver
		driver.get('http://localhost:8000')

		uri = driver.current_url.split('/')[-1]
		assert uri == ''

	def test_home_page_attempt_access_upload(self):
		driver = self.driver
		driver.get('http://localhost:8000')

		uri = driver.current_url.split('/')[-1]
		assert uri == ''

		# Find upload button
		upload_elem = driver.find_element(By.XPATH,'//*[@id="root"]/header/nav/ul/li[1]/a' )
		upload_elem.click()
		uri = driver.current_url.split('/')[-2]
		assert uri == 'upload'

	def test_home_page_attempt_upload(self):
		driver = self.driver
		driver.get('http://localhost:8000/')

		uri = driver.current_url.split('/')[-1]
		assert uri == ''

		# Find upload button
		upload_elem = driver.find_element(By.XPATH,'//*[@id="root"]/header/nav/ul/li[1]/a' )
		upload_elem.click()
		uri = driver.current_url.split('/')[-2]
		assert uri == 'upload'

		title_elem = driver.find_element(By.XPATH, '//*[@id="id_title"]')
		upload_elem = driver.find_element(By.XPATH, '//*[@id="id_file"]')
		submit_elem = driver.find_element(By.XPATH, '/html/body/div/form/input[3]')

		assert title_elem != None
		assert upload_elem != None
		assert submit_elem != None
		
		title_elem.send_keys('My custom fashion piece')
		file = os.path.join(self.test_images_dir,'6372c4026a17ad72dc478014.jpg')
		upload_elem.send_keys(file)

		submit_elem.click()
		assert driver.current_url == 'http://localhost:8000/'

	def test_home_page_can_view_items(self):
		driver = self.driver
		driver.get('http://localhost:8000/')
		
		image_xpath = '//*[@id="root"]/div/div/div/div/div[1]/ul/div[1]/img'
		desc_container_xpath = '//*[@id="root"]/div/div/div/div/div[1]/ul/div[1]/div'

		image_elem = driver.find_element(By.XPATH, image_xpath)
		desc_container_elem = driver.find_element(By.XPATH, desc_container_xpath)

		assert image_elem != None
		assert desc_container_elem != None

	def test_home_page_can_view_item_labels(self):
		driver = self.driver
		driver.get('http://localhost:8000/')

		labels_xpath = '//*[@id="root"]/div/div/div/div/div[1]/ul/div[1]/div/div[1]/ul/li'
		labels_elem = driver.find_element(By.XPATH, labels_xpath)
		
		assert labels_elem != None


	def test_home_page_can_view_color_labels(self):
		driver = self.driver
		driver.get('http://localhost:8000/')

		colors_xpath = '//*[@id="root"]/div/div/div/div/div[1]/ul/div[1]/div/div[2]/ul/li[1]/div'
		colors_elem = driver.find_element(By.XPATH, colors_xpath)		
		
		assert colors_elem != None	

	def test_home_page_can_view_similar_items(self):
		driver = self.driver
		driver.get('http://localhost:8000/')

		select_button_xpath = '//*[@id="root"]/div/div/div/div/div[1]/ul/div[1]/div/div[4]/button'
		first_rec_image_xpath = '//*[@id="root"]/div/div/div/div/div[2]/div[2]/div[1]/img'
		
		select_button_elem = self.driver.find_element(By.XPATH, select_button_xpath)
		select_button_elem.click()

		first_rec_image = self.driver.find_element(By.XPATH, first_rec_image_xpath)
		assert first_rec_image != None


	def test_home_page_can_view_complementary_items(self):
		driver = self.driver
		driver.get('http://localhost:8000/')
		select_button_xpath = '//*[@id="root"]/div/div/div/div/div[1]/ul/div[1]/div/div[4]/button'
		first_complementary_item_xpath = '//*[@id="root"]/div/div/div/div/div[3]/div[2]/div[1]/img'

		select_button_elem = self.driver.find_element(By.XPATH, select_button_xpath)
		select_button_elem.click()
		first_complementary_item_elem = self.driver.find_element(By.XPATH, first_complementary_item_xpath)
		assert first_complementary_item_elem != None
	# def test_attempt_wardrobe(self):
	# 	driver = self.driver
	# 	driver.get('http://localhost:8000')
		


	# 	assert driver.current_url == 'http://localhost:8000/'

	# 	csrftoken = driver.get_cookie('csrftoken')
	# 	assert csrftoken != None
