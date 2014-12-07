import socket
import mygpio

DEVICE_MAC = 'e8:4e:06:1c:37:e8'
SENSOR_ID_1 = '28-000005ffad2a'
sensor_value_1 = mygpio.getTemp()
sock = socket.socket()

try:
    sock.connect(('narodmon.ru', 8283))
    sock.send("#{}\n#{}#{}\n##".format(DEVICE_MAC, SENSOR_ID_1, sensor_value_1))
    data = sock.recv(1024)
    sock.close()
    print data
except socket.error, e:
    print('ERROR! Exception {}'.format(e))
