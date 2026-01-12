"""
Part 1: Basic GET Request
=========================
Difficulty: Beginner

Learn: How to make a simple GET request and view the response.

We'll use JSONPlaceholder - a free fake API for testing.
"""

import requests

# Step 1: Define the API URL
url1 = "https://jsonplaceholder.typicode.com/posts/1"

# Step 2: Make a GET request
response1 = requests.get(url1)

# Step 3: Print the response
print("=== Basic API Request 1===\n")
print(f"URL: {url1}")
print(f"Status Code: {response1.status_code}")
print(f"\nResponse Data:")
print(response1.json())


# --- EXERCISES ---
# Exercise 1: Change the URL to fetch post number 5
#             Hint: Change /posts/1 to /posts/5
url2 = "https://jsonplaceholder.typicode.com/posts/5"
response2 = requests.get(url2)
print("\n=== Basic API Request 2===\n")
print(f"URL: {url2}")
print(f"Status Code: {response2.status_code}")
print(f"\nResponse Data:")
print(response2.json())


# Exercise 2: Fetch a list of all users
#             URL: https://jsonplaceholder.typicode.com/users
url3 = "https://jsonplaceholder.typicode.com/users"
response3 = requests.get(url3)
print("\n=== Basic API Request 3===\n")
print(f"URL: {url3}")
print(f"Status Code: {response3.status_code}")
print(f"\nResponse Data:")
print(response3.json())

# Exercise 3: What happens if you fetch a post that doesn't exist?
#             Try: https://jsonplaceholder.typicode.com/posts/999
url4 = "https://jsonplaceholder.typicode.com/999"
response4 = requests.get(url4)
print("\n=== Basic API Request 4===\n")
print(f"URL: {url4}")
print(f"Status Code: {response4.status_code}")
print(f"\nResponse Data:")
print(response4.json())