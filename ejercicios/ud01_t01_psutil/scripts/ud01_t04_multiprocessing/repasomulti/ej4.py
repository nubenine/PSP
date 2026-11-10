import multiprocessing
def enviarTexto(conn, msg):
    conn.send(msg)
    print("Se ha enviado el mensaje: {}".format(msg))
    conn.close()

def recibirTexto(conn):
    msg = conn.recv()
    print("Se ha recibido el mensaje: {}".format(msg.upper()))

if __name__ == '__main__':
    cadena = "aaaay"

    inicio, final = multiprocessing.Pipe()

    p1 = multiprocessing.Process(target=enviarTexto, args=(inicio, cadena))
    p2 = multiprocessing.Process(target=recibirTexto, args=(final, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()