from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from spec import *
from dotenv import load_dotenv
import os
import time
    
def Login(driver):
    # env = "https://testnet.btse.io"
    env = "https://staging.oa.btse.io"
    driver.get(f"{env}/en/login")
    load_dotenv()
    driver.find_element(By.XPATH,"//input[@class='input-inline-input']").send_keys(os.getenv('username'))
    driver.find_element(By.XPATH,"//div[@class='flex-box flex-column justify-center'][2]//input[@class='input-inline-input']").send_keys(os.getenv('passward'))
    time.sleep(1)
    driver.find_element(By.XPATH,"//button[@class='w-100 btse-button inline-flex flex-row justify-center items-center border-box button-type--confirm button-size--bigger']").click()
    time.sleep(1)
    driver.get(f"{env}/en/trading/BTC-USD")

def ChangeCoin(driver):
    # icon/search
    ele = driver.find_element(By.XPATH,"//div[@class='market-menu__button']")
    ActionChains(driver).move_to_element(ele).perform()
    driver.find_element(By.XPATH,"//input[@class='market-search-input']").send_keys(New_Coin)
    driver.find_element(By.XPATH,"//div[@class='market-name__text text-main']").click()

def USD(driver):
    
    # SupportedQuoteCoins 
    ele = driver.find_element(By.XPATH,"//header[@class='header no-select']")
    ActionChains(driver).move_to_element(ele).perform()
    driver.find_element(By.XPATH,"//div[@class='action-wrap']").click()
    time.sleep(2)
    # limit buy
    min_price = driver.find_element(By.XPATH,"//input[@class='w-70 border-none tx-align--right input']")
    ActionChains(driver).double_click(min_price).perform()
    min_price.send_keys(Keys.DELETE)
    min_price.send_keys(minValidPrice)
    min_size = driver.find_element(By.XPATH,"//div[@class='__form_item']//input")
    ActionChains(driver).click(min_size).perform()
    min_size.send_keys(minOrderSize)
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()
    # market buy
    driver.find_element(By.XPATH,"//li[@class='-item'][1]/span").click()
    driver.find_element(By.XPATH,"//input[@class='w-70 border-none tx-align--right input']").send_keys('100')
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()
    # oco buy
    driver.find_element(By.XPATH,"//li[@class='-item'][2]/span").click()
    driver.find_element(By.XPATH,"//input[@id='spotOcoPriceInput']").send_keys(minValidPrice)
    driver.find_element(By.XPATH,"//input[@id='spotOcoStopPriceInput']").send_keys(big_price)
    driver.find_element(By.XPATH,"//input[@id='spotOcoSizeInput']").send_keys(minOrderSize)
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()
    # index buy
    driver.find_element(By.XPATH,"//li[@class='-item'][3]/span").click()
    index_price = driver.find_element(By.XPATH,"//div[@class='input--container flex-box justify-between items-center'][1]//input")
    ActionChains(driver).double_click(index_price).perform()
    index_price.send_keys(Keys.DELETE)
    index_price.send_keys(minValidPrice)
    driver.find_element(By.XPATH,"//div[@class='input--container flex-box justify-between items-center'][2]//input").send_keys(minOrderSize)
    driver.find_element(By.XPATH,"//div[@class='input--container flex-box justify-between items-center'][3]//input").send_keys('10')
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()
    # limit sell
    driver.find_element(By.XPATH,"//div[@class='spot-order-type-tab sell']").click()
    driver.find_element(By.XPATH,"//li[@class='-item'][1]/span").click()
    price = driver.find_element(By.XPATH,"//input[@class='w-70 border-none tx-align--right input']")
    ActionChains(driver).double_click(price).perform()
    price.send_keys(Keys.DELETE)
    price.send_keys(big_price)
    min_size = driver.find_element(By.XPATH,"//div[@class='__form_item']//input")
    ActionChains(driver).click(min_size).perform()
    min_size.send_keys(minOrderSize)
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()
    # market sell
    driver.find_element(By.XPATH,"//li[@class='-item'][1]/span").click()
    driver.find_element(By.XPATH,"//input[@class='w-70 border-none tx-align--right input']").send_keys(minOrderSize)
    time.sleep(1)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()
    # oco sell
    driver.find_element(By.XPATH,"//li[@class='-item'][2]/span").click()
    driver.find_element(By.XPATH,"//input[@id='spotOcoPriceInput']").send_keys(big_price)
    driver.find_element(By.XPATH,"//input[@id='spotOcoStopPriceInput']").send_keys(minValidPrice)
    driver.find_element(By.XPATH,"//input[@id='spotOcoSizeInput']").send_keys(minOrderSize)
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()
    # index sell
    driver.find_element(By.XPATH,"//li[@class='-item'][3]/span").click()
    index_price = driver.find_element(By.XPATH,"//div[@class='input--container flex-box justify-between items-center'][1]//input")
    ActionChains(driver).double_click(index_price).perform()
    index_price.send_keys(Keys.DELETE)
    index_price.send_keys(big_price)
    driver.find_element(By.XPATH,"//div[@class='input--container flex-box justify-between items-center'][2]//input").send_keys(minOrderSize)
    driver.find_element(By.XPATH,"//div[@class='input--container flex-box justify-between items-center'][3]//input").send_keys('10')
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()
    
