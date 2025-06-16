
# 🧠 Virtual Assistant with Python

This is a voice-activated **Virtual Assistant** built using Python. It can perform a variety of tasks such as opening websites, searching information online, telling the time, and much more — all using simple **voice commands**.

Whether you're learning Python or building smart automation tools, this project is a great start for hands-free computing.

---

## 📌 Features

✅ Voice input recognition  
✅ Text-to-speech response  
✅ Tells current time and date  
✅ Opens apps and websites  
✅ Performs Google searches  
✅ YouTube search with voice  
✅ Easy to extend with new commands

---

## 🧰 Tech Stack

| Component         | Library              | Purpose                          |
|------------------|----------------------|----------------------------------|
| 🎤 Voice Input    | `speech_recognition` | Captures and interprets speech   |
| 🔊 TTS Output     | `pyttsx3`            | Converts text responses to audio |
| 🌐 Web Control    | `webbrowser`         | Opens websites like Google, YT   |
| 🕒 Time Handling  | `datetime`           | Gets current time and date       |
| 💻 System Access | `os`                 | Launches local apps              |

---

## 📦 Installation Guide

1. **Clone the repository:**
```bash
git clone https://github.com/alokbhateshwar/virtual-assistant.git
cd virtual-assistant
````

2. **Install the dependencies:**

```bash
pip install pyttsx3 SpeechRecognition pyaudio
```

> ⚠️ If you get errors with `pyaudio`, install it using a `.whl` file:
> [Download PyAudio Wheel](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)

---

## ▶️ How to Run

Simply run the assistant script:

```bash
python assistant.py
```

The assistant will activate and listen for your voice commands.

---

## 🗣️ Sample Commands You Can Try

| 🗣️ Say This                         | 🤖 Assistant Does This                                    |
| ------------------------------------ | --------------------------------------------------------- |
| "What time is it?"                   | Speaks the current time                                   |
| "Open Google"                        | Opens [https://google.com](https://google.com) in browser |
| "Search Python tutorials on YouTube" | Searches YouTube for Python tutorials                     |
| "Open Notepad"                       | Launches Notepad app                                      |
| "Exit" or "Quit"                     | Stops the assistant                                       |

---

## 🧩 File Structure

```
virtual-assistant/
│
├── assistant.py         # Main program logic
├── README.md            # Project documentation
├── requirements.txt     # (Optional) List of packages
└── LICENSE              # MIT License
```

---

## 🌟 Future Upgrades

* Add GUI using Tkinter or PyQt
* Integrate weather/news APIs
* Add chatbot capabilities using NLP (spaCy or transformers)
* Store command history and logs
* Enable multi-language support

---

## 📸 Screenshots / Demo

*(Add screenshots or GIFs of your assistant in action if available)*

---

## 🧑‍💻 Author

**Alok Bhateshwar**
🌐 [GitHub Profile](https://github.com/alokbhateshwar)

---

## 📄 License

Licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute.

---

## 🙌 Contributions Welcome!

If you’d like to improve the assistant, add more voice commands, or integrate APIs — contributions are welcome! Just fork the repo, make your changes, and submit a pull request.

````

---

### ✅ Next Steps for You:
- Copy-paste this into your `README.md` file in your `virtual-assistant` repo.
- Add a screenshot or demo GIF if possible.
- (Optional) Create a `requirements.txt`:
```bash
pip freeze > requirements.txt
