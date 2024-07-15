import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class TestLoginWithExistedAccount():
    @pytest.mark.login
    def login_with_existed_account(self):
        driver.get("https://www.amazon.in/")
        driver.implicitly_wait(10)
        element = driver.find_element(By.ID, "nav-link-accountList")
        element.click()
        time.sleep(10)
        user_Id = driver.find_element(By.ID, "ap_email_login")
        user_Id.send_keys("7286814512")
        driver.implicitly_wait(10)
        driver.find_element(By.ID, "continue").click()
        driver.implicitly_wait(5)
        Password = driver.find_element(By.ID, "ap_password")
        Password.send_keys("Praveen@1234")
        time.sleep(10)
        driver.implicitly_wait(10)
        signin = driver.find_element(By.ID, "signInSubmit")
        signin.click()
        time.sleep(20)


@pytest.mark.additems
class TestAddItemsToCart(TestLoginWithExistedAccount):
    def add_items_to_cart(self):
        """
        Overview : After Sign in Add at least  2 - 3 items to cart
        :return: cart should be filled
        """
        self.login_with_existed_account()
        self.cart_size_before_adding = driver.find_element(By.ID, 'nav-cart-count').text
        print("Cart size before adding ", self.cart_size_before_adding)
        driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Mobiles under 20000")
        driver.implicitly_wait(5)
        driver.find_element(By.ID, "nav-search-submit-button").click()
        driver.implicitly_wait(10)

        driver.execute_script("window.scrollBy(0, 200);")
        driver.implicitly_wait(5)
        driver.find_element(By.ID, "a-autoid-7-announce").click()
        driver.implicitly_wait(5)
        driver.execute_script("window.scrollBy(0, 300);")
        driver.implicitly_wait(5)
        driver.find_element(By.ID, "a-autoid-8-announce").click()
        driver.implicitly_wait(5)
        driver.execute_script("window.scrollBy(0, 400);")
        driver.implicitly_wait(5)
        driver.find_element(By.ID, "a-autoid-9-announce").click()
        time.sleep(10)

    def cart_size(self):
        # Check Items are added or not in cart
        driver.execute_script("window.scrollBy(0, 300);")
        self.cart_size_after_adding = driver.find_element(By.ID, 'nav-cart-count').text
        print("Cart size before adding ", self.cart_size_after_adding)
        total = len(self.cart_size_after_adding) - len(self.cart_size_before_adding)
        return total

    def test(self):
        if self.cart_size == 3:
            print("3 items are added to cart")
        else:
            print("failed to add items to cart")


@pytest.mark.emptycart
class TestEmptyTheCart(TestAddItemsToCart):
    def empty_cart(self):
        """
        3 items are ther in your cart empty the cart
        :return:
        """
        if self.cart_size() == 0 :
            self.add_items_to_cart()
        driver.find_element(By.ID, "nav-cart-text-container").click()
        driver.implicitly_wait(10)
        driver.execute_script("window.scrollBy(0, 150);")
        for i in range(self.cart_size()):
            driver.find_element(By.XPATH,
                                '//*[@id="sc-active-67c7297e-4ff1-45d3-a81d-4c936a3130c1"]/div[4]/div/div[3]/div[1]/span[2]/span/input').click()

        time.sleep(10)


@pytest.mark.sponsorrow
class TestSponsorRow(TestLoginWithExistedAccount):
    def check_sponsor_row(self):
        """
        Check Sponsor row in Web Page
        :return:
        """
        self.login_with_existed_account()
        driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Mobiles under 20000")
        driver.implicitly_wait(5)
        driver.find_element(By.ID, "nav-search-submit-button").click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '//*[@id="CardInstancenYBrN10FneBuO6h32ryZKw"]/a').is_displayed()
        time.sleep(10)
