# 🦉 OwlWatch — Your Night-Time Video Progress Tracker for Linux

> *Track your video progress. Take notes. Never lose your place again — even when the sun goes down.*

---

## ✨ What Is OwlWatch?

**OwlWatch** is a lightweight, right-click-enabled Python tool designed for learners who download video courses (like HackTheBox, Udemy, or YouTube playlists) and need to:

✅ Track which videos you’ve watched, are watching, or haven’t started  
✅ Add personal notes directly to each video  
✅ Save progress locally — no cloud, no login, no tracking  
✅ Use it instantly via **right-click → “Track Videos”** in any folder on Linux (Parrot OS, Ubuntu, etc.)

Built with **Python + Tkinter**, it’s **open-source, customizable, and works offline** — perfect for late-night study sessions. 🌙🦉

---

## 🖥️ Features

- 🔹 **Right-click integration** with Caja (Parrot OS) / Nautilus / Dolphin
- 🔹 **Dark mode UI** — easy on the eyes during late-night study
- 🔹 **Progress tracking**: ✅ Completed | ⏳ In Progress | ❌ Not Started
- 🔹 **Note-taking**: Write & save notes per video (Ctrl+S, Ctrl+A, Ctrl+C/V)
- 🔹 **Local storage**: All data saved in `.video_tracker.json` inside your course folder
- 🔹 **Keyboard shortcuts**: `Ctrl+S` to save, `Ctrl+A` to select all, `Esc` to close
- 🔹 **Mouse scroll support** — scroll through long lists smoothly
- 🔹 **Zero dependencies** — just Python 3 and Tkinter (usually pre-installed)

---

## 📦 Installation

### 1. Clone the repo:
```bash
git clone https://github.com/mazin208/owlwatch.git
cd owlwatch
```

### 2. Make the script executable:
```bash
chmod +x tracker.py
```

### 3. Install to Caja (Parrot OS):

```bash
cp . ~/.config/caja/scripts/
```

> ✅ Now, right-click any folder → **Scripts → OwlWatch** to launch!

---

## 🛠️ Customization

You can easily customize:
- Colors (dark/light themes)
- Keyboard shortcuts
- Status icons
- Note editor size

Just edit `tracker.py` — it’s clean, well-commented, and beginner-friendly.

---

## 🧩 How It Works

When you run OwlWatch from a folder:
- It scans for `.mp4`, `.mkv`, `.avi`, etc.
- Loads existing progress from `.video_tracker.json` (if exists)
- Lets you update status + add notes
- Saves everything back to the same file — so your progress travels with your folder

---

## 🤝 Contribute

This project is open-source and welcomes contributions! Whether you want to:
- Add new features (export to PDF, sync with Notion, etc.)
- Improve the UI
- Fix bugs
- Add support for other file managers (Dolphin, Thunar)

👉 Just fork the repo and send a PR!

## 🚀 Built With

- Python 3
- Tkinter (GUI)
- JSON (data storage)
- Linux file manager scripts (Caja/Nautilus)

---

## 🙋‍♂️ Questions? Feedback?

Open an issue on GitHub or DM me on LinkedIn — I’d love to hear how you’re using OwlWatch!

---

## 🌟 P.S.

Big thanks to **Qwen AI** for helping turn this idea into reality. This is what happens when creativity meets code — and you get something truly useful.

---

📌 **Star ⭐ this repo if you find it helpful — and share it with fellow learners!**

#Python #OpenSource #EdTech #Productivity #Linux #DeveloperTools #OnlineLearning #NightMode #OwlWatch #LearnSmart
