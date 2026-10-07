from http.server import HTTPServer, BaseHTTPRequestHandler


class CallbackHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        print("Requisição recebida!")
        print("Caminho:", self.path)

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        self.wfile.write(
            b"<h1>Autorizacao recebida!</h1>"
            b"<p>O Mercado Livre conseguiu chegar ate o nosso programa.</p>"
        )


servidor = HTTPServer(("localhost", 8000), CallbackHandler)

print("Servidor iniciado!")
print("Aguardando callback em http://localhost:8000")

servidor.serve_forever();from http.server import HTTPServer, BaseHTTPRequestHandler


class CallbackHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        print("Requisição recebida!")
        print("Caminho:", self.path)

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        self.wfile.write(
            b"<h1>Autorizacao recebida!</h1>"
            b"<p>O Mercado Livre conseguiu chegar ate o nosso programa.</p>"
        )


servidor = HTTPServer(("localhost", 8000), CallbackHandler)

print("Servidor iniciado!")
print("Aguardando callback em http://localhost:8000")

servidor.serve_forever()