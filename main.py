import socket
import code
def server():
    # 1: bind & listen
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('', 8000))
    server.listen(100)
    while 1:
        # 2: accept new connection
        con, _ = server.accept()
        # 3: read request
        req = con.recv(32*1024)
        print(req.decode("utf-8"))
        #code.interact(local=locals())
        # 4: process request and make response
        # 5: send response

        res = """HTTP/1.1 200 OK\r
Content-Type: text/plain\r
Content-Length: 5\r
\r
hello"""

        con.sendall(res.encode('utf-8'))
        # 6: close connection
        con.close()

if __name__ == '__main__':
    server()
