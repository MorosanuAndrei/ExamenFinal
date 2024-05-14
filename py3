from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I open the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.example.com")

@when('I search for "{search_term}"')
def step_impl(context, search_term):
    search_box = context.driver.find_element(By.NAME, "q")
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)

@then('I should see results related to "{search_term}"')
def step_impl(context, search_term):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "results"))
    )
    assert search_term in context.driver.page_source
    context.driver.quit()
