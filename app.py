# app.py

try:
    import streamlit as st
except Exception:
    print("⚠️ streamlit is not installed. Install it with: pip install streamlit")
    print("Then run the app with: streamlit run app.py")
    import sys
    sys.exit(1)

import pandas as pd
import os

# ---------------------------
# Load environment variables
# ---------------------------
try:
    from dotenv import load_dotenv
    load_dotenv()  # Loads .env into environment
except ImportError:
    print("⚠️ python-dotenv not installed. Make sure OPENAI_API_KEY and OPENAI_API_BASE are set manually.")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_BASE = "https://openrouter.ai/api/v1"

os.environ["OPENAI_API_KEY"] = OPENROUTER_API_KEY  # Some libs still check this
os.environ["OPENAI_API_BASE"] = OPENROUTER_API_BASE


# ---------------------------
# OpenAI / OpenRouter SDK
# ---------------------------
try:
    from openai import OpenAI
except ImportError:
    OpenAI = None
    print("⚠️ openai package not installed. Run 'pip install openai'.")

client = None
if OpenAI and OPENROUTER_API_KEY:
    try:
        client = OpenAI(
            api_key=OPENROUTER_API_KEY,
            base_url=OPENROUTER_API_BASE
        )
    except Exception as e:
        print(f"⚠️ Failed to create OpenRouter client: {e}")


# ---------------------------
# Language detection
# ---------------------------
try:
    from langdetect import detect, LangDetectException
except ImportError:
    # Fallback to English if langdetect not installed
    def detect(text):
        return "en"

    class LangDetectException(Exception):
        pass

try:
    from googletrans import Translator
    _translator = Translator()
except Exception:
    _translator = None

# ---------------------------
# Streamlit page config
# ---------------------------
st.set_page_config(
    page_title="SmartShop Electronics",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark theme
st.markdown("""
<style>
    .stApp { background-color: #1a1a1a; color: #ffffff; }
    .stChatMessage { background-color: #2d2d2d; border-radius: 10px; padding: 15px; margin: 10px 0; }
    .stButton > button { background-color: #4a9eff; color: white; border: none; border-radius: 8px; padding: 10px 20px; font-weight: bold; }
    .stButton > button:hover { background-color: #357abd; }
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Load products CSV
# ---------------------------
@st.cache_data
def load_products():
    csv_path = os.path.join("data", "products.csv")
    try:
        df = pd.read_csv(csv_path)

        # Ensure required columns exist (added image_url)
        required_cols = {"name_en", "brand", "category", "price", "specification", "image_url"}
        for col in required_cols:
            if col not in df.columns:
                df[col] = ""

        # Ensure price is numeric
        df["price"] = pd.to_numeric(df["price"], errors="coerce")
        df = df.dropna(subset=["price"]).reset_index(drop=True)
        return df
    except Exception:
        return pd.DataFrame(columns=["name_en", "brand", "category", "price", "specification", "image_url"])

# ---------------------------
# AI response function
# ---------------------------
def get_ai_response(user_query, df, language="en"):
    if df.empty:
        return "❌ No products available."

    # Build product catalog including image URLs
    product_list = "\n".join(
        f"- {row['name_en']}: {row['brand']} ({row['category']}), Price: {row['price']} Birr, Specs: {row['specification']}, Image: {row.get('image_url', 'N/A')}"
        for idx, row in df.iterrows()
    )

    system_prompt = f"""
You are a helpful shopping assistant.

Use the product list below to find relevant matches for the user query.
Respond in {language}.

Product list:
{product_list}
"""

    if client is None:
        return "❌ OpenAI/OpenRouter client not available."

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query}
            ],
            temperature=0.7,
            max_tokens=500
        )

        if hasattr(response, "choices") and len(response.choices) > 0:
            choice = response.choices[0]
            if hasattr(choice, "message") and hasattr(choice.message, "content"):
                return choice.message.content
            elif hasattr(choice, "text"):
                return choice.text
        return str(response)
    except Exception as e:
        return f"❌ Error: {e}"

# ---------------------------
# Session state
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.products_df = load_products()
    st.session_state.language = "en"

# ---------------------------
# Sidebar
# ---------------------------
with st.sidebar:
    st.markdown("### 🛍 SmartShop Electronics")
    st.markdown("---")

    language_options = {
        "en": "🇬🇧 English",
        "am": "🇪🇹 Amharic",
        "oro": "🇪🇹 Afaan Oromo"
    }
    selected_lang = st.selectbox(
        "Select Language",
        options=list(language_options.keys()),
        format_func=lambda x: language_options[x],
        key="language_select"
    )
    st.session_state.language = selected_lang

    st.markdown("---")
    st.subheader("🏷 Filter by Category")
    if not st.session_state.products_df.empty:
        categories = ["All"] + st.session_state.products_df["category"].unique().tolist()
        selected_category = st.selectbox("Select Category", categories, key="category_select")

        st.subheader("💰 Price Range")
        min_price = int(st.session_state.products_df["price"].min())
        max_price = int(st.session_state.products_df["price"].max())
        price_range = st.slider("Select price range (Birr)", min_price, max_price, (min_price, max_price), step=5000)

    st.markdown("---")
    st.subheader("⭐️ Featured Brands")
    if not st.session_state.products_df.empty:
        for brand in st.session_state.products_df["brand"].unique()[:5]:
            st.caption(f"• {brand}")

    st.markdown("---")
    st.info("💡 Tip: Ask natural questions like 'Show laptops under 50000' or 'Do you have cheap phones?'")

# ---------------------------
# Main chat
# ---------------------------
col1, col2 = st.columns([3, 1])
with col1:
    st.title("💬 SmartShop AI Assistant")
with col2:
    if st.button("🔄 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

st.markdown("---")
st.markdown("Ask me anything about our products! I understand natural language questions. 🤖")

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Type your question here...", key="user_input")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("🤖 Thinking..."):
            response = get_ai_response(user_input, st.session_state.products_df, st.session_state.language)
            st.markdown(response)

            # 🖼️ Display matching product images in a grid
            df = st.session_state.products_df
            matched = [
                row for _, row in df.iterrows()
                if row["name_en"].lower() in response.lower() and str(row.get("image_url", "")).startswith("http")
            ]

            if matched:
                st.markdown("### 🖼️ Matching Products")
                cols = st.columns(3)
                for i, row in enumerate(matched):
                    with cols[i % 3]:
                        st.image(
                            row["image_url"],
                            caption=f"{row['name_en']} - {row['price']} Birr",
                            use_container_width=True
                        )

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666666; font-size: 12px;'>
    <p>🏪 SmartShop Electronics | 📞 +251 911 000 000 | 📧 info@smartshop.et</p>
    <p>Powered by AI | Last updated: 2025</p>
</div>
""", unsafe_allow_html=True)
