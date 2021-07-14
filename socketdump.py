import socket

_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
_socket.connect(("192.168.1.37", 8069))
_socket.settimeout(5)


def _write_to_socket(data):
    _socket.send(data)


def _read_byte_from_socket():
    data = _socket.recv(1)
    return data[0]


while True:
    byte = _read_byte_from_socket()
    print(hex(byte))

