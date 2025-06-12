# 🖋️ InkQ — Scribble Recognition Web App

InkQ is an intelligent web application that turns your freehand scribbles into meaningful insights — whether it’s solving mathematical expressions, interpreting equations, or understanding abstract visual concepts. Just draw, and let the AI do the thinking.

![InkQ Demo Banner](banner_placeholder.png) <!-- Replace with actual banner image -->

---

## 🚀 Features

- 🎨 **Canvas Drawing**: A blackboard-like canvas where users can freely scribble.
- 🌈 **Swatch Palette**: Choose from multiple ink colors for a custom drawing experience.
- 🧠 **AI-Powered Recognition**: Converts the canvas image into expressions or answers using Google’s Gemini AI (Vision model).
- 📐 **LaTeX Rendering**: Dynamically renders mathematical results using MathJax.
- 🖱️ **Draggable Results**: Move and reposition result overlays easily.
- 🔁 **Reset & Run Controls**: Interactive buttons to manage the canvas lifecycle.
- 🧠 **Memory & Variables**: Handles variable assignments and multi-step logic.

---

## 🛠️ Tech Stack

| Frontend       | Backend           | AI/ML               | Utilities           |
|----------------|-------------------|---------------------|---------------------|
| React.js       | FastAPI (Python)  | Gemini Pro Vision   | Pillow (Image I/O)  |
| Tailwind CSS   | Uvicorn (Server)  | Google Generative AI| MathJax, Axios      |
| Mantine UI     |                   |                     | React-Draggable     |

---

## 📷 How It Works

1. User draws a sketch or scribbles a math expression.
2. The canvas is converted to an image and sent to the backend.
3. Backend sends the image + prompt to **Gemini AI** using `google.generativeai`.
4. The response is parsed, structured into:
   - Raw Expression
   - Evaluated Answer
   - Optional LaTeX version
5. Frontend displays the result as draggable LaTeX overlay.

---

## 📦 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/inkq.git
cd inkq
```

### 2. Frontend

```bash
cd frontend
npm install
npm run dev
```

### 3. Backend (Python 3.10+)

```bash
cd backend
pip install -r requirements.txt
python main.py
```

### 🔐 API Configuration
```.env
GEMINI_API_KEY=your_api_key
```

### 📌 Folder Structure

```bash
InkQ/
├── backend/
│   ├── main.py
│   ├── model.py
│   ├── utils/
│   ├── .env.example
│   └── ...
├── frontend/
│   ├── public/
│   ├── components/
│   ├── App.tsx
│   ├── .env.local
│   └── ...
└── README.md
```

## 📚 Example Use Cases

1. 🧮 Quick evaluation of handwritten math problems
2. 🧑‍🏫 Teaching tool to show AI-driven understanding of symbols
3. 📲 Future possibility: use with stylus or mobile devices for real-time input
4. 🔍 Research tool for human-AI visual communication

## 🙌 Acknowledgements
- Google Generative AI
- Mantine UI
- MathJax
- Pillow