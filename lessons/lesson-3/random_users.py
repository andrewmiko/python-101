import json
import random
import string


def generate_random_string(length):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_random_phone():
    return "".join(random.choices(string.digits, k=10))


def generate_random_email(username):
    domains = ["example.com", "mail.com", "test.com", "demo.com"]
    return f"{username}@{random.choice(domains)}"


def generate_random_address():
    streets = ["Main St", "High St", "Elm St", "Maple St", "Oak St"]
    cities = ["Springfield", "Rivertown", "Lakeview", "Hilltop", "Fairview"]
    return f"{random.randint(1, 999)} {random.choice(streets)}, {random.choice(cities)}, USA"


def generate_random_tags():
    all_tags = ["admin", "user", "guest", "moderator", "premium", "free"]
    return random.sample(all_tags, random.randint(1, 3))


def generate_user():
    username = generate_random_string(8)
    return {
        "username": username,
        "password": generate_random_string(12),
        "email": generate_random_email(username),
        "phone": generate_random_phone(),
        "address": generate_random_address(),
        "tags": generate_random_tags(),
    }


# Generate the list of users
users = [[], []]
for _ in range(50):
    users[0].append(generate_user())
    users[1].append(generate_user())


with open("users.json", "w") as f:
    json.dump(users, f, indent=2)
