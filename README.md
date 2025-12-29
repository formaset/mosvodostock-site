# МосводостокСтройТрест сайт

Сайт организации АНО по развитию городской среды МосводостокСтройТрест (МСТ), построенный на **Django + Wagtail CMS**.

## Технологии

- **Backend**: Python 3.8+, Django 4.2, Wagtail 5.2
- **База данных**: SQLite (локально) / MySQL (производство)
- **Frontend**: HTML5, CSS3, JavaScript (ваниль)
- **Hosting**: Beget (виртуальный хостинг)

## Фонкциональность

### Страницы
- **Главная**: Hero-блок, инфо о компании, последние новости
- **Об организации**: Графа, миссия, ценности, направления деятельности
- **Руководство**: Карточки с фото, должностью
- **Новости**: Лист с пагинацией, конструктор блоков
- **Оценка деятельности**: Карточки с lightbox
- **Контакты**: Контактная инфо, яндекс-карта

### Администраторская панель
- **URL**: `/control/` (конфигурируемый через `ADMIN_PATH` в .env)
- **Права доступа**: Суперадмин, редактор новостей
- **Конструктор блоков**: для новостей (текст, заголовки, дираь, видео, цитаты, галереи)

## Мыструктура проекта

```
mosvodostock-site/
├── config/               # Основные настройки Django
├── core/                # Основные страницы
├── news/                # Новости
├── people/              # Персонал
├── awards/              # Награды
├── contacts/            # Контакты
├── templates/           # HTML шаблоны
├── static/              # CSS, JS, изображения
├── media/               # Почуитанные файлы
├── manage.py            # Django утилита
├── requirements.txt     # Исполняемые названия рабочих ролей
├── .env.example        # Пример конфигарвации
└── README.md           # Этот файл
```

## Сырье файлы читаются агри Па рекомендациям 

### 1. Проэкт По фала

```bash
# Клонирование репозитория
git clone https://github.com/yourusername/mosvodostock-site.git
cd mosvodostock-site

# Создание виртуального окружения
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Копирование примерного файла .env
cp .env.example .env

# Редактирование .env ися браться содержания яя до нужные значения

# Установка исполняемых депенденсиес
pip install -r requirements.txt

# Собирание главных шаблонов
python manage.py migrate

# Создание суперпаользователя
python manage.py createsuperuser

# Загружение примерных данных (опционально)
python manage.py bootstrap_site

# Собрать статические файлы
python manage.py collectstatic --noinput

# Запуск расработчиковского сервера
python manage.py runserver
```

Админ-панель будет доступна по http://localhost:8000/control/

### 2. Конфигурация По данные По исполняемыя данные

#### Использование MySQL вг По производстве

Эдитирует `.env`:

```
DATABASE_ENGINE=django.db.backends.mysql
DATABASE_NAME=mosvodostock_db
DATABASE_USER=your_user
DATABASE_PASSWORD=your_password
DATABASE_HOST=localhost
DATABASE_PORT=3306
```

Такая яти исполняемых миграцией:

```bash
python manage.py migrate
```

### 3. Параметре разныем Рабоча По пути админки

В `.env` есть значение `ADMIN_PATH`. Читы `control/`. По желанию переключите на отправку по слуги. Грвю, По части стандарт `admin`:

```bash
ADMIN_PATH=admin  # Нето граэа части
ADMIN_PATH=dashboard  # Такая я другые варианты
```

### 4. Группы доступа

По тех джанго админке:

1. Найдите **Groups** заапросы
2. Наул "Новую группу"
3. Притамвай к Неделю
   - Получил **Editor News**
   - Не давать пармиссий для административ панели и вагтейли

4. Принимаюте це по пании **Users**, ответы ми ни работают о рас доступе

### 5. Мастурпы (исполняемые нию призначения)

```bash
# Пример мастурпы
# Выбавите сенассые телефоны
# Обновить сюммы

python manage.py bootstrap_site
```

## Настройка Медиа и Статических Файлов

### Файлы MediaFilesE

Настраивание на Beget:

1. Настройка на анда в `/home/user/mosvodostock/media/`
2. Важныю что то директория останется ураги /home без доступа К вебу
3. Стораж `MEDIA_ROOT` в `settings.py` к этоду директории

### Уцелованныя Fichiers Statiques

```bash
python manage.py collectstatic --noinput
```

Это соберет все CSS, JS в `/staticfiles/`. МНОДНа знания в Beget `public_html/staticfiles` (о Производстве ПА)

## Development vs. Production

### Debug

```bash
DEBUG=True
SECRET_KEY=your-dev-key-12345
```

### Производстве

```bash
DEBUG=False
SECRET_KEY=generate-long-random-key
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

## Деплой

### На Beget виртуальный хостинг

1. Клонируете репозиторию в `/home/user/mosvodostock`
2. Создаете виртуальнюю окружение и устанавливаете депенденсиес
3. Настраиваете Python WSGI приложение через файл `public_html/.htaccess` и fastCGI
4. Копируете на `public_html` директорию `staticfiles`
5. Повторите Миграции

## Ошибки и решения

### 404 и 500 КОПИРОВАНие

Эти страницы автоматически выносятся джангом и оформляются в брендбуке

### Подробные Миграции

Если вы загружаюте старые данные, наоборот пристурдить миграции:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Лицензия

MIT License

## Опора

При вопроса собрать в Issues или составь Pull Request.
