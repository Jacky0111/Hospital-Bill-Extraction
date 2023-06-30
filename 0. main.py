import pandas as pd
from time import sleep

from urllib.parse import urlparse

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException


def main():
    mi_care = pd.read_excel('micare_data.xlsx')

    url = 'https://eclaims.micaresvc.com'
    driver = setDriver()

    # Navigate to the login page
    driver.get(url)

    # Set the window size
    driver.set_window_size(2560, 1440)

    # Navigate to Login Page
    login_page = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="navbarCollapse"]/div[2]/button[2]'))
    )
    login_page.click()

    # Find the username and password input fields and enter your credentials
    username = driver.find_element(By.NAME, 'txtUserID')
    password = driver.find_element(By.NAME, 'txtPassword')
    username.send_keys('ALM000156')
    password.send_keys('newpassword')
    sleep(3)

    # Submit the login form
    login_btn = driver.find_element(By.ID, 'btnLogIn')
    login_btn.send_keys(Keys.RETURN)
    sleep(3)

    # Loop through the Claim No column using lambda function
    mi_care[['HospitalBillURL', 'Type']] = mi_care['ClaimNo'].apply(lambda x: pd.Series(retrieveURL(x, urlparse(url), driver)))

    mi_care.to_csv('data.csv', index=False)


def retrieveURL(n, parsed_url, browser):
    try:
        ref_no = None
        uploaded_type = None
        table_xpath = '//*[@id="dgResult"]/tbody/tr'
        ref_cell_xpath = '/td[2]'
        uploaded_cell_xpath = '/td[5]'
        target_type_list = ['FINAUTO', 'SYSTEMAUTO']
        claim_url = 'https://' + parsed_url.netloc + '/Hospital/Claim/uplHosClaimPrint.aspx?ClaimNo=' + n

        browser.get(claim_url)

        row_count = len(browser.find_elements(By.XPATH, '//table[@class="Datagrid"]//tr'))
        while row_count != 0:
            uploaded_row_path = table_xpath + '[' + str(row_count) + ']' + uploaded_cell_xpath
            uploaded_type = browser.find_element(By.XPATH, uploaded_row_path).text

            ref_row_path = table_xpath + '[' + str(row_count) + ']' + ref_cell_xpath
            ref_no = browser.find_element(By.XPATH, ref_row_path).text

            if uploaded_type not in target_type_list:
                ref_no = None
                uploaded_type = None
            elif uploaded_type == target_type_list[0]:
                break
            elif uploaded_type == target_type_list[1]:
                break

            row_count -= 1

        # sleep(3)

        bill_url = 'https://' + parsed_url.netloc + '/viewUploadedFiles.aspx?filename=' + ref_no + '.pdf' if ref_no is not None else None
        print(uploaded_type)
        print(claim_url)
        print(bill_url)

        return bill_url, uploaded_type

    except (NoSuchElementException, WebDriverException):
        return None, None


def setDriver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US',
                                              'download.prompt_for_download': False,
                                              'download.directory_upgrade': True,
                                              'plugins.plugins_disabled': ['Chrome PDF Viewer']
                                              })
    caps = DesiredCapabilities.CHROME
    browser = webdriver.Chrome(desired_capabilities=caps, options=options)
    return browser


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
