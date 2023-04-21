import requests

target_url = input('[+] Ingresa la URL target >> ')
file_name = input('[+] Ingresa el archivo que contenga directorios >> ')

def request(url):
	try:
		return requests.get("http://" + url)
	except requests.exceptions.ConnectionError:
		pass

file = open(file_name, 'r')
for line in file:
	directory = line.strip()
	full_url = target_url + '/' + directory
	response = request(full_url)
	if response:
		print('[¡] Directorio descubierto: ' + full_url)

print('[!!] No se encontraron directorios, actualiza el archivo!')
