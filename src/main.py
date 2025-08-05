import os
import shutil
from generate import copy_directory_all_files, generate_pages_recursive  #, generate_page,

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
#    textnode = TextNode("Hello World", TextType.LINK, "http://localhost:8888")

#    print(textnode)
    source_dir = "./static"
    destination_dir = "./public"
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    copy_directory_all_files(dir_path_static, dir_path_public)
#    print(f"Contents copied from '{source_dir}' to '{destination_dir}'")
#    generate_page(os.path.join(dir_path_content, "index.md"),
#                   template_path, os.path.join(dir_path_public, "index.html"))
    print(f' "Generating page from {dir_path_content} to {dir_path_public} using {template_path}."')
    generate_pages_recursive(dir_path_content, template_path, dir_path_public) #"./content/", "./template.html", "./public/")

if __name__ == "__main__":
        main()


"""

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)

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