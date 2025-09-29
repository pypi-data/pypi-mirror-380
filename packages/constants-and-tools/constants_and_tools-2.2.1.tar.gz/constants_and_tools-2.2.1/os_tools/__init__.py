import glob
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from singleton_tools import SingletonMeta
import os
from typing import Dict, List, Optional
from pathlib import Path


class OsTools(metaclass=SingletonMeta):
    def __init__(self):
        pass

    @staticmethod
    def execute_process_pool(methods: Dict) -> Dict:
        """
        Metodo que ejecuta el poolexecutor y retorna el diccionario con las respuestas
        Adecuado para tareas que consuman procesamiento CPU
        :param methods: EXAMPLE:
            - Con args: {'nombre_metodo_1': (mi_metodo, (param1,)), 'nombre_metodo_2': (mi_metodo2, (param1, param2,))}
            - Sin args: {'nombre_metodo_1': mi_metodo, 'nombre_metodo_2': mi_metodo2}
            - Mixto: {'nombre_metodo_1': mi_metodo, 'nombre_metodo_2': (mi_metodo2, (param1,))}
        NOTA: Los parámetros deben ir en formato tupla (param1, ). En caso de poner (param1) puede dar error
        :return: Diccionario con los resultados
        """

        # --------------------------------------------------------------------------
        # -- 1: Creo el diccionario que almacenará los resultados y arranco el Pool
        # --------------------------------------------------------------------------

        # ---- 1.1: Diccionario de resultados
        results: dict = {}

        # ---- 1.2: Entramos al Pool
        with ProcessPoolExecutor() as executor:

            # ------ 1.2.1: Diccionario que va a almacenar los futuros
            futures = {}

            # ------ 1.2.2: Iteramos por cada metodo del diccionario
            for name, value in methods.items():

                # -------- Detectar si value es una tupla con (func, args) o solo una función
                if isinstance(value, tuple) and len(value) == 2:
                    func, args = value
                    futures[name] = executor.submit(func, *args)
                else:
                    # -------- Es solo una función sin argumentos
                    func = value
                    futures[name] = executor.submit(func)

            for name, future in futures.items():
                try:
                    results[name] = future.result()  # Obtiene el resultado de cada proceso
                except Exception as e:
                    print(f"Error en {name}: {e}")

        return results

    @staticmethod
    def execute_thread_pool(methods: Dict) -> Dict:
        """
        Méthod que ejecuta el ThreadPoolExecutor y retorna el diccionario con las respuestas.
        Adecuado para tareas I/O-bound (como llamadas a API o lectura/escritura de archivos),
        :param methods: EXAMPLE:
            - Con args: {'nombre_metodo_1': (mi_metodo, (param1,)), 'nombre_metodo_2': (mi_metodo2, (param1, param2,))}
            - Sin args: {'nombre_metodo_1': mi_metodo, 'nombre_metodo_2': mi_metodo2}
            - Mixto: {'nombre_metodo_1': mi_metodo, 'nombre_metodo_2': (mi_metodo2, (param1,))}
        NOTA: Los parámetros deben ir en formato tupla (param1, ). En caso de poner (param1) puede dar error
        :return: Diccionario con los resultados
        """

        # --------------------------------------------------------------------------
        # -- 1: Creo el diccionario que almacenará los resultados y arranco el Pool
        # --------------------------------------------------------------------------

        # ---- 1.1: Diccionario de resultados
        results: dict = {}

        # ---- 1.2: Entramos al Pool
        with ThreadPoolExecutor() as executor:

            # ------ 1.2.1: Diccionario que va a almacenar los futuros
            futures = {}

            # ------ 1.2.2: Iteramos por cada metodo del diccionario
            for name, value in methods.items():

                # -------- Detectar si value es una tupla con (func, args) o solo una función
                if isinstance(value, tuple) and len(value) == 2:
                    func, args = value
                    futures[name] = executor.submit(func, *args)
                else:
                    # -------- Es solo una función sin argumentos
                    func = value
                    futures[name] = executor.submit(func)

            for name, future in futures.items():
                try:
                    results[name] = future.result()  # Obtiene el resultado de cada proceso
                except Exception as e:
                    print(f"Error en {name}: {e}")

        return results

    @staticmethod
    def create_folder_if_not_exists(folder_path: str) -> None:
        """
        Metodo para crear una carpeta si no existe ya
        :param folder_path:
        :return:
        """

        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

    @staticmethod
    def get_path_files_by_extension(
            folder_path: str,
            extension: Optional[str] = None,
            substring: Optional[str] = None,
            recursive: bool = False,
            case_sensitive: bool = False
    ) -> List[str]:
        """
        Metodo genérico para obtener una lista de archivos de una carpeta según diversos criterios.

        :param folder_path: Ruta de la carpeta a buscar. EXAMPLE: 'data/input_data/extracted_files'
        :param extension: Extensión de archivo a filtrar (sin punto). EXAMPLE: 'png', 'pdf'. Si es None, busca todos.
        :param substring: Subcadena que debe contener el nombre del archivo. EXAMPLE: 'imagen', '2024'. Si es None, no filtra.
        :param recursive: Si True, busca en subcarpetas recursivamente. Default: False
        :param case_sensitive: Si True, la búsqueda distingue mayúsculas/minúsculas. Default: False
        :return: Lista de rutas de archivos que cumplen los criterios. EXAMPLE: ['img1.png', 'img2.png']
        """

        # -- 1: Construyo el patrón de búsqueda, si es recursivo, se va a buscar en las anidadas
        if recursive:
            pattern = f"{folder_path}/**/*"
        else:
            pattern = f"{folder_path}/*"

        # -- 2: Configuro la extension (si ya viene con punto lo elimino)
        if extension:
            pattern += f".{extension.replace('.', '')}"

        # -- 3: Obtengo todos los archivos que coinciden
        files = glob.glob(pattern, recursive=recursive)

        # -- 4: Filtro por substring y retorno
        if substring:
            if case_sensitive:
                files = [f for f in files if substring in Path(f).name]
            else:
                substring_lower = substring.lower()
                files = [f for f in files if substring_lower in Path(f).name.lower()]

        return files
