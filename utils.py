# UI Translations and Utilities

UI_TRANSLATIONS = {
    'en': {
        'welcome': '🛒 Welcome to SmartShop Electronics!',
        'ask_question': 'Ask me about our products, prices, and specifications',
        'search_placeholder': 'Search for products or ask a question...',
        'categories': 'Filter by Category',
        'price_range': 'Price Range (Birr)',
        'brands': 'Featured Brands',
        'no_results': '❌ Sorry, I couldn\'t find products matching your query.',
        'found_results': '✅ Found these products for you:',
        'price': 'Price',
        'specification': 'Specs',
        'brand': 'Brand',
        'category': 'Category',
        'description': 'Description',
        'clear_chat': '🔄 Clear Chat',
        'language': 'Language',
        'all_categories': 'All Categories',
    },
    'am': {
        'welcome': '🛒 ወደ SmartShop ኤሌክትሮኒክስ እንኳን በደህና መጡ!',
        'ask_question': 'ስለ ምርቶቻችን, ዋጋ እና ባህሪያት ጠይቁ',
        'search_placeholder': 'ምርቶችን ይፈልጉ ወይም ጥያቄ ጠይቁ...',
        'categories': 'እንደ ምድብ ማጣሪያ',
        'price_range': 'የዋጋ ክልል (Birr)',
        'brands': 'ታዋቂ ዕቃዎች',
        'no_results': '❌ ይቅርታ፣ ጥያቄዎ ጋር ሚዛመድ ምርት ማግኘት አልቻለም።',
        'found_results': '✅ ለእርስዎ የሚመጣ ምርቶች እዚህ አሉ:',
        'price': 'ዋጋ',
        'specification': 'ባህሪያት',
        'brand': 'ብራንድ',
        'category': 'ምድብ',
        'description': 'መግለጫ',
        'clear_chat': '🔄 ውይይት ንፅህ',
        'language': 'ቋንቋ',
        'all_categories': 'ሁሉም ምድቦች',
    },
    'oro': {
        'welcome': '🛒 Gara SmartShop Electronics baga nagaan dhuftan!',
        'ask_question': 'Waa\'ee oomisha, gatii fi sifaatti keenyaa gaafadha',
        'search_placeholder': 'Oomisha barbaadi ykn gaaffii gaafadha...',
        'categories': 'Gosoota Barbaadi',
        'price_range': 'Hangilaa Gatii (Birr)',
        'brands': 'Maqoota Beekamaa',
        'no_results': '❌ Dhiif, gaaffii keetii wajjin oomisha arguu hin dandeenye.',
        'found_results': '✅ Oomisha kana argisiisaa:',
        'price': 'Gatii',
        'specification': 'Sifaatni',
        'brand': 'Maqaa',
        'category': 'Gosaa',
        'description': 'Ibsa',
        'clear_chat': '🔄 Haaruu Haasawa',
        'language': 'Afaan',
        'all_categories': 'Gosoonni Hunduu',
    }
}

def get_translation(key, language='en'):
    """Get translation for a key in specified language"""
    return UI_TRANSLATIONS.get(language, {}).get(key, key)

def format_price(price):
    """Format price with currency"""
    return f"₦{price:,} Birr"

def format_product_card(product, language='en'):
    """Format product information for display"""
    translations = UI_TRANSLATIONS.get(language, UI_TRANSLATIONS['en'])
    
    card = f"""
{product['name_en']}

{translations['brand']}: {product['brand']}
{translations['category']}: {product['category']}
{translations['price']}: {format_price(product['price'])}
{translations['specification']}: {product['specification']}
{translations['description']}: {product['description_en']}

---
"""
    return card

def get_database_stats(df):
    """Get statistics about the product database"""
    if df.empty:
        return {}
    
    stats = {
        'total_products': len(df),
        'total_categories': df['category'].nunique(),
        'total_brands': df['brand'].nunique(),
        'avg_price': int(df['price'].mean()),
        'min_price': int(df['price'].min()),
        'max_price': int(df['price'].max()),
    }
    
    return stats