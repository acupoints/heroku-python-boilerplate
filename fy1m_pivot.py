import os
import sys

def get_all_files(static_dir):
    fragment_files = []
    for root, dirs, files in os.walk(static_dir):
        if root.startswith("{}static".format(static_dir)):
            pass
        else:
            temp_root = "/"+root.split("/",2)[2]
            fragment_files = fragment_files + [temp_root+files_el for files_el in files]
    return fragment_files

if __name__ == "__main__":
    # Retrieve all files with missing directory fragments
    if len(sys.argv) > 1:
        static_dir = sys.argv[1]
        fragment_files = get_all_files(static_dir)
        # print("{}".format(fragment_files))
        # Complete all links that appear in the missing directory fragments in index.html
        # href="/favicon.ico"
        # href="/logo192.png"
        # href="/manifest.json"
        source_file = "apis/templates/index.html"
        target_file = source_file
        source_file_lines = []
        try:
            with open(source_file, "r", encoding="utf-8") as sf:
                for sf_line in sf:
                    source_file_lines.append(sf_line)
        except Exception as ex:
            print(ex)
        # List to string
        source_file_lines_new = "".join(source_file_lines)
        # Supplement all folder fragments
        print("--- {}".format("The following files can be filled with the directory fragment /static"))
        print("-"*32)
        for fragment_files_el in fragment_files:
            if 'href="{}"'.format(fragment_files_el) in source_file_lines_new:
                print('[Src] href="{}"'.format(fragment_files_el))
                print('[Dst] href="/static{}"'.format(fragment_files_el))
                print("-"*0)
            source_file_lines_new = source_file_lines_new.replace('href="{}"'.format(fragment_files_el), 'href="/static{}"'.format(fragment_files_el))

        try:
            with open(target_file, "w", encoding="utf-8") as tf:
                tf.write("".join(source_file_lines_new))
                print("-"*32)
                print("--- Write successful")
        except Exception as ex:
            print("-"*32)
            print("--- Write failed")
            print(ex)

    else:
        print("--- {}".format("Missing required parameters"))
        print("--- {}".format("Please specify a destination folder"))
        print("eg. {}".format("python fy1m_pivot.py apis/templates/"))
    pass