def BTC(driver):
    try:
        # Change to BTC
        ele = driver.find_element(By.XPATH,"//header[@class='header no-select']")
        ActionChains(driver).move_to_element(ele).perform()
        driver.find_element(By.XPATH,"//div[@class='action-wrap']").click()
        driver.find_element(By.XPATH,"//div[@class='options-block-container'][2]/div[@class='options']/div[1]").click()
        driver.find_element(By.XPATH,"//div[@class='spot-order-type-tab buy']").click()
        driver.find_element(By.XPATH,"//li[@class='-item'][1]/span").click()
    except:
        pass
    # limit buy
    min_price = driver.find_element(By.XPATH,"//input[@class='w-70 border-none tx-align--right input']")
    ActionChains(driver).double_click(min_price).perform()
    min_price.send_keys(Keys.DELETE)
    time.sleep(2)
    min_price.send_keys(quote_BTC_minValidPrice)
    min_size = driver.find_element(By.XPATH,"//div[@class='__form_item']//input")
    ActionChains(driver).click(min_size).perform()
    min_size.send_keys(minOrderSize)
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()

    # market buy
    driver.find_element(By.XPATH,"//li[@class='-item'][1]/span").click()
    driver.find_element(By.XPATH,"//input[@class='w-70 border-none tx-align--right input']").send_keys(quote_BTC_minValidPrice)
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()
    # oco buy
    driver.find_element(By.XPATH,"//li[@class='-item'][2]/span").click()
    driver.find_element(By.XPATH,"//input[@id='spotOcoPriceInput']").send_keys(quote_BTC_minValidPrice)
    driver.find_element(By.XPATH,"//input[@id='spotOcoStopPriceInput']").send_keys(big_price)
    driver.find_element(By.XPATH,"//input[@id='spotOcoSizeInput']").send_keys(minOrderSize)
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()
    # index buy
    driver.find_element(By.XPATH,"//li[@class='-item'][3]/span").click()
    index_price = driver.find_element(By.XPATH,"//div[@class='input--container flex-box justify-between items-center'][1]//input")
    ActionChains(driver).double_click(index_price).perform()
    index_price.send_keys(Keys.DELETE)
    index_price.send_keys(minValidPrice)
    driver.find_element(By.XPATH,"//div[@class='input--container flex-box justify-between items-center'][2]//input").send_keys(minOrderSize)
    driver.find_element(By.XPATH,"//div[@class='input--container flex-box justify-between items-center'][3]//input").send_keys('10')
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()
    # limit sell
    driver.find_element(By.XPATH,"//div[@class='spot-order-type-tab sell']").click()
    driver.find_element(By.XPATH,"//li[@class='-item'][1]/span").click()
    price = driver.find_element(By.XPATH,"//input[@class='w-70 border-none tx-align--right input']")
    ActionChains(driver).double_click(price).perform()
    price.send_keys(Keys.DELETE)
    price.send_keys(big_price)
    min_size = driver.find_element(By.XPATH,"//div[@class='__form_item']//input")
    ActionChains(driver).click(min_size).perform()
    min_size.send_keys(minOrderSize)
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()
    # market sell
    driver.find_element(By.XPATH,"//li[@class='-item'][1]/span").click()
    driver.find_element(By.XPATH,"//input[@class='w-70 border-none tx-align--right input']").send_keys(minOrderSize)
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()
    # oco sell
    driver.find_element(By.XPATH,"//li[@class='-item'][2]/span").click()
    driver.find_element(By.XPATH,"//input[@id='spotOcoPriceInput']").send_keys(big_price)
    driver.find_element(By.XPATH,"//input[@id='spotOcoStopPriceInput']").send_keys(quote_BTC_minValidPrice)
    driver.find_element(By.XPATH,"//input[@id='spotOcoSizeInput']").send_keys(minOrderSize)
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()
    # index sell
    driver.find_element(By.XPATH,"//li[@class='-item'][3]/span").click()
    index_price = driver.find_element(By.XPATH,"//div[@class='input--container flex-box justify-between items-center'][1]//input")
    ActionChains(driver).double_click(index_price).perform()
    index_price.send_keys(Keys.DELETE)
    index_price.send_keys(big_price)
    driver.find_element(By.XPATH,"//div[@class='input--container flex-box justify-between items-center'][2]//input").send_keys(minOrderSize)
    driver.find_element(By.XPATH,"//div[@class='input--container flex-box justify-between items-center'][3]//input").send_keys('10')
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()
    
