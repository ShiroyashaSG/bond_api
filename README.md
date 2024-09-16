# Проект API для социальной сети

## Описание

Этот проект представляет собой API для социальной сети, где пользователи могут создавать посты, комментировать их, подписываться друг на друга и просматривать группы. API предоставляет полный набор функционала для работы с контентом, включая создание, просмотр, редактирование и удаление постов и комментариев, а также управление подписками.

### Основной функционал:
- **Группы**: просмотр доступных групп.
- **Посты**: создание, просмотр, редактирование и удаление постов.
- **Комментарии**: добавление и редактирование комментариев к постам.
- **Подписки**: управление подписками на других пользователей.

## Установка

### 1. Клонирование репозитория
Для начала, клонируйте репозиторий проекта на локальную машину:
```bash
git clone https://github.com/ShiroyashaSG/api_final_yatube.git
cd api_final_yatube
```

### 2. Cоздать и активировать виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate
```

### 3. Обновить pip:
```bash
python -m pip install --upgrade pip
```

### 4. Установить зависимости из файла requirements.txt:
```bash
pip install -r requirements.txt
```

### 5. Выполнить миграции:
```bash
python3 manage.py migrate
```

### 6. Запустить проект:
```bash
python3 manage.py runserver
```

Теперь проект доступен по адресу http://127.0.0.1:8000/

## Примеры запросов к API

### 1. Просмотр списка постов:
Запрос:
```http
GET /api/v1/posts/
```

Ответ:
```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

### 2. Создание нового поста:
Запрос:
```http
POST /api/v1/posts/
Content-Type: application/json
Authorization: Bearer <your_token>

{
  "text": "string",
  "image": "string",
  "group": 0
}
```

Ответ:
```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

### 3. Добавление комментария к посту:
Запрос:
```http
POST /api/v1/posts/{post_id}/comments/
Content-Type: application/json
Authorization: Bearer <your_token>

{
    "text": "string"
}
```

Ответ:
```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

### 4. Подписка на пользователя:
Запрос:
```http
POST /api/v1/follow/
Content-Type: application/json
Authorization: Bearer <your_token>

{
    "following": "string"
}
```

Ответ:
```json
{
  "user": "string",
  "following": "string"
}
```

## Требования
    ∙ Python 3.9.x+
    ∙ Django 3.x+
    ∙ Django REST Framework 3.x+