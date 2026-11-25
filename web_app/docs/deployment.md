# Deployment — DWP301c Codex

## Platform: Render (Free Tier Docker) / Local Uvicorn

## Local Run Command
```powershell
cd "G:\My Drive\Study\FPT University AI\Kì 5\Web Development with Python (DWP301c)\Source_from_Coursera\web_app"
python seed_db.py --course coursera1   # or --all for all 7 courses
uvicorn server:app --host 127.0.0.1 --port 8000 --reload
```

## Production Docker Command
```bash
docker build -t dwp301c-codex .
docker run -p 8000:8000 dwp301c-codex
```

## Deploy to Render
1. Push `web_app/` (including pre-seeded `dwp301c_hub.db`) to GitHub.
2. Create a Blueprint / Web Service on Render using `render.yaml` (`Dockerfile` runtime, health check `/api/health`).

## Scaling to All 7 Courses
Run `python seed_db.py --all` to import all 241 lessons and 381 quiz questions across Courses 1–7 into `dwp301c_hub.db` without any code changes.
