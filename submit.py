#! /usr/local/bin/pypy3

import bs4
import sys  # for exit
import requests  # for everything HTTP
import time  # for sleeping while waiting for judging
import os  # for checking if a file exists
import dmoj


def readable_memory(kbs):
    if kbs is None:
        return "N/A"
    if kbs > 1024 * 1024:
        return "{:.4} GB".format(kbs / (1024. * 1024.))
    if kbs > 1024:
        return "{:.4} MB".format(kbs / 1024.)
    return "{:.4} KB".format(kbs)


def getFile(session):
    source_file = input("File: ").strip() if len(sys.argv) < 2 else sys.argv[1]
    while not os.path.isfile(source_file):
        print("File not found: {}".format(source_file))
        sys.exit(1)

    # done/aplusb.asm => aplusb
    problem_name = ".".join(source_file.split("/")[-1].split(".")[:-1])
    source_text = open(source_file, "r").read()

    print("Submitting: {}".format(source_file))

    info_url = "https://dmoj.ca/api/problem/info/" + problem_name
    submit_url = "https://dmoj.ca/problem/" + problem_name + "/submit"
    info = session.get(info_url).json()

    language = sys.argv[2] if len(sys.argv) >= 3 else input("Language: ")
    available_languages = info["languages"]
    if language not in available_languages:
        print("Language '", language, "' not allowed or incorrectly spelled")
        print("\n".join("\t{}".format(language) for language in available_languages))
        sys.exit(1)

    print()
    print("############## Submitted source ##############")
    print(source_text)
    print("############## Submitted source ##############")
    print("\nLanguage: ", language)

    return source_text, language, problem_name


def submit(session, username, problem, source, language):
    # There is a line in every /submit file in the form:
    # <input id="id_problem" name="problem" type="hidden" value="$NUM" />
    # where $NUM is the problem number needed to post when submitting.
    info_url = "https://dmoj.ca/api/problem/info/" + problem
    submit_url = "https://dmoj.ca/problem/" + problem + "/submit"
    login_url = "https://dmoj.ca/accounts/login/?next="

    info = session.get(info_url).json()

    response = session.get(submit_url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    problem_num = int(soup.find_all("input", {"id": "id_problem"})[0].get("value"))

    print("Problem name: ", info["name"])
    print("Problem#: ", problem_num)
    print("Time limit: ", info["time_limit"])

    # Only picked commonly used languages
    # TODO: Extract this from /submit source <select> tag.
    language_nums = {
        'PYPY2': 17,
        'PYPY3': 18,
        'PY2': 1,
        'PY3': 8,
        'C': 9,
        'CLANG': 35,
        'CPP0X': 3,
        'CPP11': 13,
        'CPP14': 33,
        'CPP': 2,
        'CLANGX': 36,
        'JAVA': 7,
        'JAVA8': 25,
        'PAS': 10,
        'TEXT': 51,
        'FORTRAN': 19,
        'TURING': 24,
        'NASM': 20,
        'BF': 30,
    }

    submit_payload = {
        "problem": problem_num,
        "source": source,
        "language": language_nums[language],
        "csrfmiddlewaretoken": session.cookies["csrftoken"],
    }

    response = session.post(submit_url, data=submit_payload, headers={"referer": login_url})
    if (response.status_code != requests.codes.ok):
        print("Could not submit, got an error code while accessing the submit page")
        sys.exit(4)

    submission_num = response.url.split("/")[-1]

    if submission_num == "submit":
        print("\nCould not submit: Unknown error")
        sys.exit(5)
    print("\nSubmission succeeded #", submission_num, "\n")

    submissions_url = "https://dmoj.ca/api/user/submissions/" + username

    response = session.get(submissions_url)
    submission = response.json()[str(submission_num)]

    while submission["status"] not in ["CE", "D", "AB"]:
        print("\rGrading Status:", submission["status"])
        time.sleep(1)
        response = session.get(submissions_url)
        submission = response.json()[str(submission_num)]

    print("Result   : {}".format(submission["result"]))
    print("Time     : {:.3}s".format(submission["time"]))
    print("Language : {}".format(submission["language"]))
    print("Memory   : {}".format(readable_memory(submission["memory"])))

    return submission_num


def results(session, submission_num):
    response = session.get("https://dmoj.ca/submission/" + str(submission_num))
    html = bs4.BeautifulSoup(response.text, "html.parser")
    table = html.find("table")
    print()
    for entry in table.find_all("tr"):
        print(" ".join(entry.get_text().split()))


def main():
    username, session = dmoj.login()
    source, language, problem = getFile(session)
    submission_num = submit(session, username, problem, source, language)
    results(session, submission_num)
    session.close()

if __name__ == "__main__":
    main()
