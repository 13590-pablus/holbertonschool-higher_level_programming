#!/usr/bin/python3
"""
API'den veri çekme ve işleme modülü.
"""
import requests
import csv


def fetch_and_print_posts():
    """Tüm gönderileri çeker ve başlıklarını yazdırır."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """Gönderileri çeker ve posts.csv dosyasına kaydeder."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        
        # Sadece id, title ve body alanlarını içeren bir liste oluşturuyoruz
        structured_data = [
            {'id': p['id'], 'title': p['title'], 'body': p['body']}
            for p in posts
        ]

        # CSV dosyasına yazma işlemi
        with open('posts.csv', 'w', encoding='utf-8', newline='') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(structured_data)
