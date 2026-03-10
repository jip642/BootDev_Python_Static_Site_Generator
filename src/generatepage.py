import os
from markdown_to_html import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    
    raise Exception("No title found")


src = os.path.join(os.getcwd(), "src/content", "index.md")
template = os.path.join(os.getcwd(), "template.html")
dest = os.path.join(os.getcwd(), "public", "index.html")

def generate_page(src_path, template_path, dest_path):
    print(f'Generating from {src_path} to {dest_path} using {template_path}')

    with open(src_path, "r") as src_file:
        markdown = src_file.read()

    with open(template_path, "r") as template_file:
        template = template_file.read()

    html_node = markdown_to_html_node(markdown)
    html_content = html_node.to_html()

    title = extract_title(markdown)

    page = template.replace("{{title}}", title)
    page = page.replace("{{content}}", html_content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as dest_file:
        dest_file.write(page)

    print(html_content)

generate_page(src, template, dest)
