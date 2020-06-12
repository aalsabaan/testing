import asyncio
import time
from pyppeteer import launch

async def main():
    browser = await launch({'headless': False})
    page = await browser.newPage()
    # open Website
    await page.goto('http://automationpractice.com')
    time.sleep(2)
    # go to login page
    await page.click('a[class="login"]')
    time.sleep(2)
    # write credentials to login and click login
    await page.type('input[id="email"]', 'ha@ha.com')
    await page.type('input[id="passwd"]', 'P@ssw0rd')
    time.sleep(2)
    await page.click('button[id="SubmitLogin"]')
    time.sleep(3)
    # check the user is redirect to profile page
    element = await page.querySelector('h1[class="page-heading"]')
    text = await page.evaluate('(element) => element.textContent', element)
    if "My account" not in text:
        raise ValueError('The user is not redirect to profile page')
    time.sleep(2)
    # go to women section 
    await page.click('a[title="Women"]')
    time.sleep(2)
    # add Faded Short Sleeve -blue- T-shirts to cart
    await page.click('a[title="Faded Short Sleeve T-shirts"]')
    time.sleep(2)
    await page.click('a[name="Blue"]')
    await page.click('button[class="exclusive"]')
    time.sleep(2)
    # check if Faded Short Sleeve -blue- T-shirts is in the cart or not
    await page.click('a[title="Proceed to checkout"]')
    time.sleep(2)
    element = await page.querySelector('h1[id="cart_title"]')
    text = await page.evaluate('(element) => element.textContent', element)
    if "Shopping-cart summary" not in text:
        raise ValueError('The user is not redirect to cart page')

    element = await page.querySelector('td[class="cart_description"]')
    text = await page.evaluate('(element) => element.textContent', element)
    if "Faded Short Sleeve T-shirts" not in text:
        raise ValueError('Faded Short Sleeve T-shirts is not in the cart')
    if "Color : Blue" not in text:
        raise ValueError('Different color is found')
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())