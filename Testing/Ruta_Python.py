
# Librerías para modificar la ruta
import sys
from pathlib import Path

# Insertar el directorio principal del archivo a testear
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "Python"))