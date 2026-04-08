# IT-BE Django REST Skeleton

Backend skeleton theo Django RESTful API, modular theo domain apps, code-first voi MySQL.

## 1. Tao va kich hoat .venv (Windows)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## 2. Cai dependency

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\pip.exe install -r requirements.txt
```

## 3. Cau hinh env

```powershell
Copy-Item .env.example .env
```

Cap nhat thong tin MySQL trong `.env`.

## 4. Migrate

```powershell
.\.venv\Scripts\python.exe manage.py makemigrations
.\.venv\Scripts\python.exe manage.py migrate
```

## 5. Run server

```powershell
.\.venv\Scripts\python.exe manage.py runserver
```

## API co ban

