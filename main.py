import requests
import datetime
from bs4 import BeautifulSoup
import time



DOLLAR_RUB = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&aqs=edge..69i57j0i131i433i512j0i433i512j0i131i433j0i433i512l4.2191j0j1&sourceid=chrome&ie=UTF-8"
EURO_RUB = "https://www.google.com/search?q=%D0%B5%D0%B2%D1%80%D0%BE&sxsrf=ALiCzsYZdru73smVgN5dUz174rH0ORm1wA%3A1654810931636&ei=M2miYvS_Jof8rgT0soOQCg&ved=0ahUKEwi0pYCOq6H4AhUHvosKHXTZAKIQ4dUDCA4&uact=5&oq=%D0%B5%D0%B2%D1%80%D0%BE&gs_lcp=Cgdnd3Mtd2l6EAMyDAgAELEDEEMQRhCCAjIHCAAQsQMQQzIHCAAQsQMQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIOCC4QgAQQsQMQxwEQowIyBAgAEEM6BwgAEEcQsAM6BwgAELADEEM6BwgjEOoCECc6CAgAEIAEELEDOgsIABCABBCxAxCDAToFCAAQgAQ6EQguEIAEELEDEIMBEMcBENEDOg4ILhCABBCxAxDHARDRAzoKCC4QxwEQ0QMQQzoICAAQChABEEM6CwguEIAEEMcBENEDOgsIABCABBAKEAEQKjoJCAAQgAQQChABOg8ILhCABBDHARCjAhAKEAE6DwguEIAEEMcBENEDEAoQAToMCC4QgAQQ1AIQChABOgcIABCABBAKOg0IABCABBCHAhCxAxAUOggIABCxAxCDAUoECEEYAEoECEYYAFCiCVj2FWCpF2gDcAF4AIABZIgBggWSAQM4LjGYAQCgAQGwAQnIAQrAAQE&sclient=gws-wiz"
KZT_RUB = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D1%82%D0%B5%D0%BD%D0%B3%D0%B5&ei=ok3NYrW7M8yOrwSMkqrYCg&ved=0ahUKEwi1lIjvkvP4AhVMx4sKHQyJCqsQ4dUDCA4&uact=5&oq=%D0%BA%D1%83%D1%80%D1%81+%D1%82%D0%B5%D0%BD%D0%B3%D0%B5&gs_lcp=Cgdnd3Mtd2l6EAMyEAgAEIAEELEDEIMBEEYQggIyBQgAEIAEMgsIABCABBCxAxCDATIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6CggAEEcQsAMQyQM6EQguEIAEELEDEIMBEMcBENEDOggIABCABBCxAzoOCC4QgAQQsQMQxwEQ0QM6EQguEIAEELEDEIMBEMcBEK8BOgwIABCABBCxAxAKEAE6EAguELEDEIMBEMcBENEDEAo6BwgAELEDEAo6CAgAELEDEIMBOgcILhCxAxAKOgYIABAKEAM6BAgAEAo6BggAEAoQQzoECAAQQzoKCAAQsQMQgwEQQ0oECEEYAEoECEYYAFD0BliWG2CEHGgGcAF4AIABcYgB9QmSAQM5LjWYAQCgAQGwAQDIAQjAAQE&sclient=gws-wiz"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"}



def check_currency():

	full_page = requests.get(DOLLAR_RUB, headers=headers)
	full_page1 = requests.get(EURO_RUB, headers=headers)
	full_page2= requests.get(KZT_RUB, headers=headers)


	soup = BeautifulSoup(full_page.content, "html.parser")
	soup1 = BeautifulSoup(full_page1.content, "html.parser")
	soup2 = BeautifulSoup(full_page2.content, "html.parser")
	

	convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision":2})
	convert1 = soup1.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision":2})
	convert2 = soup2.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision":2})
	


	date = datetime.datetime.today().strftime(' %d/%m/%Y %H:%M')
	print("Сейчас курс: 1 доллар = " + convert[0].text +  " Время:" + date)
	print ("Сейчас курс: 1 евро = " + convert1[0].text + " Время:" + date)
	print("Сейчас курс: 1 тенге = " + convert2[0].text + " Время:" + date)
	print("----------------------------")

	time.sleep(30)
	check_currency()

check_currency()	
