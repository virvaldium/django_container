Пример контейнера для разработки под django. Перед запуском необходимо добавить в example.env значение DJANGO_SECRET_KEY.
Для сборки и запуска контейнера необходмио выполнить команды:

docker-compouse build

docker-compouse up

Для запуска тестов нужно зайти в контейнер и выполнить команду:

docker-compouse run app bash 

./manage.py test







