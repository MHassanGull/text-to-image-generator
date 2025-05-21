# 🖼️ Text-to-Image Generation App

A powerful web app that transforms text prompts into images using AI-powered generation. Built with Django and Stable Diffusion, this project demonstrates how natural language can be used to produce creative visuals in real-time.

---

## 🚀 Features

- 🔤 Convert natural language text into images
- 🎨 Uses Stable Diffusion under the hood
- 🧠 AI generation utilities neatly encapsulated
- 🌐 Django-powered web backend
- 💾 Image rendering and saving locally
- 📁 Clean project structure with static asset handling

---

## 🛠️ Tech Stack

- **Backend**: Django, Python
- **AI Model**: Stable Diffusion (via Hugging Face or local inference)
- **Frontend**: HTML, CSS (animated styles), JS
- **Database**: SQLite (for development)
- **Deployment Ready**: Easily adaptable to production environments

---

## 📂 Project Structure

```bash
txt2img_project/
├── generator/
│   ├── views.py          # Core view logic for handling generation
│   ├── models.py         # (Optional) Django models
│   ├── urls.py           # URL routing
│   ├── static/           # Static assets (CSS, JS)
│   ├── stable_diffusion_utils.py  # AI generation logic
│   └── templates/        # HTML templates (if any)
├── manage.py             # Django project entry point
└── db.sqlite3            # Local DB for testing
