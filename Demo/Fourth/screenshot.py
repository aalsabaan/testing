import asyncio
import time
from pyppeteer import launch

async def main():
    browser = await launch()
    # browser = await launch({'headless': False})
    page = await browser.newPage()
    await page.goto('https://google.com')
    # time.sleep(5)
    await page.screenshot({'path': 'google.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())