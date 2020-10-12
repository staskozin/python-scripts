# Скрипты на Python
Разные скрипты, которые были мне нужны.

## watermark.py
Добавляет вотермарку на изображения в директории и сохраняет в другую.

`python watermark.py watermark_file source/path destination/path`

Использовал для фотографий в интернет-магазине.

## download_images.py
Скачивает изображения в директорию. Принимает на вход список ссылок в текстовом файле.

`python download_images.py images.txt destination/path`

Использовал чтобы скачать альбом из ВК.

## square_images.py
Делает картинки квадратными. Работает только с jpg с белым фоном.

```
python square_images.py -s source.jpg -r result.jpg
# Одна картинка
```

```
python square_images.py -m -s source_dir -r result_dir
# Все картинки в директории
```

Использовал для фотографий в интернет-магазине.

## resize_images.py
Подгоняет картинки под указанный размер. Например, картика 2459×2873 при указанном размере 1600 станет 1369×1600 Работает только с jpg.

```
python resize_images.py -s source.jpg -r result.jpg -ms 1600
# Одна картинка
```

```
python resize_images.py -m -s source_dir -r result_dir -ms 1600
# Все картинки в директории
```

Использовал для фотографий в интернет-магазине.
