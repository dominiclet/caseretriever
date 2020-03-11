from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

#Username and Password for login
USERNAME = 
PASSWORD =

def settings():
        options = ChromeOptions()
        options.add_argument('--ignore-certificate-errors-spki-list')
        options.add_argument('--ignore-ssl-errors')
        options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        return options

def lawnet(q):
    driver.get('https://proxylogin.nus.edu.sg/lawproxy1/public/login.asp?logup=false&url=http://www.lawnet.sg/lawnet/ip-access')
    username = driver.find_element_by_name("user")
    username.send_keys(USERNAME)
    password = driver.find_element_by_name("pass")
    password.send_keys(PASSWORD)
    login = driver.find_element_by_xpath('//*[@id="main-content"]/table/tbody/tr/td/form/div/input')
    login.click()
    accept = driver.find_element_by_xpath('//*[@id="main-content"]/table/tbody/tr[2]/td[4]/div/form/input')
    accept.click()
    search = driver.find_element_by_name("basicSearchKey")
    search.send_keys(q)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="_searchbasicformportlet_WAR_lawnet3legalresearchportlet_bsfm"]/div[1]/ul/li[2]/a[1]')))
    search_button = driver.find_element_by_xpath('//*[@id="_searchbasicformportlet_WAR_lawnet3legalresearchportlet_bsfm"]/div[1]/ul/li[2]/a[1]')
    search_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tabs-1"]/div[3]/div[2]/div[2]/div[2]/h2/span/a')))
    case = driver.find_element_by_xpath('//*[@id="tabs-1"]/div[3]/div[2]/div[2]/div[2]/h2/span/a')
    case.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="dropPrint"]/ul/li[4]/a')))


def lexisnexis(q):
    driver.get('https://proxylogin.nus.edu.sg/libproxy1/public/login.asp?logup=false&url=https://advance.lexis.com/sgresearchhome/?pdmfid=1522471&identityprofileid=RHB5HS58401')
    domain = Select(driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[3]/td[4]/div[2]/form/table/tbody/tr[1]/td[2]/select'))
    domain.select_by_value("NUSSTU")
    username = driver.find_element_by_name("user")
    username.send_keys(USERNAME)
    password = driver.find_element_by_name("pass")
    password.send_keys(PASSWORD)
    login = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[3]/td[4]/div[2]/form/input[2]')
    login.click()
    # Some issues with the 'I Accept' button here so I used the hidden href redirect link
    accept = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[3]/td[4]/div/form/input[1]').get_attribute("value")
    driver.get(accept)
    # In LexisNexis now
    country = driver.find_element_by_xpath('//*[@id="9fvL9kk"]/section/span[1]/button')
    country.click()
    select_UK = driver.find_element_by_xpath('//*[@id="9fvL9kkcountrymenuzone"]/div[3]/div/div[2]/ul/li')
    select_UK.click()
    search_term = driver.find_element_by_xpath('//*[@id="searchTerms"]')
    # To deal with the white loading screen which renders everything uninteractable on page
    while True:
        try:
            search_term.click()
        except:
            print("EXCEPTION")
        else:
            break
    search_term.send_keys(q)
    search = driver.find_element_by_id('mainSearch')
    search.click()

if __name__ == "__main__":
    options = settings()
    while True:
        search_engine = input("'1' for Lawnet | '2' for Lexisnexis: ")
        if search_engine == ('1' or '2'):
            break
        else:
            print("You must either key in '1' or '2'!")
    q = input("Case citation: ")
    driver = WebDriver("/mnt/c/WebDriver/bin/chromedriver.exe", chrome_options=options)
    if search_engine == '1':
        lawnet(q)
    elif search_engine == '2':
        lexisnexis(q)
