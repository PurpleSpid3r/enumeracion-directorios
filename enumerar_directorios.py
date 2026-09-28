#!/usr/bin/env python3
"""Enumerador de directorios web por diccionario.

Prueba rutas de una wordlist contra una URL base y reporta las que responden
con un código HTTP "interesante" (200, 301, 403, etc.). Para aprendizaje y
pruebas autorizadas únicamente.
"""
import argparse
import sys

import requests


def enumerar(base_url, wordlist, timeout, status_ok):
    """Prueba cada ruta de `wordlist` contra `base_url`.

    Devuelve la lista de URLs cuyo código de respuesta está en `status_ok`.
    """
    base_url = base_url.rstrip("/")
    encontrados = []
    with open(wordlist, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            directorio = line.strip()
            if not directorio or directorio.startswith("#"):
                continue
            full_url = f"{base_url}/{directorio}"
            try:
                resp = requests.get(full_url, timeout=timeout, allow_redirects=False)
            except requests.exceptions.RequestException:
                # Timeout, DNS, conexión rechazada... seguimos con la siguiente.
                continue
            if resp.status_code in status_ok:
                print(f"[+] {resp.status_code}  {full_url}")
                encontrados.append(full_url)
    return encontrados


def main():
    parser = argparse.ArgumentParser(
        description="Enumerador de directorios web por diccionario.")
    parser.add_argument("-u", "--url", help="URL base, ej: http://10.0.0.1")
    parser.add_argument("-w", "--wordlist",
                        help="Archivo con rutas/directorios (uno por línea)")
    parser.add_argument("-t", "--timeout", type=float, default=5.0,
                        help="Timeout por petición en segundos (por defecto 5.0)")
    parser.add_argument("-c", "--codes", default="200,204,301,302,307,401,403",
                        help="Códigos HTTP considerados 'encontrado' (separados por coma)")
    args = parser.parse_args()

    url = args.url or input("[+] Ingresa la URL base (con o sin http): ")
    wordlist = args.wordlist or input("[+] Ingresa el archivo de diccionario: ")

    # Solo anteponemos el esquema si no lo trae ya (bug antiguo: doble http://).
    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    try:
        status_ok = {int(c) for c in args.codes.split(",") if c.strip()}
    except ValueError:
        parser.error("Los códigos HTTP deben ser números separados por coma.")

    try:
        encontrados = enumerar(url, wordlist, args.timeout, status_ok)
    except FileNotFoundError:
        parser.error(f"No se encontró la wordlist: {wordlist}")

    if not encontrados:
        print("[!] No se encontraron directorios. Prueba con otra wordlist.")
    else:
        print(f"\n[✓] {len(encontrados)} ruta(s) encontrada(s).")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Interrumpido por el usuario.")
        sys.exit(130)
