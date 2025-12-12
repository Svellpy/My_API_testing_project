import httpx
import json
import datetime
import os



# number = str(input("Введи номер человека:\n"))
number = 1


response_people = httpx.get(f"https://swapi.dev/api/people/{number}/", verify=False)
data_people = response_people.json()

if response_people.status_code == 200:
    data = response_people.json()
else:
    print("Герой не найден.")
    data_people = None

def beautify_key(value):
    if data_people is None:
        return
    elif value not in data_people:
        print(f"Ключ '{value}' отсутствует в данных.")
        return
    elif type(data_people[value]) == list:
        for i in range(len(data_people[value])):
            data = httpx.get(data_people[value][i], verify=False).json()

            if "title" in data:
                data_people[value][i] = data["title"]

            elif "name" in data:
                data_people[value][i] = data["name"]

            else:
                print(f"Ключи 'name' и 'title' отсутствуют в данных для {value}")

    elif type(data_people[value]) == str:
        data = httpx.get(data_people[value], verify=False).json()

        if "title" in data:
                data_people[value][i] = data["title"]

        elif "name" in data:
            data_people[value] = data["name"]
        else:
            print(f"Ключи 'name' и 'title' отсутствуют в данных для {value}")



beautify_key("films")
beautify_key("species")
beautify_key("homeworld")
beautify_key("starships")
beautify_key("vehicles")


print(json.dumps(data_people, indent=4, ensure_ascii=False))  # красиво печатаем JSON

a=0

os.makedirs('logs', exist_ok=True)
def log_response(url, response):
    now = datetime.datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M")
    log_filename = f"logs/Star_wars_id.txt"

# 📌 Открытие файла для записи (перезаписывает всё содержимое)
with open('Star_wars_id.txt', 'w', encoding='utf-8') as f:
    f.write('Программа запущена:\n')  
    f.write(f"Время: {formatted_date}\n")
    f.write(f"--- Ответ ---\n")
    f.write(f"Статус: {response_people.status_code}\n")
    try:
        # Попытка вывести тело ответа как JSON
        json_data = response_people.json()
        f.write("Тело (JSON):\n")
        json.dump(json_data, f, ensure_ascii=False, indent=4)
        f.write("\n")
    except Exception:
        # Если не удалось распарсить JSON, выводим текст ответа
        f.write("Тело (текст):\n")
        f.write(response_people.text + "\n")

        