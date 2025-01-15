# Test_task_DDC
## Содержание
* CRUD Новостей с данными (где?)
* Выполнение периодической задачи (подсказка: celery) на отправку email о Новостях, опубликованных сегодня, с настройками (подсказка: constance) + Сводка погоды в Примечательном месте
* Импорт Примечательных мест из xlsx-файла с данными
* Просмотр и редактирование Примечательных мест(карты)
* Экспорт Сводки погоды в xlsx-файл
* Запуск

## Основная часть

### CRUD Новостей с данными (где?)
нужная вкладка

<img width="263" alt="3-Crud" src="https://github.com/user-attachments/assets/9da86178-9f03-4f9f-bf08-bb7a7cf8f836" />

Кнопки для создания

<img width="161" alt="5 - Для создания поста" src="https://github.com/user-attachments/assets/e39c6066-fe32-4be5-af82-54cf62606893" />

после создания еще редактирования, удаления

<img width="466" alt="Для удаления_создания" src="https://github.com/user-attachments/assets/d94cb0a6-96ff-4936-9420-449d8666f168" />

### Выполнение периодической задачи (celery) на отправку email о Новостях, опубликованных сегодня, с настройками (constance) + Сводка погоды в Примечательном месте
Все celery-таски находятся в папке проекта NewsProject в файле tasks.py

Параметры, задающиеся через constance в admin-panel:
<img width="425" alt="Сщтыефтсу" src="https://github.com/user-attachments/assets/545dfb96-74e3-4f76-9783-cfb800eae6fa" />

<img width="433" alt="Параметры для celery-тасок" src="https://github.com/user-attachments/assets/094abd1c-1c75-4bc3-a050-9fb45832fe35" />

### Импорт Примечательных мест из xlsx-файла с данными
В админ панели можно импортировать данные о примечательных местах из xlsx-файла(импортирует из активного листа, файл подается без заголовков для колонок):
<img width="392" alt="Remarkable-xl" src="https://github.com/user-attachments/assets/a562c928-afb4-44a6-8282-f61143f1965e" />

Из этого файла добавиться одна запись
<img width="251" alt="Exc" src="https://github.com/user-attachments/assets/56c1ab9c-4b6c-4305-b896-9288718c0169" />

### Просмотр и редактирование Примечательных мест(карты)
Для всех объектов в админ панели под полями расположен виджет карты. Для изменения координа перетажите маркер(Нужно наводить на самое основание, тогда появится синяя точка)
<img width="697" alt="Maps" src="https://github.com/user-attachments/assets/2302f605-0f99-43d6-b49a-c5606b9cb154" />

### Экспорт Сводки погоды в xlsx-файл
В разделе "сводки погоды" имеется форма для получения всех записей о конкретном примечательном месте. После заполнения полей и нажатия будет загружен xlsx-файл
<img width="661" alt="Водки" src="https://github.com/user-attachments/assets/e7b31984-5faa-4798-97b7-0ef1586ee272" />

### Запуск

Устанавливаем зависимости:
```
poetry install
```

Создаем и выполняем миграции:
```
poetry run python manage.py makemigrations
poetry run python manage.py migrate
```

создаем суперюзера:
```
python manage.py createsuperuser
```

Собираем статические файлы:

```
poetry run python manage.py collectstatic
```

Каждую из следующих трех команд запускаем в отдельном терминале:

```
poetry run python manage.py runserver
```

```
poetry run celery -A NewsProject.celery worker --pool=solo -l info
```

```
poetry run celery -A NewsProject beat -l info
```
