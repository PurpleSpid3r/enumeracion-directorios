# enumeracion-directorios

Enumerador de directorios web por diccionario, desarrollado en Python 3.
Prueba las rutas de una wordlist contra una URL base y reporta las que
devuelven un código HTTP interesante (200, 301, 403, etc.).

> ⚠️ **Uso autorizado únicamente.** Ejecuta esta herramienta solo contra
> aplicaciones de tu propiedad o para las que tengas permiso explícito.

## Requisitos

- Python 3.6 o superior
- [`requests`](https://pypi.org/project/requests/)

```bash
pip install -r requirements.txt
```

## Uso

Modo con argumentos (recomendado):

```bash
python3 enumerar_directorios.py -u http://10.0.0.1 -w wordlist.txt

# Ajustar códigos considerados "encontrado" y el timeout
python3 enumerar_directorios.py -u http://10.0.0.1 -w wordlist.txt -c 200,301,403 -t 3
```

Modo interactivo (si no pasas argumentos, los pregunta):

```bash
python3 enumerar_directorios.py
```

## Opciones

| Opción            | Descripción                                                       |
|-------------------|-------------------------------------------------------------------|
| `-u`, `--url`     | URL base (si omites el esquema, se asume `http://`)               |
| `-w`, `--wordlist`| Archivo con una ruta por línea (las líneas con `#` se ignoran)    |
| `-t`, `--timeout` | Timeout por petición en segundos (def. `5.0`)                     |
| `-c`, `--codes`   | Códigos HTTP considerados "encontrado" (def. `200,204,301,302,307,401,403`) |

Puedes usar wordlists como las de [SecLists](https://github.com/danielmiessler/SecLists)
(p. ej. `Discovery/Web-Content/common.txt`).