def ETH(driver):
    try:
        # Change to ETH
        ele = driver.find_element(By.XPATH,"//header[@class='header no-select']")
        ActionChains(driver).move_to_element(ele).perform()
        driver.find_element(By.XPATH,"//div[@class='action-wrap']").click()
        driver.find_element(By.XPATH,"//div[@class='options-block-container'][2]/div[@class='options']/div[2]").click()
        driver.find_element(By.XPATH,"//div[@class='spot-order-type-tab buy']").click()
        driver.find_element(By.XPATH,"//li[@class='-item'][1]/span").click()
    except:
        pass
    # limit buy
    min_price = driver.find_element(By.XPATH,"//input[@class='w-70 border-none tx-align--right input']")
    ActionChains(driver).double_click(min_price).perform()
    min_price.send_keys(Keys.DELETE)
    time.sleep(1)
    min_price.send_keys(quote_ETH_minValidPrice)
    driver.find_element(By.XPATH,"//div[@class='__form_item']//input").send_keys(minOrderSize)
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()

    # market buy
    driver.find_element(By.XPATH,"//li[@class='-item'][1]/span").click()
    driver.find_element(By.XPATH,"//input[@class='w-70 border-none tx-align--right input']").send_keys(quote_ETH_minValidPrice)
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()
    # oco buy
    driver.find_element(By.XPATH,"//li[@class='-item'][2]/span").click()
    driver.find_element(By.XPATH,"//input[@id='spotOcoPriceInput']").send_keys(quote_ETH_minValidPrice)
    driver.find_element(By.XPATH,"//input[@id='spotOcoStopPriceInput']").send_keys(big_price)
    driver.find_element(By.XPATH,"//input[@id='spotOcoSizeInput']").send_keys(minOrderSize)
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()
    # index buy
    driver.find_element(By.XPATH,"//li[@class='-item'][3]/span").click()
    index_price = driver.find_element(By.XPATH,"//div[@class='input--container flex-box justify-between items-center'][1]//input")
    ActionChains(driver).double_click(index_price).perform()
    index_price.send_keys(Keys.DELETE)
    time.sleep(1)
    index_price.send_keys(minValidPrice)
    driver.find_element(By.XPATH,"//div[@class='input--container flex-box justify-between items-center'][2]//input").send_keys(minOrderSize)
    driver.find_element(By.XPATH,"//div[@class='input--container flex-box justify-between items-center'][3]//input").send_keys('10')
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()
    # limit sell
    driver.find_element(By.XPATH,"//div[@class='spot-order-type-tab sell']").click()
    driver.find_element(By.XPATH,"//li[@class='-item'][1]/span").click()
    price = driver.find_element(By.XPATH,"//input[@class='w-70 border-none tx-align--right input']")
    ActionChains(driver).double_click(price).perform()
    price.send_keys(Keys.DELETE)
    price.send_keys(big_price)
    min_size = driver.find_element(By.XPATH,"//div[@class='__form_item']//input")
    ActionChains(driver).click(min_size).perform()
    min_size.send_keys(minOrderSize)
    time.sleep(3)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()
    # market sell
    driver.find_element(By.XPATH,"//li[@class='-item'][1]/span").click()
    driver.find_element(By.XPATH,"//input[@class='w-70 border-none tx-align--right input']").send_keys(minOrderSize)
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()
    # oco sell
    driver.find_element(By.XPATH,"//li[@class='-item'][2]/span").click()
    driver.find_element(By.XPATH,"//input[@id='spotOcoPriceInput']").send_keys(big_price)
    driver.find_element(By.XPATH,"//input[@id='spotOcoStopPriceInput']").send_keys(quote_ETH_minValidPrice)
    driver.find_element(By.XPATH,"//input[@id='spotOcoSizeInput']").send_keys(minOrderSize)
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()
    # index sell
    driver.find_element(By.XPATH,"//li[@class='-item'][3]/span").click()
    index_price = driver.find_element(By.XPATH,"//div[@class='input--container flex-box justify-between items-center'][1]//input")
    ActionChains(driver).double_click(index_price).perform()
    index_price.send_keys(Keys.DELETE)
    index_price.send_keys(big_price)
    driver.find_element(By.XPATH,"//div[@class='input--container flex-box justify-between items-center'][2]//input").send_keys(minOrderSize)
    driver.find_element(By.XPATH,"//div[@class='input--container flex-box justify-between items-center'][3]//input").send_keys('10')
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[@class='button-content']").click()
    

