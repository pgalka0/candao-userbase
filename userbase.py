import random
import threading

import requests



def load_addresses():
    with open('addresses.txt', 'r') as f:
        content = f.read()
        addresses = content.split(",")
        return addresses

def load_roles():
    with open('roles.txt', 'r') as f:
        content = f.read()
        roles = content.split("\n")
        roles = [r[1:len(r) - 1] for r in roles]
        return roles

def load_posts():
    with open('posts.txt', 'r') as f:
        content = f.read()
        posts = content.split("\n")
        posts = [r[3:len(r)] for r in posts]
        return posts
def add_post(author, roles, interests, text):
    req = {
        "author": author,
        "images": [],
        "sharing": "",
        "target": {
            "roles": roles,
            "interests": interests
        },
        "text": text,
        "thread": ""
    }

    post_response = requests.post("http://localhost/v1/post/upload", json=req)
    return post_response

def get_random(f, t):
    return random.randint(f,t)

def generate_post(addresses, roles, content):
    addr = addresses[get_random(0, len(addresses) -1)]
    post = posts[get_random(0, len(content) -1)]
    roles_chance = get_random(0, 5)
    choosen_roles = []
    if(roles_chance >= 3):
        roles_amount = get_random(0, 5)
        for x in range(roles_amount):
            choosen_roles.append(roles[get_random(0, len(roles) - 1)])

    res = add_post(addr, choosen_roles, [], post)
    print(res.status_code)

def generate_posts(addresses, roles, content, amount = 20, ):
    for x in range(0, amount):
        # threading.Thread(target=lambda: generate_post(addresses, roles, f"Example post: {x}")).start()
        generate_post(addresses, roles, content)
if __name__ == "__main__":
    addr = load_addresses()
    roles = load_roles()
    posts = load_posts()
    generate_posts(addr, roles, posts, 500)
    # print(posts)
    # add_post("0x7c2477a1e2af8e4b28b972405db4d81fb48d0a7e", [], [], "My First Post")
