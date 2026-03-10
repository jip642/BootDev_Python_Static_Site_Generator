import os
from markdown_to_html import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    
    raise Exception("No title found")


# src = os.path.join(os.getcwd(), "src/content", "index.md")
# template = os.path.join(os.getcwd(), "template.html")
# dest = os.path.join(os.getcwd(), "public", "index.html")

def generate_page(src_path, template_path, dest_path, basepath="/"):
    print(f'Generating from {src_path} to {dest_path} using {template_path}')

    with open(src_path, "r") as src_file:
        markdown = src_file.read()

    with open(template_path, "r") as template_file:
        template = template_file.read()

    html_node = markdown_to_html_node(markdown)
    html_content = html_node.to_html()

    title = extract_title(markdown)

    page = template.replace("{{ Title }}", title)
    page = page.replace("{{ Content }}", html_content)
    page = page.replace('href="/', f'href="{basepath}')
    page = page.replace('src="/', f'src="{basepath}')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as dest_file:
        dest_file.write(page)

def generate_pages_recursive(content_dir, template_path, dest_dir, root_content_dir=None, basepath="/"):
    if root_content_dir is None:
        root_content_dir = os.path.abspath(content_dir)

    os.makedirs(dest_dir, exist_ok=True)

    for f in os.listdir(content_dir):
        content_path = os.path.join(content_dir, f)
        dest_path = os.path.join(dest_dir, f)

        if os.path.isdir(content_path):
            os.makedirs(dest_path, exist_ok=True)
            generate_pages_recursive(content_path, template_path, dest_path, root_content_dir, basepath)
        else:
            name, ext = os.path.splitext(f)
            if ext.lower() != ".md":
                continue
            in_nested_dir = os.path.abspath(content_dir) != root_content_dir
            if in_nested_dir and name == "index":
                output_name = os.path.basename(content_dir) + ".html"
            else:
                output_name = name + ".html"
            dest_path = os.path.join(dest_dir, output_name)
            generate_page(content_path, template_path, dest_path, basepath)
