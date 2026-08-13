from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('http://localhost:8000')
    page.wait_for_timeout(2000)
    page.evaluate("document.querySelector('#theme-switcher').value = 'Styles/style-macos8.css'; document.querySelector('#theme-switcher').dispatchEvent(new Event('change'))")
    page.wait_for_timeout(1000)
    page.screenshot(path='screenshot.png')
    browser.close()
