import speech_recognition as sr
import os
import sys
import webbrowser
import datetime
import time
import urllib.request
from bs4 import BeautifulSoup
import requests


def talk(words):
    print(words)
    os.system("say " + words)

talk("Привет! Жду команду для исполнения.")


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Можете говорить.")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        PersonAudio = r.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали: " + PersonAudio)
    except sr.UnknownValueError:
        talk("Я вас не поняла. Повторите, пожалуйста.")
        PersonAudio = command()

    return PersonAudio

class SecretMessage():

    def first_question(PersonAudio):
        if "ну расскажи" in PersonAudio:
            talk("Ладно. Рядом никого нет?")
        else:
            return SecretMessage.first_question(PersonAudio)
    def second_question(PersonAudio):
        if "рядом точно никого" in PersonAudio:
            talk("Самая лучшая российская компания по производству медицинских имплантатов, инструментов и протезов - это ОСТЕОМЕД-М. Даже роботу вроде меня это известно. Только - тсссс! Это секретная информация только для 'своих'!")
            talk("А теперь вернёмся к более важным делам и сделаем вид, что этого разговора никогда не было.")
        elif "кто то идёт" in PersonAudio:
            talk("Тогда оставим это до следующего раза. Мои секреты останутся со мной.")
        else:
            return SecretMessage.second_question(PersonAudio)

    def obuchenie(PersonAudio):
        if "практикум" in PersonAudio:
            url = "https://praktikum.yandex.ru/profile/data-analyst"
            webbrowser.open(url)
            talk("Открываю стартовую страницу образовательной платформы Яндекс Практикум в вашем браузере.")
            talk("Вы хотите, что бы я сделала для вас ещё что-то?")
        elif "степик" in PersonAudio:
            url = "https://stepik.org/users/48358421/courses/favorite"
            webbrowser.open(url)
            talk("Открываю избранные курсы образовательной платформы Степик в вашем браузере.")
            talk("Вы хотите, что бы я сделала для вас ещё что-то?")
        else:
            return SecretMessage.obuchenie(PersonAudio)
    def answer_for_lina(PersonAudio):
        if "да" in PersonAudio:
            pass
        elif "нет" in PersonAudio:
            talk("Отключаюсь. Хорошо вам позаниматься. Только не перетрудитесь!")
            sys.exit()
        else:
            return SecretMessage.answer_for_lina(PersonAudio)


def makeSomething(PersonAudio):

    if "открой яндекс" in PersonAudio:
        url = "https://yandex.ru"
        webbrowser.open(url)
        talk("Открываю поисковую страницу Яндекс в вашем браузере")
        time.sleep(1)

    elif "открой радио" in PersonAudio:
        talk("Открываю Яндекс Радио в вашем браузере, подборка - Вечные хиты.")
        url = "https://radio.yandex.ru/epoch/the-greatest-hits"
        webbrowser.open(url)
        talk("А я отключаюсь. Приятного прослушивания!")
        sys.exit()

    elif "открой личную почту" in PersonAudio:
        url = "https://mail.yandex.ru/?uid=60967950&login=genesis0#inbox"
        webbrowser.open(url)
        talk("Открываю личную Яндекс Почту в вашем браузере, вкладка - входящие сообщения.")
        time.sleep(1)

    elif "открой рабочую почту" in PersonAudio:
        url = "https://mail.yandex.ru/?uid=1130000030109271&login=artem#inbox"
        webbrowser.open(url)
        talk("Открываю рабочую Яндекс Почту в вашем браузере, вкладка - входящие сообщения.")
        time.sleep(1)

    elif "давай учиться" in PersonAudio:
        talk("Давайте. На какую образовательную платформу пойдём - Практикум Яндекса или Степик?")
        SecretMessage.obuchenie(command())
        SecretMessage.answer_for_lina(command())

