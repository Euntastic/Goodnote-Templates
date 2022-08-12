# Convert svg templates into pdfs

# Looking for a viable way to convert svg to pdfs.

import os

for subdir, dirs, files in os.walk("svg"):
    for file in files:
        if os.name == 'nt':
            path_sep = "\\"
        else:
            path_sep = "/"
        
        file_path = subdir + path_sep + file
        save_path = file_path.replace("svg", "pdf")
        print(file_path)
        print(save_path)
        
