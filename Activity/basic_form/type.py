import asyncio
import time
from pyppeteer import launch

async def main():
    browser = await launch({'headless': False})
    page = await browser.newPage()
    await page.goto('http://automationpractice.com/index.php')
    time.sleep(3)
    # await page.type('.search_query', 'Dress') # Types instantly
    time.sleep(3)
    await page.type('.search_query', 'Dress', {'delay': 200}) # Types slower, like a user
    await page.keyboard.press('Enter')
    time.sleep(3)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())