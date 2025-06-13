import subprocess
import os

def generarSolucionesSolver(instances=1):
    os.makedirs("tests/resultados_solver", exist_ok=True)

    for i in range(instances):
        command = [
            "wsl",
            "/root/proyecto/solver/BSG_CLP2",                 # Ruta absoluta del ejecutable en WSL
            "-i", str(i),
            "-f", "BR",                                       # Ajusta si tu formato no es BR
            "-t", "5",
            "--verbose2=5",
            "/root/proyecto/tests/instances/instances.txt"    # Ruta absoluta del archivo de instancias
        ]

        print(f"Ejecutando: {' '.join(command)}")
        
        result = subprocess.run(command, capture_output=True, text=True)

        output_file = f"tests/resultados_solver/output{i+1}.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result.stdout)

        if result.stderr:
            print(f"Errores:\n{result.stderr}")