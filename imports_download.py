import os

# Installe tous les modules requis pour le programme 
def imports_download():
    os.system('python -m pip install -r requirements.txt')

imports_download()