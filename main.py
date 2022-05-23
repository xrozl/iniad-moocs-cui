import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager 

option: Options = Options()
option.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
print("Loading login page...")
driver.get('https://moocs.iniad.org/auth/iniad')
time.sleep(4)
username: str = input('Username: ')
password: str = input('Password: ')
driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[2]/div/form/fieldset/div[1]/input').send_keys(username)
driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[2]/div/form/fieldset/div[2]/input').send_keys(password)
driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[2]/div/form/fieldset/div[4]/input').click()
time.sleep(5)
if driver.title == "INIAD ID Manager":
    print("Login Failed")
    exit()
else:
    print("Login Success")
    time.sleep(1)
driver.find_element(by=By.XPATH, value='/html/body/div/div/div[2]/div/form/fieldset/div[2]/div[1]/button[2]').click()
time.sleep(1)
page = 0
while True:
    medias: list = driver.find_elements(by=By.CLASS_NAME, value="media-heading")
    links: list = driver.find_elements(by=By.TAG_NAME, value="a")[8:]
    count = 0
    for i in range(page * 10, len(medias)):
        if count == 10:
            break
        count += 1
        print(str(i) + ": " + medias[i].text)
    print("Next: n", "Prev: p", "Exit: e")
    print("Page: " + str(page) + " / " + str(len(medias) // 10))
    user_input: str = input("Select course: ")
    if user_input == "e":
        print("Good Bye!")
        exit()
    elif user_input == "n":
        if page == len(medias) // 10:
            print("no more page")
            continue
        page += 1
        continue
    elif user_input == "p":
        if page == 0:
            print("No more page")
            continue
        page -= 1
        continue
    elif user_input.isdigit():
        try:
            print(medias[int(user_input)].text)
            print(links[int(user_input)].get_attribute("href"))
            continue
        except:
            print("Invalid input")
            continue
    time.sleep(100)
