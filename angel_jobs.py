from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import requests
import time
from dotenv import load_dotenv
import os

load_dotenv()
username = os.getenv("ANGEL_USER")
password = os.getenv("ANGEL_PASS")

# Open firefox and navigate to Angel List's log in page
driver = webdriver.Firefox()
driver.get("https://angel.co/login")
assert "Log In | AngelList" in driver.title
email_input = driver.find_element_by_id("user_email")
password_input = driver.find_element_by_id("user_password")

# log in
email_input.send_keys(username)
password_input.send_keys(password)
password_input.send_keys(Keys.RETURN)

time.sleep(1)

# navigate to jobs applied page
driver.get("https://angel.co/jobs/applied")

# wait for the page to load jobs
time.sleep(3)

# get list of applied jobs
links = driver.find_elements_by_class_name("startup-link")
locations = driver.find_elements_by_xpath(
    '//div[contains(@class, "tag") and contains(@class, "locations") and contains(@class, "tiptip")]')
company_sizes = driver.find_elements_by_xpath(
    '//div[contains(@class, "tag") and contains(@class, "employees")]')

number_of_jobs = len(links)
jobs = {}

# Construct job data
for index in range(number_of_jobs):
    link = links[index]
    name = link.text
    locationList = locations[index].text
    company_size = company_sizes[index].text

    jobs[name] = {
        "link": link.get_attribute('href'),
        "locations": locationList,
        "size": company_size
    }

print(jobs)
