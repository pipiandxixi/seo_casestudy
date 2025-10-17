import re
from collections import defaultdict
import os

def parse_product_files(directory):
    products = []
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            with open(os.path.join(directory, filename), 'r') as f:
                content = f.read()
                for product_block in content.split('--------------------'):
                    if product_block.strip():
                        product_name_match = re.search(r"Product: (.*)", product_block)
                        best_match_match = re.search(r"Best Match: (.*)", product_block)
                        if product_name_match and best_match_match:
                            product_name = product_name_match.group(1).strip()
                            best_match = best_match_match.group(1).strip()
                            products.append({"name": product_name, "category_path": best_match})
    return products

def parse_sub_category_file(filepath):
    categories = defaultdict(lambda: defaultdict(list))
    current_category = None
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('# '):
                current_category = line[2:].strip()
            elif line.startswith('- '):
                sub_category_name = line.split(':')[0][2:].strip()
                if current_category:
                    categories[current_category][sub_category_name] = []
    return categories

def get_main_category_key(product_main_cat, categories):
    # Exact match first
    if product_main_cat in categories:
        return product_main_cat
    # Then case-insensitive
    for cat_key in categories:
        if cat_key.lower() == product_main_cat.lower():
            return cat_key
    # Then partial match
    for cat_key in categories:
        if cat_key.lower() in product_main_cat.lower() or product_main_cat.lower() in cat_key.lower():
            return cat_key
    return None

def get_sub_category_key(product_sub_cat, sub_categories):
    # Exact match first
    if product_sub_cat in sub_categories:
        return product_sub_cat
    # Then case-insensitive
    for sub_cat_key in sub_categories:
        if sub_cat_key.lower() == product_sub_cat.lower():
            return sub_cat_key

    # Then partial match, preferring longer matches
    best_match = None
    # Match based on starting words
    for sub_cat_key in sub_categories:
        if product_sub_cat.lower().startswith(sub_cat_key.lower()):
            if best_match is None or len(sub_cat_key) > len(best_match):
                best_match = sub_cat_key
    if best_match:
        return best_match

    # More fuzzy matching
    words_in_product_sub_cat = set(product_sub_cat.lower().replace('&', ' ').split())
    for sub_cat_key in sub_categories:
        words_in_key = set(sub_cat_key.lower().replace('&', ' ').split())
        if len(words_in_product_sub_cat.intersection(words_in_key)) > 0:
             if best_match is None or len(sub_cat_key) > len(best_match):
                best_match = sub_cat_key

    return best_match


def categorize_products(products, categories):
    for product in products:
        path_parts = [part.strip() for part in product['category_path'].split(';') if part]
        if len(path_parts) > 1:
            main_cat_from_product = path_parts[0]
            sub_cat_from_product = path_parts[1]

            main_cat_key = get_main_category_key(main_cat_from_product, categories)

            if main_cat_key:
                sub_cat_key = get_sub_category_key(sub_cat_from_product, categories[main_cat_key])

                if sub_cat_key:
                    categories[main_cat_key][sub_cat_key].append(product['name'])
                elif "Other" in categories[main_cat_key]:
                     categories[main_cat_key]["Other"].append(product['name'])

    return categories

def format_as_markdown(categorized_products):
    markdown_string = ""
    for main_cat, sub_cats in sorted(categorized_products.items()):
        markdown_string += f"# {main_cat}\n\n"
        # Sort sub-categories by name for consistent output
        for sub_cat in sorted(sub_cats.keys()):
            products = sub_cats[sub_cat]
            markdown_string += f"- {sub_cat}: {len(products)}\n"
            for product in sorted(products):
                markdown_string += f"  - {product}\n"
        markdown_string += "\n"
    return markdown_string.strip()

if __name__ == "__main__":
    product_dir = 'product_categorization'
    sub_category_file = 'product_sub_category.md'

    products = parse_product_files(product_dir)
    categories = parse_sub_category_file(sub_category_file)
    categorized_products = categorize_products(products, categories)
    markdown_output = format_as_markdown(categorized_products)

    with open(sub_category_file, 'w') as f:
        f.write(markdown_output)
    
    print(f"Successfully updated {sub_category_file}")