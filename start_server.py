"""
ATELIER NOIR - Local Development Server
Starts a lightweight local HTTP server and automatically opens the website in your default browser.
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 5500

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Disable caching for snappy development
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

def main():
    web_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(web_dir)
    
    server_address = ("", PORT)
    try:
        with socketserver.TCPServer(server_address, Handler) as httpd:
            url = f"http://localhost:{PORT}/"
            print("=" * 60)
            print("  ATELIER NOIR — Modern Luxury Menswear Storefront")
            print("=" * 60)
            print(f"  Serving live from: {web_dir}")
            print(f"  Website URL:       {url}")
            print("  Press Ctrl+C in this terminal window to stop the server.")
            print("=" * 60)
            
            # Open browser automatically
            try:
                webbrowser.open(url)
            except Exception:
                pass
                
            httpd.serve_forever()
    except OSError as e:
        print(f"Port {PORT} is currently occupied or unavailable: {e}")
        print("You can also simply double-click index.html directly to view the site!")

if __name__ == "__main__":
    main()
