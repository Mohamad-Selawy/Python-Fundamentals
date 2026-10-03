import os

# Define the directory where your notebooks live
source_folder = r'C:\Users\moham\OneDrive\Documents\GitHub\Python-Fundamentals\notebooks'
print('Source directory:', source_folder)

# Define the mapping from current filenames to desired target filenames
rename_mapping = {
    "Ch00-IntroCourseTableOfContents.ipynb": "Ch00-IntroCourseTableOfContents.ipynb",
    "Ch01-Introduction.ipynb": "Ch01-Introduction.ipynb",
    "Ch02-Data-Variables-StdIO.ipynb": "Ch02-Data-Variables-StdIO.ipynb",
    "Ch03-1-Functions-Built-in.ipynb": "Ch09-1-Functions-Built-in.ipynb",
    "Ch03-2-Functions-Library.ipynb": "Ch09-2-Functions-Library.ipynb",
    "Ch03-3-Functions-UserDefined.ipynb": "Ch09-3-Functions-UserDefined.ipynb",
    "Ch03-5-NamespaceModulesRefactoring.ipynb": "Ch09-4-NamespaceModulesRefactoring.ipynb",
    "Ch04-Conditionals.ipynb": "Ch03-Conditionals.ipynb",
    "Ch05-Iterations.ipynb": "Ch04-Iterations.ipynb",
    "Ch06-Strings.ipynb": "Ch05-Strings.ipynb",
    "Ch07-Tuples.ipynb": "Ch06-Tuples.ipynb",
    "Ch08-1-Lists.ipynb": "Ch07-Lists.ipynb",
    "Ch09-1-Dictionaries.ipynb": "Ch08-Dictionaries.ipynb",
    "Ch10-1-FileIO.ipynb": "Ch10-FileIO.ipynb",
    "Ch12-Modules-Packages.ipynb": "Ch11-Modules-Packages.ipynb",
    "Ch13-Recursion.ipynb": "Ch12-Recursion.ipynb",
    "Ch14-OOP.ipynb": "Ch13-OOP.ipynb",
    "Ch16-Exceptions.ipynb": "Ch15-Exceptions.ipynb",      
    "Ch18-Inheritance.ipynb": "Ch14-Inheritance.ipynb"    
}

for old_name, new_name in rename_mapping.items():
    old_path = os.path.join(source_folder, old_name)
    new_path = os.path.join(source_folder, new_name)
    
    if os.path.exists(old_path):
        if old_path != new_path:
            if os.path.exists(new_path):
                print(f"Skipped (destination exists): {new_name}")
                continue
        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} -> {new_name}")
    else:
        print(f"File not found: {old_path}")

print('\nDone!')