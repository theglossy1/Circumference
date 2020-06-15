import subprocess
import sys

from socketIO_client import SocketIO

if len(sys.argv) > 1:
    server_address = sys.argv[1]
else:
    server_address = '127.0.0.1'

print(f"Connecting to {server_address} on port 8383")
io = SocketIO(server_address, 8383)

def on_coa(json):
    coa_command = f"echo Acct-Session-ID={json['Acct-Session-ID']},"
    coa_command += f"{json['attribute']}={json['value']} | radclient "
    coa_command += f"{json['host']}:{json['port']} coa {json['secret']}"
    print(coa_command)
    response = subprocess.run(coa_command, shell=True, capture_output=True, text=True)
    print(response.returncode)
    print(response.stdout)
    print(response.stderr)


def on_mysql(json):
    """ Placeholder for now """
    print(json['command'])


io.on('coa', on_coa)
io.on('mysql', on_mysql)
io.emit('join coa')
io.wait()
