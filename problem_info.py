#!/usr/bin/env python3
# Gets the problem info from the problem page and displays the raw
# text to the screen

import requests
import bs4
import sys

def main():
    problem_name = sys.argv[1] if len(sys.argv) >= 2 else input("Problem: ")
    response = requests.get("https://dmoj.ca/problem/" + problem_name)

    while response.text.find("No such problem") != -1:
        print("Problem not found: {}".format(problem_name))
        problem_name = input("Problem: ")
        response = requests.get("https://dmoj.ca/problem/" + problem_name)

    html_parser = bs4.BeautifulSoup(response.text, "html.parser")

    print(html_parser.find("title").get_text())
    print(html_parser.find("div", "content-description screen").get_text())

if __name__ == "__main__":
    main()
