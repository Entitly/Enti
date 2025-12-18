import speedtest
import datetime

print('='*40)
print("       BIENVENIDO AL SPEEDTEST        ")
print('='*40)


sp = speedtest.Speedtest()
print('Encontrando el mejor servidor para ti...')
sp.get_best_server() 

info_cliente = sp.results.client 
proveedor = info_cliente['isp']
ip = info_cliente['ip']

print(f'Proveedor: {proveedor}')
print(f'IP: {ip}')
print('-'*40)

try:
    with open("speed_test.txt", "r") as f:
        intentos_previos = len(f.readlines())
except FileNotFoundError:
    intentos_previos = 0

repes = 1 
for rep in range(repes):
    tries = intentos_previos + rep + 1 
    print(f'Ejecutando prueba N°: {tries}...')

    try: 
        download_speed = sp.download() / 1_000_000 
        upload_speed = sp.upload() / 1_000_000
        ping = sp.results.ping
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("speed_test.txt", "a") as f:
            linea = f'Intento N° {tries} - {fecha_actual} - Descarga: {download_speed:.2f} Mbps | Subida: {upload_speed:.2f} Mbps | Ping: {ping} ms\n'
            f.write(linea)
        
        print(f'Numero de intento: {tries}, Speed Test realizado y documentado con éxito!')

    except Exception as error:
        print(f'Error en el intento {tries}: {error}')

print('='*40)