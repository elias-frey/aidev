
import os # For environment variables and file path operations
from dotenv import load_dotenv # To load .env files
load_dotenv() #loads .env file into environment (make sure the right starting path is set)
folder_path = os.getenv("FOLDER_PATH") #reads from environment
print(folder_path)

# Recursively scanning a folder
def scan_folder_recursively(folder_path):
    results = []
    names = [] # just for showing names in the example usage
    for root, dirs, files in os.walk(folder_path): #os.walk generates the file names in a directory tree by walking the tree either top-down or bottom-up. For each directory in the tree rooted at directory top (including top itself), it yields a 3-tuple (dirpath, dirnames, filenames).
        for file in files:
            file_path = os.path.join(root, file) #combine root and file name to get full file path
            # Filter specific file types, great example of compute efficient file handling (will load filesizes only for those that are needed)
            if not file.lower().endswith(('.txt', '.pdf', '.docx')):
                continue
            file_size = os.path.getsize(file_path)
            results.append({
                    "name": file,
                    "path": file_path,
                    "size_bytes": file_size
            })
            names.append(file) # example usage
    return results, names

# Example usage(s):
#files = scan_folder_recursively(folder_path)
#print(f"Found {len(files)} files \n With following names: \n {files}")
# for f in files:
    # print(f"Name: {f['name']}")
    # print(f"Path: {f['path']}")
    # print(f"Size: {f['size_bytes']} bytes\n")
print(list(os.walk(folder_path))) #converts the generator to a list and prints it