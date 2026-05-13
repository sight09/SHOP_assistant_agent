import pandas as pd
import os

class ProductDatabase:
    """Handle all product database operations"""
    
    def init(self, csv_path='data/products.csv'):
        self.csv_path = csv_path
        self.products = self.load_products()
    
    def load_products(self):
        """Load products from CSV file"""
        if os.path.exists(self.csv_path):
            return pd.read_csv(self.csv_path)
        else:
            return pd.DataFrame(columns=[
                'product_id', 'name_en', 'name_am', 'name_oro',
                'brand', 'category', 'price', 'specification',
                'description_en', 'image_url'
            ])
    
    def search_products(self, query, language='en'):
        """Search products by name or description"""
        if self.products.empty:
            return pd.DataFrame()
        
        query_lower = query.lower()
        name_col = 'name_en'
        desc_col = 'description_en'
        
        mask = (
            self.products[name_col].str.contains(query_lower, case=False, na=False) |
            self.products[desc_col].str.contains(query_lower, case=False, na=False)
        )
        return self.products[mask]
    
    def filter_by_category(self, category):
        """Filter products by category"""
        if self.products.empty or category == 'All':
            return self.products
        return self.products[self.products['category'] == category]
    
    def filter_by_price_range(self, min_price, max_price):
        """Filter products by price range"""
        if self.products.empty:
            return pd.DataFrame()
        return self.products[
            (self.products['price'] >= min_price) & 
            (self.products['price'] <= max_price)
        ]
    
    def filter_by_brand(self, brand):
        """Filter products by brand"""
        if self.products.empty:
            return pd.DataFrame()
        return self.products[self.products['brand'] == brand]
    
    def get_product_by_id(self, product_id):
        """Get specific product by ID"""
        if self.products.empty:
            return pd.DataFrame()
        return self.products[self.products['product_id'] == product_id]
    
    def get_all_categories(self):
        """Get list of all categories"""
        if self.products.empty:
            return []
        return self.products['category'].unique().tolist()
    
    def get_all_brands(self):
        """Get list of all brands"""
        if self.products.empty:
            return []
        return self.products['brand'].unique().tolist()