import os
def rename_files():

    file_list = os.listdir(r"F:\Pictures\Me")
    print(file_list)
    saved_path = os.getcwd()
    print("Current working directory is " +saved_path)
    os.chdir(r"F:\Pictures\Me")

    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "_[].+)("))
        os.chdir(saved_path)
        
    rename_files()