def CancelOrder(driver):
    # cancel order
    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
    driver.find_element(By.XPATH,"//div[@class='cancel-panel-content']//span[@class='button-content']").click()
    driver.find_element(By.XPATH,"//div[@class='cancel-panel-content']//button[1]/span").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//div[@class='cancel-panel']//button/span").click()
    driver.find_element(By.XPATH,"//div[@class='el-message-box__btns']/button[2]").click()
    time.sleep(2)
    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_UP)

def OTC(driver):
    driver.find_element(By.XPATH,"//a[@class='navigation-link hover-effect'][1]").click()
    time.sleep(4)

    # fiat buy
    driver.find_element(By.XPATH,"//div[@class='action-wrapper'][1]//div[@class='drop-down-wrap']/button").click()
    search = ActionChains(driver)
    search.send_keys(New_Coin).perform()
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[@class='action-wrapper'][1]//div[@class='currency-card flex-1 flex-box items-center']").click()
    driver.find_element(By.XPATH,"//div[@class='action-wrapper'][1]//input").send_keys("1")
    driver.find_element(By.XPATH,"//div[@class='otc-panel-footer']/span").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[@class='otc-timeline-text buy']/span").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//div[@class='otc-popup-footer']/span[@class='otc-button']").click()

    # crypto buy
    driver.find_element(By.XPATH,"//div[@class='action-wrapper'][2]//div[@class='drop-down-wrap']/button").click()
    search = ActionChains(driver)
    search.send_keys(crypto).perform()
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[@class='action-wrapper'][2]//div[@class='currency-card flex-1 flex-box items-center']").click()
    driver.find_element(By.XPATH,"//div[@class='otc-panel-footer']/span").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[@class='otc-timeline-text buy']/span").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//div[@class='otc-popup-footer']/span[@class='otc-button']").click()

    # stablecoin buy
    driver.find_element(By.XPATH,"//div[@class='action-wrapper'][2]//div[@class='drop-down-wrap']/button").click()
    search = ActionChains(driver)
    search.send_keys(stablecoin).perform()
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[@class='action-wrapper'][2]//div[@class='currency-card flex-1 flex-box items-center']").click()
    driver.find_element(By.XPATH,"//div[@class='otc-panel-footer']/span").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[@class='otc-timeline-text buy']/span").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//div[@class='otc-popup-footer']/span[@class='otc-button']").click()

    # change to sell
    driver.find_element(By.XPATH,"//div[@class='tab item-sell']").click() 
    time.sleep(2)

    # fiat sell
    driver.find_element(By.XPATH,"//div[@class='action-wrapper'][2]//div[@class='drop-down-wrap']/button").click()
    search = ActionChains(driver)
    search.send_keys(fiat).perform()
    time.sleep(1)
    driver.find_element(By.XPATH,"//button[@class='filter-button'][1]").click()
    driver.find_element(By.XPATH,"//div[@class='action-wrapper'][2]//div[@class='currency-card flex-1 flex-box items-center']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[@class='otc-panel-footer']/span").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[@class='otc-timeline-text sell']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//div[@class='otc-popup-footer']/span[@class='otc-button']").click()

    # crypto sell
    driver.find_element(By.XPATH,"//div[@class='action-wrapper'][2]//div[@class='drop-down-wrap']/button").click()
    search = ActionChains(driver)
    search.send_keys(crypto).perform()
    driver.find_element(By.XPATH,"//button[@class='filter-button'][1]").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[@class='action-wrapper'][2]//div[@class='currency-card flex-1 flex-box items-center']").click()
    
    driver.find_element(By.XPATH,"//div[@class='otc-panel-footer']/span").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[@class='otc-timeline-text sell']/span").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//div[@class='otc-popup-footer']/span[@class='otc-button']").click()

    # stablecoin sell
    driver.find_element(By.XPATH,"//div[@class='action-wrapper'][2]//div[@class='drop-down-wrap']/button").click()
    search = ActionChains(driver)
    search.send_keys(stablecoin).perform()
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[@class='action-wrapper'][2]//div[@class='currency-card flex-1 flex-box items-center']").click()

    driver.find_element(By.XPATH,"//div[@class='otc-panel-footer']/span").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//div[@class='otc-timeline-text sell']/span").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//div[@class='otc-popup-footer']/span[@class='otc-button']").click()



def main():
    option = webdriver.ChromeOptions()
    path = Service("./chromedriver")
    driver = webdriver.Chrome(service=path,options=option)
    driver.maximize_window()
    Login(driver)
    ChangeCoin(driver)
    USD(driver)
    BTC(driver)
    ETH(driver)
    CancelOrder(driver)
    OTC(driver)
    time.sleep(3)
    driver.quit()

main()