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

нужная вкладка:

<img width="263" alt="3-Crud" src="https://github.com/user-attachments/assets/f829b804-7c82-4eda-a7c7-a94e9493e0d6" />

Кнопкa для создания:

<img width="161" alt="5 - Для создания поста" src="https://github.com/user-attachments/assets/b2494cd6-d482-4373-b18b-f4d69dbe33b3" />

После создания поста мы можем отредактировать или удалить его:

<img width="466" alt="Для удаления_создания" src="https://github.com/user-attachments/assets/0b9929bb-4211-4ab9-beaf-6e682a8d9fde" />

### Выполнение периодической задачи (celery) на отправку email о Новостях, опубликованных сегодня, с настройками (constance) + Сводка погоды в Примечательном месте
Все celery-таски находятся в папке проекта NewsProject в файле tasks.py
**Celery-таска для рассылки писем запускается по Московскому времени**

Параметры, задающиеся через constance в admin-panel(используются для настройки Celery-тасок):

<img width="433" alt="Параметры для celery-тасок" src="https://github.com/user-attachments/assets/8b83bafe-94bb-4bbf-80d1-ee3a7db6e0f8" />

### Импорт Примечательных мест из xlsx-файла с данными
В админ панели можно импортировать данные о примечательных местах из xlsx-файла(импортирует из активного листа, файл подается без заголовков для колонок):

<img width="392" alt="Remarkable-xl" src="https://github.com/user-attachments/assets/725e5ff8-f2d4-4cd1-8d96-f2a62a525f03" />

Например, после выбора этого файла будет создана одна новая запись(представлен пример файла):

<img width="251" alt="Exc" src="https://github.com/user-attachments/assets/ef22d2ee-604a-493f-bd52-b252f8f4f5e9" />

### Просмотр и редактирование Примечательных мест(карты)
Для всех объектов в админ панели под полями расположен виджет карты. Для изменения координа перетажите маркер(Нужно наводить на самое основание, тогда появится синяя точка):

<img width="697" alt="Maps" src="https://github.com/user-attachments/assets/eb6449ed-2b12-4cbc-b72e-7a4134261ca2" />


### Экспорт Сводки погоды в xlsx-файл
В разделе "сводки погоды" имеется форма для получения всех записей о конкретном примечательном месте. После заполнения полей и нажатия будет загружен xlsx-файл:

<img width="661" alt="Водки" src="https://github.com/user-attachments/assets/55f7fff8-90f3-420f-9c5b-7d859ed5c05b" />


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
