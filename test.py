from selenium import  webdriver
from selenium.webdriver.support.ui import  Select
import time
from gtts import gTTS
import os
import random
import playsound
from selenium.webdriver.common.keys import Keys
dede = r'C:\Users\Emre\AppData\Roaming\Mozilla\Firefox\Profiles\6sj71gbw.default'
profile = webdriver.FirefoxProfile(dede)
browser = webdriver.Firefox(profile)
url = "https://tr.englishcentral.com/videos"
browser.get(url)
time.sleep(7)
uye_button = browser.find_element_by_xpath("/html/body/header/div/ec-header-navigation/div[1]/nav/div[2]/div[2]/button")
uye_button.click()
time.sleep(7)
giris_mail = browser.find_element_by_xpath("/html/body/header/div/ec-header-navigation/div[2]/ngb-modal-window/div/div/div[2]/ec-authentication-app/div/ec-login-app/div/form/div[1]/input")
giris_mail.send_keys("mail")
giris_pass = browser.find_element_by_xpath("/html/body/header/div/ec-header-navigation/div[2]/ngb-modal-window/div/div/div[2]/ec-authentication-app/div/ec-login-app/div/form/div[2]/input")
giris_pass.send_keys("sifre")
giris_button = browser.find_element_by_xpath("/html/body/header/div/ec-header-navigation/div[2]/ngb-modal-window/div/div/div[2]/ec-authentication-app/div/ec-login-app/div/form/div[3]/div/button")
giris_button.click()
time.sleep(7)
url2 = "https://tr.englishcentral.com/courses/preview/4113"
browser.get(url2)
time.sleep(6)
unit_button = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/div/ec-course-app/div/div/div[3]/div/ec-activity-app/div/div[1]/div[2]/ec-activity-list/div/div[3]")
unit_button.click()
time.sleep(2)
uniteler = len(list(browser.find_elements_by_css_selector(".unit-name")))
unit_button = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/div/ec-course-app/div/div/div[2]/div/ec-course-unit/div/div[1]/div[2]/div/div["+str(uniteler)+"]/a/span")
unit_button.click()
time.sleep(3)
i=5
while i <= 5:
    video_button = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/div/ec-course-app/div/div/div[2]/div/ec-course-unit/div/div[2]/div[2]/div/div/div[" + str(i) + "]/div/ec-course-unit-activity/div/ec-activity-thumbnail/div/div[3]")
    video_button.click()
    time.sleep(8)
    oldstr = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/div/ec-course-app/div/div/div[3]/div/ec-activity-app/div/div[1]/div[1]/div[2]/ec-player-app/div/div/div/div[4]/div[5]/span[2]").text
    sure = oldstr.replace("/ ", "")
    dk = int((int(sure.split(":")[0]) * 60) + int(sure.split(":")[1]))
    print(dk)
    #time.sleep(dk)
    time.sleep(9)
    sorulara_geçiş = browser.find_element_by_xpath("//*[@id='wrap']/div[1]/div/div[1]/div/ec-course-app/div/div/div[3]/div/ec-activity-app/div/div[1]/div[1]/div[2]/ec-comprehension-quiz-app/div/div/div[2]/div[2]/button[1]")
    sorulara_geçiş.click()
    konus_button = browser.find_element_by_xpath(
        "/html/body/div[2]/div[1]/div/div[1]/div/ec-course-app/div/div/div[3]/div/ec-activity-app/div/div[1]/div[2]/ec-activity-list/div/div[3]")
    konus_button.click()
    kelime1 = browser.find_element_by_xpath(
        "/html/body/div[2]/div[1]/div/div[1]/div/ec-course-app/div/div/div[3]/div/ec-activity-app/div/div[1]/div[1]/div[3]/ec-activity-interstitial/div/div/div[2]/ec-speak-interstitial/div/div/div[2]/div/button[2]").text
    kelimeler = int(kelime1.split("Seçilen: ")[1])
    print(kelimeler)
    x = 1
    konus_basla_button = browser.find_element_by_xpath(
        "/html/body/div[2]/div[1]/div/div[1]/div/ec-course-app/div/div/div[3]/div/ec-activity-app/div/div[1]/div[1]/div[3]/ec-activity-interstitial/div/div/div[2]/ec-speak-interstitial/div/div/div[4]/span")
    konus_basla_button.click()
    while x <= kelimeler:
        time.sleep(4)
        konus_metin_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div/div[1]/div/ec-course-app/div/div/div[3]/div/ec-activity-app/div/div[1]/div[1]/div[3]/ec-activity-interstitial/div/div/div[2]/ec-speak-interstitial/div/div/div[4]/span")
        time.sleep(4)
        konusma_metin_yazi = browser.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div/div[1]/div/ec-course-app/div/div/div[3]/div/ec-activity-app/div/div[1]/div[1]/div[2]/ec-player-app/div/div/div/div[2]/div/ec-player-transcript/div/div[1]/div/div").text
        print(konusma_metin_yazi)

        def fetch():
            language = 'en'
            myob = gTTS(text=mytext.get(), lang=language, slow=False)
            myob.save('Voice' + str(x) + '.mp3')
        tts = gTTS(text=konusma_metin_yazi, lang='en')
        tts.save("Voice" + str(x) +"-"+ str(i) +".mp3")
        time.sleep(1)
        oynat_button = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/div/ec-course-app/div/div/div[3]/div/ec-activity-app/div/div[1]/div[1]/div[2]/ec-player-app/div/div/div/div[1]/div[2]/ec-speak-mode/div/ec-speak-mode-mic/div[2]/div/div")
        oynat_button.click()


        playsound.playsound('Voice' + str(x) + '-'+ str(i) +'.mp3', True)
        os.remove("Voice" + str(x) +"-"+ str(i) +".mp3")
        oynat_durdur = browser.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div/div[1]/div/ec-course-app/div/div/div[3]/div/ec-activity-app/div/div[1]/div[1]/div[2]/ec-player-app/div/div/div/div[1]/div[2]/ec-speak-mode/div/ec-speak-mode-mic/div[2]/div/div/div")
        oynat_durdur.click()
        time.sleep(5)
        x += 1
    time.sleep(4)
    i += 1


