# from pyrad.client import Client
# from pyrad import dictionary
# from pyrad import packet
import subprocess
import sys

from socketIO_client import SocketIO

# def send_coa(json_obj):
#     radclient = Client(
#         server= json_obj['host'],
#         secret= json_obj['secret'],
#         dict=dictionary.Dictionary("dictionary")
#     )

# json_obj = {
#   "type": "mysql",
#   "command": "SELECT * FROM radcheck;"
# }


io = SocketIO((len(sys.argv) > 1 and sys.argv[1]) or '127.0.0.1', 8383)


# json_obj = {
#     "type": "coa",
#     "Acct-Session-ID": "abcdef01",
#     "attribute": "MikroTik-Rate-Limit",
#     "value": "5M/5M",
#     "host": "home.jemnetworks.com",
#     "port": 3799,
#     "secret": "sonarsecret"
# }

def on_coa(json):
    coa_command = f"echo Acct-Session-ID={json['Acct-Session-ID']},"
    coa_command += f"{json['attribute']}={json['value']} | radclient "
    coa_command += f"{json['host']}:{json['port']} coa {json['secret']}"
    print(coa_command)
    # response = subprocess.Popen(coa_command)
        # stream = os.popen(f"echo 'Acct-Session-ID={sessionid},{update}'  | radclient {COA_HOST}:{COA_PORT} coa {COA_SECRET}")


def on_mysql(json):
    print(json['command'])


io.on('coa', on_coa)
io.on('mysql', on_mysql)
io.emit('join coa')
io.wait()
