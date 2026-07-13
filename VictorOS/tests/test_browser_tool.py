from JarvisOS.services.tools.browser import BrowserTool

browser = BrowserTool()

browser.start()

browser.open_url("https://google.com")

input("Press Enter...")

browser.stop()