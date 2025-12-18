import speedtest
import datetime

print("       BIENVENIDO A UN SPEEDTEST        ")

#Recolecatmos información mediante speedtest y secure
sp = speedtest.Speedtest(secure=True)
print('Encontrando el mejor servidor para ti...')
sp.get_best_server() 

#Agregamos la información del usuario que la use como: proveedo e ip
info_cliente = sp.results.client 
proveedor = info_cliente['isp']
ip = info_cliente['ip']

print(f'Proveedor: {proveedor}')
print(f'IP: {ip}')
print('-'*40)

#Buscamos si ya se hizo alguna prueba, sino empieza con contador 0
try:
    with open("speed_test.txt", "r") as f:
        intentos_previos = len(f.readlines())
except FileNotFoundError:
    intentos_previos = 0

repes = 1 
for rep in range(repes):
    tries = intentos_previos + rep + 1 
    print(f'Ejecutando prueba N°: {tries}...')
    
#Calculamos la vecocidad diviendola para un millon
    try: 
        download_speed = sp.download() / 1_000_000 
        upload_speed = sp.upload() / 1_000_000
        ping = sp.results.ping
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#Imprimimos la infomracion obtenida, dentro de un documento txt generado automaticamente
        with open("speed_test.txt", "a") as f:
            linea = f'Intento N° {tries} - {fecha_actual} - Descarga: {download_speed:.2f} Mbps | Subida: {upload_speed:.2f} Mbps | Ping: {ping} ms\n'
            f.write(linea)
        
        print(f'Numero de intento: {tries}, Speed Test realizado y documentado con éxito!')

    except Exception as error:
        print(f'Error en el intento {tries}: {error}')
