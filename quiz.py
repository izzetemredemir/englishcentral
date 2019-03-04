from selenium import webdriver
import time
import random
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get("https://tr.englishcentral.com/videos")
time.sleep(5)
giris_yap = browser.find_element_by_xpath("/html/body/header/div/ec-header-navigation/div[1]/nav/div[2]/div[2]/button")
giris_yap.click()
time.sleep(5)
username = browser.find_element_by_xpath("/html/body/header/div/ec-header-navigation/div[2]/ngb-modal-window/div/div/div[2]/ec-authentication-app/div/ec-login-app/div/form/div[1]/input")
password = browser.find_element_by_xpath("/html/body/header/div/ec-header-navigation/div[2]/ngb-modal-window/div/div/div[2]/ec-authentication-app/div/ec-login-app/div/form/div[2]/input")
username.send_keys("mail)
password.send_keys("sifre")
time.sleep(7)
giriş = browser.find_element_by_xpath("/html/body/header/div/ec-header-navigation/div[2]/ngb-modal-window/div/div/div[2]/ec-authentication-app/div/ec-login-app/div/form/div[3]/div/button")
giriş.click()
time.sleep(7)
browser.get("https://tr.englishcentral.com/courses/preview/4113")
quiz1 = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/div/ec-course-app/div/div/div[2]/div/ec-course-unit/div/div[2]/div[2]/div/div/div[6]/div/ec-course-unit-activity/div/ec-activity-thumbnail/div/div[3]")
quiz2 = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/div/ec-course-app/div/div/div[2]/div/ec-course-unit/div/div[2]/div[2]/div/div/div[7]/div/ec-course-unit-activity/div/ec-activity-thumbnail/div/div[3]")
quiz3 = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/div/ec-course-app/div/div/div[2]/div/ec-course-unit/div/div[2]/div[2]/div/div/div[8]/div/ec-course-unit-activity/div/ec-activity-thumbnail/div/div[3]")
quiz3.click()
time.sleep(6)
quize_başla = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/div/ec-course-app/div/div/div[3]/div/ec-activity-app/div/div[1]/div[1]/div[2]/div/ec-quiz-app/div/div/ec-quiz-start/div/div[2]/div/button")
quize_başla.click()
time.sleep(7)
soru_sayısı_yazısı = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/div/ec-course-app/div/div/div[3]/div/ec-activity-app/div/div[1]/div[1]/div[2]/div/ec-quiz-app/div/div/ec-quiz-question/div/div[2]/div[1]").text
soru_sayısı = int(soru_sayısı_yazısı.split()[3])
print(soru_sayısı)
i = 1
sözlük = {}
while(i <= soru_sayısı):
    soru_metni = '//*[@id="wrap"]/div[1]/div/div[1]/div/ec-course-app/div/div/div[3]/div/ec-activity-app/div/div[1]/div[1]/div[2]/div/ec-quiz-app/div/div/ec-quiz-question/div/div[1]/div[2]/div[2]/div[1]/div/ec-transcript/div'
    soru = str(browser.find_element_by_xpath(soru_metni).text)
    veri1 = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/div/ec-course-app/div/div/div[3]/div/ec-activity-app/div/div[1]/div[1]/div[2]/div/ec-quiz-app/div/div/ec-quiz-question/div/div[1]/div[2]/div[2]/div[2]/button[1]").text
    şık1 = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/div/ec-course-app/div/div/div[3]/div/ec-activity-app/div/div[1]/div[1]/div[2]/div/ec-quiz-app/div/div/ec-quiz-question/div/div[1]/div[2]/div[2]/div[2]/button[1]")
    sözlük[str(soru)]=[str(veri1)]
    şık1.click()
    time.sleep(8)
    i+=1

x=1
time.sleep(5)
e=1
while e <= 4:
    time.sleep(11)
    dogru_sayisi = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/div/ec-course-app/div/div/div[3]/div/ec-activity-app/div/div[1]/div[1]/div[2]/div/ec-quiz-app/div/div/ec-quiz-complete/div/div[2]/div[3]/div[4]/span[1]").text
    soru_sayısı = soru_sayısı - int(dogru_sayisi)
    print(soru_sayısı)
    quiz_yenile = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/div/ec-course-app/div/div/div[3]/div/ec-activity-app/div/div[1]/div[1]/div[2]/div/ec-quiz-app/div/div/ec-quiz-complete/div/div[2]/div[3]/div[6]/div/span")
    quiz_yenile.click()
    time.sleep(5)
    quize_başla = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/div/ec-course-app/div/div/div[3]/div/ec-activity-app/div/div[1]/div[1]/div[2]/div/ec-quiz-app/div/div/ec-quiz-start/div/div[2]/div/button")
    quize_başla.click()
    time.sleep(5)
    while x <= soru_sayısı:
        time.sleep(5)
        soru_metni = '//*[@id="wrap"]/div[1]/div/div[1]/div/ec-course-app/div/div/div[3]/div/ec-activity-app/div/div[1]/div[1]/div[2]/div/ec-quiz-app/div/div/ec-quiz-question/div/div[1]/div[2]/div[2]/div[1]/div/ec-transcript/div'
        soru = str(browser.find_element_by_xpath(soru_metni).text)
        veri1 = browser.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div/div[1]/div/ec-course-app/div/div/div[3]/div/ec-activity-app/div/div[1]/div[1]/div[2]/div/ec-quiz-app/div/div/ec-quiz-question/div/div[1]/div[2]/div[2]/div[2]/button[1]").text
        veri2 = browser.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div/div[1]/div/ec-course-app/div/div/div[3]/div/ec-activity-app/div/div[1]/div[1]/div[2]/div/ec-quiz-app/div/div/ec-quiz-question/div/div[1]/div[2]/div[2]/div[2]/button[2]").text
        veri3 = browser.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div/div[1]/div/ec-course-app/div/div/div[3]/div/ec-activity-app/div/div[1]/div[1]/div[2]/div/ec-quiz-app/div/div/ec-quiz-question/div/div[1]/div[2]/div[2]/div[2]/button[3]").text
        veri4 = browser.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div/div[1]/div/ec-course-app/div/div/div[3]/div/ec-activity-app/div/div[1]/div[1]/div[2]/div/ec-quiz-app/div/div/ec-quiz-question/div/div[1]/div[2]/div[2]/div[2]/button[4]").text
        şık1 = browser.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div/div[1]/div/ec-course-app/div/div/div[3]/div/ec-activity-app/div/div[1]/div[1]/div[2]/div/ec-quiz-app/div/div/ec-quiz-question/div/div[1]/div[2]/div[2]/div[2]/button[1]")
        şık2 = browser.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div/div[1]/div/ec-course-app/div/div/div[3]/div/ec-activity-app/div/div[1]/div[1]/div[2]/div/ec-quiz-app/div/div/ec-quiz-question/div/div[1]/div[2]/div[2]/div[2]/button[2]")
        şık3 = browser.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div/div[1]/div/ec-course-app/div/div/div[3]/div/ec-activity-app/div/div[1]/div[1]/div[2]/div/ec-quiz-app/div/div/ec-quiz-question/div/div[1]/div[2]/div[2]/div[2]/button[3]")
        şık4 = browser.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div/div[1]/div/ec-course-app/div/div/div[3]/div/ec-activity-app/div/div[1]/div[1]/div[2]/div/ec-quiz-app/div/div/ec-quiz-question/div/div[1]/div[2]/div[2]/div[2]/button[4]")
        döngü = sözlük[str(soru)]
        print(döngü)

        def kontrol(döngü, veri):
            i = 0
            while i < len(döngü):
                print(döngü[i])
                if str(döngü[i]) == str(veri):
                    return True
                else:
                    i += 1
        sorgu = kontrol(str(soru), str(veri1))
        sorgu2 = kontrol(str(soru), str(veri2))
        sorgu3 = kontrol(str(soru), str(veri3))
        sorgu4 = kontrol(str(soru), str(veri4))
        print(döngü)
        print(veri1)
        if sorgu != True:
            döngü.append(str(veri1))
            şık1.click()
            time.sleep(8)
            x += 1
            print("şık 1")
        else:
            if sorgu2 != True:
                şık2.click()
                time.sleep(8)
                print("şık 2")
                x += 1
            else:
                if sorgu3 != True:
                    şık3.click()
                    time.sleep(8)
                    print("şık 3")
                    x += 1
                else:
                    şık4.click()
                    time.sleep(8)
                    print("şık 4")
                    x += 1
    e+=1




