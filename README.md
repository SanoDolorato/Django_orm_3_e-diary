# Электронный дневник школы

Изменяем записи в электронном дневнике в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
Дневник без БД хранится в репозитории https://github.com/devmanorg/e-diary

## Установка


Переместите файл scripts.py в корень сайта, рядом с manage.py



## Запуск
Запустите Django Shell
```
python manage.py shell
```
В Django Shell выполните команду:
```
from scripts import fix_marks, remove_chastisements, create_commendation
```

## Использование

Исправляем оценки "2" и "3" на "5"
```
fix_marks("Фамилия Имя")
```
Удаляем замечания
```
remove_chastisements("Фамилия Имя")
```
Добавляем похвалу
```
create_commendation("Фамилия Имя", "Предмет")
```
