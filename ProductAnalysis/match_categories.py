
import csv
import re
import sys

def find_best_match(product_name, categories, product_category):
    best_match = ""
    max_score = 0

    # Map product category to the top-level category in AmazonCategories.csv
    category_mapping = {
        "baby": "Baby Products",
        "beauty": "Beauty & Personal Care",
        "clothing": "Clothing, Shoes & Jewelry",
        "home": "Home & Kitchen",
        "pet": "Pet Supplies",
        "tools": "Tools & Home Improvement"
    }
    mapped_category = category_mapping.get(product_category.lower(), product_category)


    filtered_categories = [cat for cat in categories if cat.lower().startswith(mapped_category.lower())]

    if not filtered_categories:
        filtered_categories = categories

    product_words = set(re.split(r'[\s,;\-/|()]', product_name.lower()))

    for category in filtered_categories:
        category_parts = category.split(';')
        category_words = set(re.split(r'[\s,;\-/|()]', category.lower()))
        
        score = len(product_words.intersection(category_words))
        
        depth_bonus = len([part for part in category_parts if part]) / 10.0
        score += depth_bonus

        if score > max_score:
            max_score = score
            best_match = category

    return best_match

with open("/Users/zhoufan/Public/workspace/seo_data/ProductAnalysis/AmazonCategories.csv", 'r') as categories_file:
    categories = [line.strip() for line in categories_file.readlines()]

product_file_path = sys.argv[1]

with open(product_file_path, 'r') as products_file:
    # Skip the first two lines
    for _ in range(2):
        next(products_file)
    reader = csv.DictReader(products_file)
    for row in reader:
        product_name = row["Product Name"]
        # The category is the filename without the extension
        product_category = product_file_path.split('/')[-1].split('.')[0]
        best_category = find_best_match(product_name, categories, product_category)
        print(f"Product: {product_name}")
        print(f"Best Match: {best_category}")
        print("-" * 20)
