import time

from behave import *
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from features.pages.login_page import LoginPage


@given('I navigate to admin-demo.nopcommerce.com')
def step_impl(context):
    # context.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    context.reg = LoginPage(context.driver)


@when('I open login page')
def step_impl(context):
    context.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2FAdmin")
    context.driver.maximize_window()
    time.sleep(5)


@then('I enter name "{user}"')
def step_impl(context, user):
    context.reg.enter_username(user)

@then('I enter password "{pwd}"')
def step_impl(context, pwd):
    context.reg.enter_password(pwd)

@then('I tap on login button')
def step_impl(context):
    context.reg.click_login_button()

