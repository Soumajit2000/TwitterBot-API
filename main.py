from selenium import webdriver
# Add client side inputs to the UI
from selenium.webdriver.common.keys import Keys
import time

# copy the X_Path of the username,password and login button using inspect_element
email_xpath = '/html/body/div/div/div/div/main/div/div/div/div[1]/div[1]/div/form/div/div[1]/div/label/div/div[2]/div/input/html/body/div/div/div/div/main/div/div/div/div[1]/div[1]/div/form/div/div[1]/div/label/div/div[2]/div/input'
password_xpath = '/html/body/div/div/div/div/main/div/div/div/div[1]/div[1]/div/form/div/div[2]/div/label/div/div[2]/div/input'
login_xpath = '/html/body/div/div/div/div/main/div/div/div/div[1]/div[1]/div/form/div/div[3]/div/div/span/span'
tweets_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[11]/div/div/article/div/div'


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()  # open links, pages and tabs in firefox browser

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)
        email = bot.find_element_by_xpath(email_xpath)
        password = bot.find_element_by_xpath(password_xpath)
        login_button = bot.find_element_by_xpath(login_xpath)
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
        login_button.click()
        login_button1 = bot.find_element_by_xpath(login_xpath)
        login_button1.click()

    def like_tweets(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typed_query')
        time.sleep(3)
        for i in range(1, 3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            tweets = bot.find_elements_by_xpath(tweets_xpath)
            links = [elem.get_attribute('data-permalink-path')
                     for elem in tweets]
            print(links)
            for link in links:
                bot.get('https://twitter.com' + link)
                try:
                    bot.find_elements_by_class_name('Heartanimation').click()
                    time.sleept(10)
                except Exception as ex:
                    time.sleept(60)


dev = TwitterBot('username', 'password')
dev.login()
dev.like_tweets('webdevelopment')