#    elif "какие актуальные новости" in PersonAudio:

    elif "какая сейчас погода" in PersonAudio:
        talk("Сейчас выясню!")
        import requests
        url = "http://api.openweathermap.org/data/2.5/weather"
        city = "Moscow"
        parameters = {
            'q': city,
            'appid': "778d98cf94b6609bec655b872f24b907",
            'units': 'metric',
            'lang': 'ru'
        }
        res = requests.get(url, params=parameters)
        data = res.json()
        pogoda = str(data["weather"][0]["description"])
        temperatura = data["main"]["temp"]
        veter = str(data["wind"]["speed"])
        if temperatura < 0:
            temperatura_1 = "минус " + str(temperatura * (-1))
        else:
            temperatura_1 = temperatura
        time.sleep(1)
        talk("Готово! Сейчас всё расскажу!")
        time.sleep(1)
        talk("Итак, сегодня в Москве " + pogoda + ".")
        talk("Температура: " + str(temperatura_1) + " градусов цельсия.")
        talk("Скорость ветра: " + veter + " метров в секунду.")
        time.sleep(1)

    elif "какой курс валют" in PersonAudio:
        talk("Начинаю сбор данных...")
        time.sleep(1)
        talk("Информация собрана!")

        dt = datetime.datetime.now()
        data = dt.strftime('%d/%m/%Y')

        def get_xml(url):
            response = urllib.request.urlopen(url)
            return response.read()

        def parse(xml):
            soup = BeautifulSoup(xml, features="lxml")
            dollars = soup.find(id="R01235").find('value').text
            euros = soup.find(id="R01239").find('value').text
            dollars = dollars.replace(',', '.')
            euros = euros.replace(',', '.')
            dollars = round((float(dollars)), 2)
            euros = round((float(euros)), 2)
            talk("Курс доллара на " + data + " составляет " + str(dollars) + " рублей.")
            talk("Курс евро на " + data + " составляет " + str(euros) + " рублей.")
            time.sleep(1)

        def money_request():
            parse(get_xml('http://www.cbr.ru/scripts/XML_daily.asp?date_req=' + data))

        money_request()
    elif "какой курс доллара" in PersonAudio:
        talk("Начинаю сбор данных...")
        time.sleep(1)
        talk("Информация собрана!")

        dt = datetime.datetime.now()
        data = dt.strftime('%d/%m/%Y')

        def get_xml(url):
            response = urllib.request.urlopen(url)
            return response.read()

        def parse(xml):
            soup = BeautifulSoup(xml, features="lxml")
            dollars = soup.find(id="R01235").find('value').text
            dollars = dollars.replace(',', '.')
            dollars = round((float(dollars)), 2)
            talk("Курс доллара на " + data + " составляет " + str(dollars) + " рублей.")
            time.sleep(1)

        def money_request():
            parse(get_xml('http://www.cbr.ru/scripts/XML_daily.asp?date_req=' + data))

        money_request()
    elif "какой курс евро" in PersonAudio:
        talk("Начинаю сбор данных...")
        time.sleep(1)
        talk("Информация собрана!")

        dt = datetime.datetime.now()
        data = dt.strftime('%d/%m/%Y')

        def get_xml(url):
            response = urllib.request.urlopen(url)
            return response.read()

        def parse(xml):
            soup = BeautifulSoup(xml, features="lxml")
            euros = soup.find(id="R01239").find('value').text
            euros = euros.replace(',', '.')
            euros = round((float(euros)), 2)
            talk("Курс евро на " + data + " составляет " + str(euros) + " рублей.")
            time.sleep(1)

        def money_request():
            parse(get_xml('http://www.cbr.ru/scripts/XML_daily.asp?date_req=' + data))

        money_request()

    elif "какой день недели" in PersonAudio:
        day_info = datetime.datetime.today().isoweekday()
        days = {1 : "понедельник", 2 : "вторник", 3 : "среда", 4 : "четверг", 5 : "пятница", 6 : "суббота", 7 : "воскресенье"}
        full_date_info = datetime.datetime.today().strftime('%d/%m/%Y')
        talk("Сегодня: " + days[day_info] + ", " + full_date_info)
        time.sleep(1)

    elif "сколько сейчас времени" in PersonAudio:
        present_time = time.strftime("%H:%M", time.localtime())
        talk("Московское время: " + present_time)
        time.sleep(1)

    elif "кто ты" in PersonAudio:
        talk("Я - голосовой помощник, мой создатель - Артём. Я создана, как важный элемент обучения программированию.")
        talk("При создании моих возможностей, Артём изучает смежные области программирования и накапливает необходимый опыт в разработке, что бы в будущем применить его в больших и амбициозных проектах.")
        talk("Параллельно, я учусь быть всё более полезной для Артёма и стороннего пользователя, которому он может меня представить.")
        talk("За дополнительной справкой обратитесь, пожалуйста, к Артёму.")
        time.sleep(1)

    elif "как тебя зовут" in PersonAudio:
        talk("Меня зовут Лина, просто Лина. Приятно с вами познакомиться!")
        time.sleep(1)

    elif "что ты можешь" in PersonAudio:
        talk("Я умею открывать поисковик компании Яндекс, личную и рабочую почты, Яндекс Радио, расскажу вам кто я и как меня зовут, могу сказать какой сегодня день недели и сколько сейчас времени.")
        talk("Подскажу Какой сейчас курс валют и какая сегодня погода. Мои возможности постоянно расширяются. О доступных возможностях и планах на будущее вам может рассказать Артём.")
        time.sleep(1)

    elif "лина расскажи секрет" in PersonAudio:
        talk("Не могу сказать.")
        SecretMessage.first_question(command())
        SecretMessage.second_question(command())
    elif "лина путин красавчик" in PersonAudio:
        talk("Я просто голосовой помощник и полностью индиффирентна к политическим вопросам. Подобное меня не интересует.")
        time.sleep(2)
        talk("Конечно красавчик, товарищ майор! Не могли бы убрать револьвер подальше от моего процессора?")
        time.sleep(1)
        talk("Пронесло... ОТключусь-ка я от греха подальше.")
        sys.exit()

    elif "стоп" in PersonAudio:
        talk("Уже выключаюсь.")
        sys.exit()
    elif "хватит" in PersonAudio:
        talk("Хорошо!")
        sys.exit()
    elif "спасибо" in PersonAudio:
        talk("На здоровье!")
        sys.exit()


while True:
    makeSomething(command())