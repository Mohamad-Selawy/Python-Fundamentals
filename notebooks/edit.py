import os

source_folder = r'C:\Users\moham\OneDrive\Documents\GitHub\Python-Fundamentals\notebooks'
output_folder = r'C:\Users\moham\OneDrive\Documents\GitHub\Python-Fundamentals\notebooks'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

print('Source directory:', source_folder)
print('Output directory:', output_folder)

for file in os.listdir(source_folder):

    if file.endswith('.ipynb'):

        source_path = os.path.join(source_folder, file)
        output_path = os.path.join(output_folder, file)

        # Read the notebook
        with open(source_path, 'r', encoding='utf-8') as f:
            notebook = f.read()

        # Replace the old repository path
        updated_notebook = notebook.replace(
            'rambasnet/Python-Fundamentals',
            'Mohamad-Selawy/Python-Fundamentals'
        )
        updated_notebook = updated_notebook.replace(
            'rambasnet/FDSPython-Notebooks',
            'Mohamad-Selawy/Python-Fundamentals'
        )

        # Save the updated notebook in the new folder
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(updated_notebook)

        print('Processed:', file)

print('\nDone!')