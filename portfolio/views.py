from django.shortcuts import render

PROJECTS = [
    {
        "id": 1,
        "title": "Агрегатор новин та аналітики",
        "description": "Платформа для збору та автоматичного аналізу новинних стрічок у реальному часі.",
        "full_description": "Система автоматично збирає інформацію з відкритих RSS-каналів та новинних порталів, класифікує матеріали за темами та надає аналітичні звіти щодо популярності тем.",
        "year": 2024,
        "status": "Завершено",
        "technologies": ["Python", "Django", "BeautifulSoup", "PostgreSQL"],
    },
    {
        "id": 2,
        "title": "Платформа моніторингу серверів",
        "description": "Веб-панель для відстеження навантаження на сервери, оперативної пам'яті та дискового простору.",
        "full_description": "Інструмент для системних адміністраторів із графічним дашбордом. Дозволяє налаштовувати сповіщення при досягненні критичних показників навантаження системи.",
        "year": 2024,
        "status": "В процесі",
        "technologies": ["Python", "Django", "SQLite", "Chart.js"],
    },
    {
        "id": 3,
        "title": "Сервіс бронювання коворкінгів",
        "description": "Система для онлайн-бронювання робочих місць, переговорних кімнат та конференц-залів.",
        "full_description": "Комплексне рішення з інтерактивною мапою приміщень, календарем зайнятості та автоматичним генеруванням квитанцій для відвідувачів.",
        "year": 2023,
        "status": "Завершено",
        "technologies": ["Python", "Django", "Bootstrap", "PostgreSQL"],
    },
    {
        "id": 4,
        "title": "Телеграм-бот фінансового обліку",
        "description": "Бот та панель керування для фіксації щоденних витрат і формування бюджету.",
        "full_description": "Інструмент персональних фінансів з можливістю імпорту банківських виписок, категоризації витрат та експорту звітів у формати CSV та PDF.",
        "year": 2023,
        "status": "Завершено",
        "technologies": ["Python", "aiogram", "Django", "SQLite"],
    },
]

SKILLS = [
    {"name": "Python", "level": "advanced"},
    {"name": "Django", "level": "advanced"},
    {"name": "PostgreSQL", "level": "intermediate"},
    {"name": "Redis & Celery", "level": "intermediate"},
    {"name": "REST API", "level": "advanced"},
    {"name": "Linux / Bash", "level": "intermediate"},
    {"name": "HTML & CSS", "level": "advanced"},
    {"name": "Docker", "level": "beginner"},
    {"name": "Git", "level": "advanced"},
    {"name": "FastAPI", "level": "beginner"},
]

def home(request):
    context = {
        "name": "Максим Коваленко",
        "bio": "Full-Stack Python розробник. Спеціалізуюся на бекенді на базі Django, проєктуванні баз даних та створенні REST API сервісів.",
        "skills": SKILLS,
    }
    return render(request, "portfolio/home.html", context)

def projects(request):
    return render(request, "portfolio/projects.html", {"projects": PROJECTS})

def project_detail(request, pk):
    project = next((p for p in PROJECTS if p["id"] == pk), None)
    return render(request, "portfolio/project_detail.html", {"project": project})

def contacts(request):
    contact_data = {
        "email": "developer.portfolio@mail.net",
        "phone": "+380 50 987 65 43",
        "github": "https://github.com/developer-demo",
        "telegram": "https://t.me/dev_demo",
        "location": "Львів, Україна",
    }
    return render(request, "portfolio/contacts.html", {"contacts": contact_data})
