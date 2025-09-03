from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

APP_URL = "http://localhost:5173"

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
