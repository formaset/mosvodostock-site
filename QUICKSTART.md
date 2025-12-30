# Быстрый старт

## Установка и запуск

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/formaset/mosvodostock-site.git
cd mosvodostock-site
```

### 2. Создайте виртуальное окружение

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Установите зависимости

```bash
pip install -r requirements.txt
```

### 4. Создайте файл .env

```bash
cp .env.example .env
```

Редактируйте `.env` по необходимости:

```bash
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Примените миграции

```bash
python manage.py migrate
```

### 6. Создайте суперпользователя

```bash
python manage.py createsuperuser
```

Введите:
- Username: `admin`
- Email: `admin@example.com`
- Password: `ваш_пароль`

### 7. (Опционально) Загрузите тестовые данные

```bash
python manage.py bootstrap_site
```

### 8. Соберите статические файлы

```bash
python manage.py collectstatic --noinput
```

### 9. Запустите сервер

```bash
python manage.py runserver
```

## Доступ к сайту

- **Сайт**: http://localhost:8000/
- **Админ-панель**: http://localhost:8000/control/

## Первые шаги в админке

1. Войдите в админ-панель: http://localhost:8000/control/
2. Введите логин и пароль суперпользователя
3. Перейдите в **Pages** и найдите главную страницу
4. Редактируйте содержимое по своему усмотрению

### Создание новости

1. В админке перейдите в **Pages**
2. Найдите страницу "Новости"
3. Нажмите "Add child page" → "Новость"
4. Заполните:
   - **Title**: заголовок
   - **Lead**: краткое описание
   - **Cover Image**: обложка
   - **Body**: основное содержание (используйте блоки)
5. Нажмите **Publish**

### Добавление руководителя

1. В Django админке (http://localhost:8000/admin/) перейдите в **People** → **Руководство**
2. Нажмите "Add Руководитель"
3. Заполните данные и загрузите фото
4. Сохраните

## Частые проблемы

### Ошибка импорта

Если вы видите ошибку импорта, убедитесь, что:
1. Активировано виртуальное окружение
2. Установлены все зависимости: `pip install -r requirements.txt`

### Ошибка базы данных

Если миграции не применяются:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Статические файлы не загружаются

В режиме разработки (с `DEBUG=True`) Django автоматически обслуживает статические файлы.

Если проблемы персистируют, выполните:
```bash
python manage.py collectstatic --noinput
```

## Следующие шаги

- Прочитайте полный [README.md](README.md)
- Ознакомьтесь с [Wagtail документацией](https://docs.wagtail.org/)
- Настройте продакшен окружение
