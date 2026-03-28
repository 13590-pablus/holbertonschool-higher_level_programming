#!/usr/bin/python3
"""
http.server kullanarak basit bir API oluşturma modülü.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """HTTP isteklerini yöneten özel işleyici sınıfı."""

    def do_GET(self):
        """GET isteklerini yönlendirir ve yanıtlar."""
        
        # 1. Ana Sayfa: /
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # 2. Veri Uç Noktası: /data
        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            sample_data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(sample_data).encode("utf-8"))

        # 3. Durum Uç Noktası: /status
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # 4. Bilgi Uç Noktası: /info
        elif self.path == '/info':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info_data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info_data).encode("utf-8"))

        # 5. Hata Yönetimi: Tanımlanmayan yollar için 404
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run_server():
    """Sunucuyu 8000 portunda başlatır."""
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print("Sunucu 8000 portunda çalışıyor... Durdurmak için Ctrl+C'ye basın.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nSunucu kapatılıyor...")
        httpd.server_close()


if __name__ == "__main__":
    run_server()
