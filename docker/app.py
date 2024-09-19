import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

# Get the container ID or hostname where the container is running
container_id = os.uname()[1]

# Define a request handler that will serve our custom message
class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Send a 200 OK response
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Write the message to the browser
        self.wfile.write(bytes(f"Hi, I am running in container ID: {container_id}", "utf8"))

# Define the server to run on port 8080
def run(server_class=HTTPServer, handler_class=MyHandler):
    server_address = ('', 80)  # Listen on all available interfaces, port 8080
    httpd = server_class(server_address, handler_class)
    print(f"Server started on port 80 in container {container_id}")
    httpd.serve_forever()

# Run the web server
if __name__ == "__main__":
    run()
