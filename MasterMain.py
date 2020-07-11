import subprocess


# Iterable con las rutas de los scripts
scripts_paths = ("main.py", "main.py") 
	
# Creamos cada proceso    
ps = [subprocess.Popen(["python", script]) for script in scripts_paths]
exit_codes = [p.wait() for p in ps]


if not any(exit_codes):
    print("Todos los procesos terminaroin con éxito")
else:
    print("Algunos procesos terminaron de forma inesperada.")