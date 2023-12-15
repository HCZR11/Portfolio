import os

# Afișează valoarea variabilei de mediu PATH
print(os.environ.get('PATH'))

# Adaugă un director în variabila de mediu PATH
new_path = "/opt/render/project/poetry/bin"
os.environ['PATH'] += os.pathsep + new_path
