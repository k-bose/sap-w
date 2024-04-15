from browser import open_url_with_chrome, sign_in
import time

if __name__=="__main__":
    url = "http://172.31.1.203:8090/httpclient.html"
    while True:
        driver = open_url_with_chrome(url, True)
        if sign_in(driver):
            driver.quit()
        else:
            driver.quit()
        time.sleep(280)
