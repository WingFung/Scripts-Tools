import socket
import sys

host = None
port = None
if len(sys.argv) == 2:
    user_input = sys.argv[1]
elif len(sys.argv) > 2:
    user_input = sys.argv[1] + ':' + sys.argv[2]
else:
    user_input = input('Please input the host and port for connection test:\n')
user_input = user_input.strip().replace(' ', ':')

if ':' in user_input:
    input_list = user_input.split(':')
    host = input_list[0]
    port = input_list[-1]
else:
    (host, port) = (user_input, '80')
    
skt = socket.socket()
print('Connecting to ' + host + ':' + port)
try:
    skt.connect((host, int(port)))
    print('Connected')
except:
    print('Connection failed')
finally:
    if skt is not None:
        skt.close();

pause = input('\nPress any key to exit...\n')
