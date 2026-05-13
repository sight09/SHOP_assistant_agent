# SmartShop Electronics

SmartShop Electronics is a Streamlit-based shopping assistant application that uses AI to help users explore electronics products. It loads product data from `data/products.csv`, supports natural language questions, and shows recommended items based on the product catalog.

## Features

- AI-powered product search and chat interface
- Multilingual support for English, Amharic, and Afaan Oromo
- Product filtering by category and price range
- Display of matching product images when available
- Dark-themed UI with an interactive sidebar

## Requirements

- Python 3.8+
- streamlit
- pandas
- python-dotenv
- openai
- langdetect
- googletrans

## Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your OpenRouter API key to a `.env` file:
   ```text
   OPENROUTER_API_KEY=your_api_key_here
   ```
4. Run the app:
   ```bash
   streamlit run app.py
   ```

## Notes

- The app uses OpenRouter via the OpenAI-compatible SDK.
- If required packages are missing, the app prints installation hints.
- Images are shown only when valid URLs are included in the product dataset.
