import asyncio
import time
from pyppeteer import launch

async def main():
    browser = await launch({'headless': False})
    page = await browser.newPage()
    await page.goto('https://www.seleniumeasy.com')
    await page.click('a[href="http://www.seleniumeasy.com/test"]');
    time.sleep(2)
    await page.click('#btn_basic_example');
    time.sleep(50)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())