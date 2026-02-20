#!/usr/bin/python3
"""Write a basic Python script to fetch posts from JSONPlaceholder
using requests.get()"""
import requests
import csv

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch all posts from JSONPlaceholder and print their titles"""
    response = requests.get(URL)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post["title"])
    else:
        print("Failed to fetch posts")


def fetch_and_save_posts():
    """Fetch all posts from JSONPlaceholder and structure the data into
    a list of dictionaries"""
    response = requests.get(URL)

    if response.status_code == 200:
        posts = response.json()

        structured_posts = []
        for post in posts:
            structured_posts.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["id", "title", "body"]
            )
            writer.writeheader()
            writer.writerows(structured_posts)

        print("Posts successfully saved to posts.csv")
    else:
        print("Failed to fetch posts")


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()