from requests import get, RequestException
from sys import exit as stop
# импорты

ADDR = "https://glebocrew.ru" # адрес GET запроса
TIMEOUT = 10 # время ожидания ответа

print(f"Parsing info from {ADDR}")
try:
    data = get(
    ADDR,
    timeout=TIMEOUT,
) # полуаем дату

except RequestException as exception: # обработчик ошибок
    print(f"Parsing data failed! Full exception > {exception}")
    stop(0) # завершение программы

print("Parsing finished successfully")

print(f"Rendered response:\n{data.text}") # текстовый ответ
print(f"Raw response:\n{data.content}") # сырой ответ