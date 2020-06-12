import asyncio
import time
from pyppeteer import launch

async def main():
    browser = await launch({'headless': False})
    page = await browser.newPage()
    await page.goto('http://automationpractice.com/index.php')
    time.sleep(3)
    element = await page.querySelector('span[class="shop-phone"]')
    text = await page.evaluate('(element) => element.textContent', element)
    # await page.waitForSelector('span[class="shop-phone"]', { 'timeout': 1000 })
    if "0123-456-789" not in text:
        raise ValueError('Phone number on the website is not correct')
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())