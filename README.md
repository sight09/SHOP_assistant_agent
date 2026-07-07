<h1 align="center">🛒 SmartShop Electronics </h1>

<p align="center">
  <img src="assets/banner.png" width="100%" alt="SmartShop Electronics Bannerr">
</p>

<p align="center">
<b>AI-Powered Multilingual Shopping Assistant</b><br>
Helping users discover electronics products using conversational AI, intelligent search, and personalized recommendations.
</p>
<p align="center">
<img src="https://img.shields.io/badge/Python-3.11-blue?logo=python">

<img src="https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit">

<img src="https://img.shields.io/badge/OpenRouter-LLM-purple">

<img src="https://img.shields.io/badge/OpenAI-Compatible-success">

<img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas">

<img src="https://img.shields.io/badge/License-MIT-green">

</p>

---

# 📖 Overview

SmartShop Electronics is an **AI-powered multilingual shopping assistant** built with **Python**, **Streamlit**, and **OpenRouter**.

Instead of browsing through hundreds of products manually, users can simply ask questions in natural language such as:

> "Show me gaming laptops under 70,000 ETB."

or

> "Recommend a smartphone with a good camera."

The AI understands the request, searches the product catalog, and returns personalized recommendations along with product images and pricing.

The application supports **English**, **Amharic**, and **Afaan Oromo**, making it accessible to a wider audience.

---

# ✨ Features

- 🤖 AI-powered conversational shopping assistant
- 🌍 Multilingual support (English, Amharic, Afaan Oromo)
- 🔎 Intelligent product search
- 💬 Natural language recommendations
- 🖼️ Product image previews
- 📂 Product category filtering
- 💰 Price range filtering
- ⚡ Fast Streamlit interface
- 🌙 Modern dark-themed UI
- 🔐 Secure API key management using `.env`
- 📊 CSV-based product database

---

# 🏗️ Architecture

```text
                    User
                      │
                      ▼
               Streamlit Interface
                      │
                      ▼
           Language Detection Module
                      │
                      ▼
              OpenRouter AI Model
                      │
         ┌────────────┴────────────┐
         ▼                         ▼
 Product Recommendation      Translation Module
         │
         ▼
     Products.csv
```

---

# 🛠 Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Streamlit | Web Interface |
| OpenRouter | AI Model |
| OpenAI SDK | API Client |
| Pandas | Product Processing |
| LangDetect | Language Detection |
| GoogleTrans | Translation |
| Python-dotenv | Environment Variables |

---

# 📂 Project Structure

```text
SmartShop-Electronics/
│
├── assets/
│   ├── banner.png
│
├── data/
│   └── products.csv
│
├── app.py
├── requirements.txt
├── .env.example
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/SmartShop-Electronics.git
```
Navigate into the project

```bash
cd SmartShop-Electronics
```
Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```
Install dependencies

```bash
pip install -r requirements.txt
```
---

#🔑 Configuration

Create a `.env` file.

```env
OPENROUTER_API_KEY=your_api_key_here
```
---

#▶️ Run the Application

```bash
streamlit run app.py
```

The application will start locally at

```
http://localhost:8501
```

---

#💬 Example Questions

You can ask questions like:

```text
Show me gaming laptops under 70,000 ETB.

Recommend a smartphone with a great camera.

I need wireless headphones for music.

Find smartwatches below 10,000 ETB.

Show me the cheapest laptops.
```

---

# 🌍 Supported Languages

- 🇺🇸 English
- 🇪🇹 Amharic
- 🌍 Afaan Oromo

The application automatically detects the user's language and responds appropriately.

---

# 🚀 Future Improvements

- 👤 User authentication
- ❤️ Wishlist
- 🛒 Shopping cart
- 💳 Online checkout
- ⭐ Product ratings
- 🧠 Personalized recommendations
- 🎤 Voice assistant
- 📷 Image-based product search
- ☁️ PostgreSQL database
- 📱 Mobile responsive design
- 📊 Admin dashboard
- 📦 Inventory management

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Added new feature"
```

4. Push to your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

# 📄 License

This project is licensed under the MIT License.

---

<p align="center">
⭐ If you found this project helpful, consider giving it a star on GitHub !
</p>
