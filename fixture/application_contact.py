from selenium import webdriver
from fixture.session import SessionHelper
from fixture.contact import ContactHelper

class Contact_Else:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/index.php")

    def new_contact(app):
        app.contact.new_contact()

    def create_new_contact(app):
        app.contact.create_new_contact()

    def destroy(self):
        self.driver.quit()