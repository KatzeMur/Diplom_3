import requests
import zipfile
import os

# Альтернативный источник (китайское зеркало)
url = "https://registry.npmmirror.com/-/binary/chrome-for-testing/149.0.7827.155/win64/chromedriver-win64.zip"

print("Скачиваю ChromeDriver...")
response = requests.get(url)

if response.status_code == 200:
    # Сохраняем ZIP-файл
    with open("chromedriver.zip", "wb") as f:
        f.write(response.content)
    print("Скачано!")
    
    # Распаковываем
    with zipfile.ZipFile("chromedriver.zip", "r") as zip_ref:
        zip_ref.extractall("chromedriver")
    print("Распаковано в папку chromedriver!")
    
    # Удаляем ZIP
    os.remove("chromedriver.zip")
    print("Готово! Драйвер находится в папке chromedriver/chromedriver-win64/chromedriver.exe")
else:
    print(f"Ошибка скачивания: {response.status_code}")
    