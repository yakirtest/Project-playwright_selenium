from playwright.sync_api import sync_playwright,Page

def login(page:Page)->str:
    """
    function: Login
    :param page: Page
    :return: str :title
    """
    title=page.title()
    page.locator('a[class="login"]').click()
    page.locator('input[id="email"]').fill('admin11111@gmail.com')
    page.locator('input[id="passwd"]').fill('admin11111')
    page.locator('button[id="SubmitLogin"]').click()
    return title

def search_summer(page:Page)->str:
    """
    function: search
    :param page: Page
    :return:str: summer
    """
    page.locator('input[id="search_query_top"]').fill('summer')
    page.locator('button[name="submit_search"]').click()
    summer=page.locator('span[class="lighter"]').text_content().replace("\n","").replace(" ","")
    return summer

def add_to_cart_and_pay(page:Page)->(str,str):
    """
     function: Add to cart and make payment
    :param page:Page
    :return:str: test_url, str: test_title
    """
    url_drees = page.locator('div[class="right-block"] >> a[data-id-product="7"]').get_attribute("href")
    page.goto(url_drees)
    test_url=str(page.url)
    page.locator('a[class="button btn btn-default standard-checkout button-medium"]').click()
    page.locator('button[name="processAddress"]').click()
    page.locator('div[class="checker"]').click()
    page.locator('button[name="processCarrier"]').click()
    page.locator('a[title="Pay by bank wire"]').click()
    page.locator('button[class="button btn btn-default button-medium"]').click()
    test_title=page.title()
    return test_url,test_title


if __name__ == '__main__':
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('http://automationpractice.com/index.php')
        login(page)
        search_summer(page)
        add_to_cart_and_pay(page)


