# constants_and_tools

## v2.2.1 modificaciones:
 
### Versiones de dependencias

- "openpyxl==3.1.5" --->   "openpyxl==3.1.5",
- "pandas==2.2.3"   --->   "pandas==2.3.2",
- "pyarrow==19.0.1" --->   "pyarrow==21.0.0",
- "polars==1.30.0"  --->   "polars==1.33.1",

### Modificaciones de metodos y funciones

#### os_tools

- execute_process_pool          --->  Adaptado para metodos con y sin args
- execute_thread_pool           --->  Adaptado para metodos con y sin args
- get_path_files_by_extension   --->  Agregada lógica para paraametrizar mayor cantidad de casos (ver method doc)

#### pandas_tools, polars_tools

- save_json_from_dict  --->  Codificado para utf8
- load_json_in_dict    --->  Codificado para utf8
- df_to_parquet        --->  Agregado parametro replace_if_exists