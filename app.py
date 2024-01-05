from flask import Flask
import requests
from bs4 import BeautifulSoup as bs
import re
from tqdm import tqdm

res = ["(mailto.*)", "(.*?velog.*)", "(.*?instagram.*)", "(.*?linkedin.*)"]
file_path = 'github.txt'
results = {}


def open_file(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    return lines


def save_data():
    global file_path
    lines = open_file(file_path)

    for url in tqdm(lines):
        url = url.replace('\n', '')

        if len(url) == 0:
            continue

        name = url.split('/')[-2]
        page = requests.get(url)

        if page.status_code == 200:
            soup = bs(page.text, "html.parser")
            elements = soup.find_all('a')
            links = []
            for e in elements:
                for r in res:
                    m = re.search(r, e['href'])
                    if m != None:
                        links.append(m.group())

            results[name] = links
        else:
            print(f'error >> {url}')


app = Flask(__name__)


@app.route('/')
def read_txt():
    global results
    text = "<h1>신프디 3기</h1>"
    for name, links in results.items():
        text += f"<div> {name} :"
        for link in links:
            text += f"<a href={link}>{link}</a> , "
        text += "<br>"
    return text


@app.route('/user/<name>', methods=['GET'])
def show_user_profile(name):
    global results
    links = results[name]
    text = f"<h1>{name}</h1>"
    for link in links:
        text += f"<a href={link}>{link}</a><br>"
    return text


if __name__ == '__main__':
    save_data()
    app.run(host='0.0.0.0')
