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

def categorize_products_by_detailed_path(products):
    categories = defaultdict(lambda: defaultdict(list))
    for product in products:
        path_parts = [part.strip() for part in product['category_path'].split(';') if part]
        if len(path_parts) > 2:
            main_cat = path_parts[0]
            sub_cat = path_parts[2] # Use the third level as the sub-category
            categories[main_cat][sub_cat].append(product['name'])
        elif len(path_parts) > 1:
            main_cat = path_parts[0]
            sub_cat = path_parts[1]
            categories[main_cat][sub_cat].append(product['name'])

    return categories

def format_as_markdown(categorized_products):
    markdown_string = ""
    for main_cat, sub_cats in sorted(categorized_products.items()):
        markdown_string += f"# {main_cat}\n\n"
        for sub_cat in sorted(sub_cats.keys()):
            products = sub_cats[sub_cat]
            markdown_string += f"- {sub_cat}: {len(products)}\n"
            for product in sorted(products):
                markdown_string += f"  - {product}\n"
        markdown_string += "\n"
    return markdown_string.strip()

if __name__ == "__main__":
    product_dir = 'product_categorization'
    output_file = 'product_sub_category.md'

    products = parse_product_files(product_dir)
    categorized_products = categorize_products_by_detailed_path(products)
    markdown_output = format_as_markdown(categorized_products)

    with open(output_file, 'w') as f:
        f.write(markdown_output)
    
    print(f"Successfully updated {output_file} with detailed categories.")
