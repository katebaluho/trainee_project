# trainee_project
Для запуска проекта:
1. git clone https://github.com/katebaluho/trainee_project.git
2. проверить нахождениe в виртуальном окружении
3. установить зависимости pip install -r requirements.txt

Для работы с api подключен Swagger: http://127.0.0.1:8000/api/swagger/

Вполнены задачи:
Задача 1:
Создать кастомную модель пользователя.
Поля: емейл, пароль, имя пользователя для отображения в профиле, дата рождения, пол.
Поле емейл используется для аутентификации.
Реализовать ендпойнты для регистрации и аутентификации.
Регистрация: http://127.0.0.1:8000/accounts/create/
Аутентификация: http://127.0.0.1:8000/api-token-auth/
При успешной аутентификации возвращается логин, имя пользователя.
При успешной регистрации возвращается логин.

Задача 2.
Создать ендпойнт, который будет выдавать файл, содержащий список зарегистрированных в системе пользователей.
Ендпоинт: http://127.0.0.1:8000/accounts/users/download/
Минимально - список логинов. Максимально - всю информацию о каждом пользователе (кроме пароля). Что получится сделать. 
Разметка файла - на ваш вкус.
Необходимо создать файл в формате doc или pdf.
Бд - sqlite.