import psutil

if "main.py" in (p.name() for p in psutil.process_iter()):
    print("program is running")
else:
    print("not running")
# Popen(["python3", "/Users/joaoalves/Projetos/Papa-leguas/main.py"])
