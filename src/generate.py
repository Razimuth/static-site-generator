import os
import shutil
from markdown_to_html import markdown_to_html_node

def copy_directory_all_files(source_dir, destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    else:
        shutil.rmtree(destination_dir)
        os.makedirs(destination_dir)
#        print(f"removed {destination_dir}")

    for item in os.listdir(source_dir):
        source_item_path = os.path.join(source_dir, item)
        destination_item_path = os.path.join(destination_dir, item)

        if os.path.isfile(source_item_path):
            shutil.copy(source_item_path, destination_item_path)
        elif os.path.isdir(source_item_path):
            copy_directory_all_files(source_item_path, destination_item_path)

#        print(f"copied from {source_item_path} to {destination_item_path}")

def generate_page(from_path, template_path, dest_path):
    print(f' "Generating page from {from_path} to {dest_path} using {template_path}."')

    try:
        with open(from_path, 'r') as file:
            markdown_content = file.read()
#        print(f"markdown_content = {markdown_content}")
    except FileNotFoundError:
        print(f"Error: The file '{from_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        with open(template_path, 'r') as file:
            template_content = file.read()
#        print(f"template_content = {template_content}")
    except FileNotFoundError:
        print(f"Error: The file '{from_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    markdown_html = markdown_to_html_node(markdown_content).to_html()
#    print(f"markdown_html = {markdown_html}")
    title = extract_title(markdown_content)
    html_page = template_content.replace("{{ Title }}", title)
    html_page = html_page.replace("{{ Content }}", markdown_html)

#    print(f"html_page = {html_page}")

    with open(dest_path, 'w') as file:
        file.write(html_page)

#    print(f"File '{html_page}' successfully written in '{dest_path}'.")

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            title = line.lstrip("# ").strip()
#            print(f"title = {title}")
            return title
    raise Exception("No h1 heading found")





"""
def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)

def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")
"""