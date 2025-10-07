import os
import json
import tkinter as tk
from tkinter import ttk, scrolledtext

class VideoTrackerApp:
    def __init__(self, folder_path):
        self.folder = os.path.abspath(folder_path)
        self.data_file = os.path.join(self.folder, ".video_tracker.json")
        self.videos = self.get_video_files()
        self.data = self.load_data()
        self.status_labels = {
            "not_started": "❌ Not Started",
            "in_progress": "⏳ In Progress",
            "completed": "✅ Completed"
        }

    def get_video_files(self):
        exts = ('.mp4', '.mkv', '.avi', '.mov', '.webm', '.flv', '.wmv', '.m4v')
        return sorted([f for f in os.listdir(self.folder) 
                      if os.path.isfile(os.path.join(self.folder, f)) 
                      and f.lower().endswith(exts)])

    def load_data(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    for v in self.videos:
                        if v not in data:
                            data[v] = {"status": "not_started", "notes": ""}
                    return data
            except Exception as e:
                print(f"[Error] Loading data: {e}")
        return {v: {"status": "not_started", "notes": ""} for v in self.videos}

    def save_data(self):
        for v in self.videos:
            if v not in self.data:
                self.data[v] = {"status": "not_started", "notes": ""}
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
            print(f"[Success] Saved to {self.data_file}")
        except Exception as e:
            print(f"[Error] Cannot save to {self.data_file}: {e}")

    def open_notes_editor(self, video_name):
        note_win = tk.Toplevel()
        note_win.title(f"Notes: {video_name}")
        note_win.geometry("600x450")
        note_win.configure(bg="#1e1e1e")

        # ✅ محرر النص (مع دعم الاختصارات)
        text = scrolledtext.ScrolledText(
            note_win, 
            wrap=tk.WORD, 
            font=("Arial", 10),
            bg="#2d2d2d",
            fg="#ffffff"
        )
        text.insert("1.0", self.data.get(video_name, {}).get("notes", ""))
        text.pack(expand=True, fill="both", padx=10, pady=10)

        # ✅ دوال الاختصارات
        def select_all(event):
            text.tag_add("sel", "1.0", "end")
            return "break"  # منع سلوك الافتراضي

        def copy_text(event):
            text.event_generate("<<Copy>>")
            return "break"

        def paste_text(event):
            text.event_generate("<<Paste>>")
            return "break"

        def undo_text(event):
            text.event_generate("<<Undo>>")
            return "break"

        def redo_text(event):
            text.event_generate("<<Redo>>")
            return "break"

        # ✅ ربط الاختصارات
        text.bind("<Control-a>", select_all)
        text.bind("<Control-c>", copy_text)
        text.bind("<Control-v>", paste_text)
        text.bind("<Control-z>", undo_text)
        text.bind("<Control-y>", redo_text)

        # ✅ دالة للحفظ
        def save_only():
            self.data[video_name]["notes"] = text.get("1.0", "end-1c").strip()
            self.save_data()
            print("Notes saved!")

        # ✅ دالة للحفظ والإغلاق
        def save_and_close():
            save_only()
            note_win.destroy()

        # ✅ زر Save & Close
        btn = ttk.Button(
            note_win,
            text="Save & Close",
            command=save_and_close,
            width=15,
            style="Save.TButton"
        )
        btn.pack(pady=5)

        # ✅ ربط Ctrl + S
        note_win.bind("<Control-s>", lambda e: save_only())
        note_win.bind("<Escape>", lambda e: note_win.destroy())

    def run(self):
        root = tk.Tk()
        root.title(f"Video Tracker – {os.path.basename(self.folder)}")
        root.geometry("740x650")
        root.configure(bg="#1e1e1e")

        # ✅ إضافة دعم للأنماط
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except:
            style.theme_use("default")

        # ✅ تعديل الألوان
        dark_bg = "#1e1e1e"
        dark_fg = "#ffffff"
        btn_bg = "#2d2d2d"
        btn_hover = "#3a3a3a"

        style.configure("TFrame", background=dark_bg)
        style.configure("TLabel", foreground=dark_fg, background=dark_bg)
        style.configure("TButton", 
                        background=btn_bg,
                        foreground=dark_fg,
                        borderwidth=0,
                        relief="flat",
                        font=("Arial", 10, "bold"))
        style.map("TButton", 
                  background=[('active', btn_hover)],
                  foreground=[('active', dark_fg)])
        style.configure("TScrolledText", 
                        foreground=dark_fg,
                        background=dark_bg,
                        highlightbackground=dark_bg,
                        highlightcolor=dark_bg)
        style.configure("TCombobox", 
                        background=dark_bg,
                        foreground=dark_fg,
                        fieldbackground=dark_bg,
                        selectbackground=dark_bg)
        style.configure("Note.TButton", 
                        background="#2d2d2d",
                        foreground=dark_fg,
                        borderwidth=0,
                        relief="flat",
                        font=("Arial", 10, "bold"),
                        width=3,
                        height=1)
        style.configure("Save.TButton", 
                        background="#3a3a3a",
                        foreground=dark_fg,
                        borderwidth=0,
                        relief="flat",
                        font=("Arial", 10, "bold"))

        canvas = tk.Canvas(root)
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        def on_mouse_wheel(event):
            if event.num == 4:  # Scroll up
                canvas.yview_scroll(-1, "units")
            elif event.num == 5:  # Scroll down
                canvas.yview_scroll(1, "units")

        canvas.bind_all("<Button-4>", on_mouse_wheel)
        canvas.bind_all("<Button-5>", on_mouse_wheel)

        for video in self.videos:
            frame = ttk.Frame(scrollable_frame)
            frame.pack(fill="x", padx=10, pady=5)

            ttk.Label(frame, text=video, width=50, anchor="w").pack(side="left")

            current_status = self.data.get(video, {}).get("status", "not_started")
            var = tk.StringVar(value=current_status)

            combo = ttk.Combobox(
                frame,
                textvariable=var,
                values=["not_started", "in_progress", "completed"],
                state="readonly",
                width=15
            )
            combo.pack(side="left", padx=5)

            status_label = ttk.Label(frame, text=self.status_labels.get(current_status, current_status))
            status_label.pack(side="left", padx=5)

            def create_callback(vid, lbl, v_var):
                def callback(event):
                    new_val = v_var.get()
                    self.data[vid]["status"] = new_val
                    lbl.config(text=self.status_labels.get(new_val, new_val))
                    
                    # ✅ تغيير لون الخلفية حسب الحالة
                    if new_val == "completed":
                        combo.configure(background="#4CAF50")
                    elif new_val == "in_progress":
                        combo.configure(background="#2196F3")
                    else:
                        combo.configure(background="#FF5722")

                    self.save_data()
                return callback

            combo.bind("<<ComboboxSelected>>", create_callback(video, status_label, var))

            ttk.Button(
                frame,
                text="✍️",
                command=lambda v=video: self.open_notes_editor(v),
                style="Note.TButton"
            ).pack(side="right", padx=(10, 0))

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        button_frame = ttk.Frame(scrollable_frame)
        button_frame.pack(fill="x", padx=10, pady=10)

        btn = ttk.Button(
            button_frame,
            text="Save & Close",
            command=lambda: [self.save_data(), root.destroy()],
            width=15,
            style="Save.TButton"
        )
        btn.pack(side="right", padx=5)

        ttk.Label(button_frame, text="").pack(side="left")
        root.mainloop()

if __name__ == "__main__":
    folder = os.environ.get('CAJA_SCRIPT_CURRENT_URI', '')
    if folder.startswith('file://'):
        folder = folder[7:]
        if not os.path.isdir(folder):
            folder = os.getcwd()
    else:
        folder = os.getcwd()

    app = VideoTrackerApp(folder)
    app.run()
