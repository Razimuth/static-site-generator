import os
import shutil
from generate import copy_directory_all_files, generate_page

def main():
#    textnode = TextNode("Hello World", TextType.LINK, "http://localhost:8888")

#    print(textnode)
    source_dir = "static"
    destination_dir = "public"
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
    copy_directory_all_files(source_dir, destination_dir)
#    print(f"Contents copied from '{source_dir}' to '{destination_dir}'")
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
        main()


"""
dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html"),
    )

"""