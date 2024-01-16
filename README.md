# Проект «API для Yatube»  
## Описание  
Данный проект предназначен для взоимодействия пользователя с интерфейсом разработанного продукта. Пользователь может подписываться, публиковать посты, а также коментировать их.  
  
## Стек техгологий  
1. Python
2. Shell
3. HTML
4. Django REST Framework
5. JSON
## Установка  
Клонируем проект в репозиторий:  

`git clone git@github.com:Imuntouchable/api_final_yatube.git`  
  
Переходим в нужную нам директорию:  
  
`cd api_final_yatube`  
  
Создаем и активируем виртуальное окружение:  
  
`python -m venv venv`   
`source venv/Scripts/activate`  
`python -m pip install --upgrade pip`  
  
Установливаем зависимости из файла requirements.txt:  
`pip install -r requirements.txt`
  
Выполняем миграции:  
`python manage.py migrate`  
  
Запускаем проект:  
`python manage.py runserver`  
## Примеры выполнения запросов  
1. http://127.0.0.1:8000/api/v1/posts/  
![image](https://github.com/Imuntouchable/api_final_yatube/assets/127663804/fd8fe793-1a6e-4e60-bd03-e18eacfa3e58)  
2. http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/  
![image](https://github.com/Imuntouchable/api_final_yatube/assets/127663804/70108ea4-6987-4ad6-891f-2f55ce1488fa)  
3. http://127.0.0.1:8000/api/v1/groups/  
![image](https://github.com/Imuntouchable/api_final_yatube/assets/127663804/9cee8d3e-e164-4aec-ad9a-635a125622a6)  


## Автор работы  
Тогузов Александр  
