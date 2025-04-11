import http.server
import ssl
from cryptography.hazmat.primitives.serialization import pkcs12, Encoding, PrivateFormat, NoEncryption
from cryptography.hazmat.backends import default_backend

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/info":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write("Сологуб Анастасія КП-21".encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write("Not Found".encode("utf-8"))

# Функція для розпаковки .p12 файлу
def load_p12_cert(p12_file, password):
    with open(p12_file, 'rb') as f:
        p12_data = f.read()

    private_key, certificate, additional_certificates = pkcs12.load_key_and_certificates(p12_data, password.encode(), backend=default_backend())
    
    return certificate, private_key

def run_https_server():
    server_address = ('127.0.0.1', 5000)
    httpd = http.server.HTTPServer(server_address, MyHandler)

    # Створюємо TLSv1.2
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

    cert, key = load_p12_cert("D:/mkcert/localhost.p12", "changeit")
    cert_pem = cert.public_bytes(encoding=Encoding.PEM)
    key_pem = key.private_bytes(encoding=Encoding.PEM,
                                format=PrivateFormat.PKCS8,
                                encryption_algorithm=NoEncryption())

    with open("cert.pem", "wb") as cert_file:
        cert_file.write(cert_pem)

    with open("key.pem", "wb") as key_file:
        key_file.write(key_pem)

    context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

    print("HTTPS сервер запущено з TLSv1.2 на https://127.0.0.1:5000/info ...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_https_server()
