from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

class driver_edge:
    def __init__(self):
        self.service = Service('C:\Git_sela\pythonProject\Browsers\msedgedriver.exe')
        self.driver = webdriver.Edge(service=self.service)

    def open_edge_brow(self,url:str)->bool:
        """
        function: Open Edge browser
        :param url : srt
        :return:True
        """
        self.driver.maximize_window()
        self.driver.get(url)
        return True


    def close_edge_brow(self)->bool:
        """
        function: Close Edge browser
        :return:bool: True
        """
        self.driver.quit()
        return True

    def login(self)->str:
        """
        function: Login
        :return:str: att_id
        """
        self.driver.find_element(By.CLASS_NAME, "login").click()
        self.driver.find_element(By.ID, "email").send_keys("admin11111@gmail.com")
        self.driver.find_element(By.ID, "passwd").send_keys("admin11111")
        login=self.driver.find_element(By.NAME,"SubmitLogin")
        att_id=login.get_attribute("id")
        login.click()
        return att_id

    def search_summer(self) ->str:
        """
        function:search
        :return:str:att_class
        """
        self.driver.find_element(By.XPATH,'//input[@id="search_query_top"]').send_keys("summer")
        button_search=self.driver.find_element(By.XPATH,'//button[@name="submit_search"]')
        att_class=button_search.get_attribute("type")
        button_search.click()
        return att_class

    def add_to_cart_summer_dress_min_price(self)->str:
        """
        function: Add the dress to the cart at a minimum price
        :return:str: min_price
        """
        div = self.driver.find_element(By.XPATH, '//div[@id="center_column"]')
        dresses=div.find_elements(By.XPATH,'//div[@class="right-block"]')
        url=div.find_elements(By.XPATH,'//a[@title="Add to cart"]')
        min_price=float(100)
        index=int(-1)
        for i in range(len(dresses)):
           price = float(dresses[i].text.split("\n")[1].split(" ")[0].replace("$",""))
           if price < min_price:
               min_price=price
               index = i
        self.driver.get(url[index].get_attribute('href'))
        return str(min_price)

    def pay_dress(self)->bool:
        """
        function: make payment
        :return:bool :True
        """
        self.driver.find_element(By.XPATH, '//a[@class="button btn btn-default standard-checkout button-medium"]').click()
        self.driver.find_element(By.XPATH, '//button[@class="button btn btn-default button-medium"]').click()
        self.driver.find_element(By.XPATH, '//input[@type="checkbox"]').click()
        self.driver.find_element(By.XPATH, '//button[@name="processCarrier"]').click()
        self.driver.find_element(By.XPATH, '//a[@class="bankwire"]').click()
        self.driver.find_element(By.XPATH, '//button[@class="button btn btn-default button-medium"]').click()
        return True







if __name__ == '__main__':
    browser = driver_edge()
    print(browser.open_edge_brow("http://automationpractice.com/index.php"))
    print(browser.login())
    print(browser.search_summer())
    print(browser.add_to_cart_summer_dress_min_price())
    print(browser.pay_dress())
    # browser.close_edge_brow()