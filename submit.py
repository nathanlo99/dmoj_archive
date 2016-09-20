#! /usr/bin/env python3

import bs4
import sys  # for exit
import requests  # for everything HTTP
import time  # for sleeping while waiting for judging
import os  # for checking if a file exists
import shutil  # for checking terminal width
import dmoj


def pretty_print_list(n):
    # Prints a list of strings in columns
    max_length = max(map(len, n))
    term_size = shutil.get_terminal_size((0, 0))
    width = term_size.columns
    padding = 3
    num_entries_per_col = width // (max_length + padding) - 1
    col = 0
    for entry in n:
        print(("{:>" + str(max_length + padding) + "}").format(entry), end="")
        col += 1
        if col == num_entries_per_col:
            col = 0
            print()


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
    while language not in available_languages:
        print("Language '", language, "' not allowed or incorrectly spelled")
        print("Allowed languages for this problem: ")
        print()
        pretty_print_list(available_languages)
        print("\n")
        # print("\n".join("\t{}".format(language) for language in available_languages))
        language = input("Language: ")

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
        'ADA': 42,
        'AWK': 43,
        'BF': 30,
        'C': 9,
        'CBL': 39,
        'CCL': 65,
        'COFFEE': 45,
        'CLANG': 35,
        'CLANGX': 36,
        'CPP03': 2,
        'CPP11': 13,
        'CPP14': 33,
        # 'CS': ?,
        'D': 29,
        'DART': 37,
        # 'ERL': ?,
        # 'FS': ?,
        'F95': 19,
        # 'GASARM': ?,
        'GAS32': 56,
        'GAS64': 58,
        'GO': 16,
        'GROOVY': 64,
        'HASK': 15,
        # 'ICK': ?,
        'JAVA7': 7,
        'JAVA8': 25,
        'JAVA9': 61,
        'KOTLIN': 67,
        'LUA': 22,
        'MONOCS': 14,
        'MONOFS': 40,
        'MONOVB': 34,
        'NASM': 20,
        'NASM64': 62,
        'NIM': 66,
        'OBJC': 31,
        'OCAML': 23,
        # 'OCTAVE': ?,
        'PAS': 10,
        'PERL': 6,
        'PHP': 5,
        # 'PHP7': ?
        'PIKE': 68,
        'PRO': 47,
        'PYPY': 17,
        'PYPY3': 18,
        'PY2': 1,
        'PY3': 8,
        # 'R': ?,
        'RKT': 63,
        # 'RUBY18': ?,
        'RUBY21': 21,
        'RUST': 44,
        'SCALA': 52,
        'SCM': 41,
        'SED': 60,
        'SWIFT': 54,
        'TCL': 38,
        'TEXT': 51,
        'TURING': 24,
        # 'VB': ?,
        # 'VC': ?,
        'V8JS': 27
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
    response_json = response.json()
    if str(submission_num) not in response_json:
        print("[ Submission results not visible ]")
        return submission_num

    submission = response_json[str(submission_num)]

    seconds = 0
    while submission["status"] not in ["CE", "D", "AB"]:
        print("\rGrading Status:", submission["status"])
        print("   ({} seconds)".format(seconds))
        time.sleep(1)
        seconds += 1
        response = session.get(submissions_url)
        submission = response.json()[str(submission_num)]

    print("Result   : {}".format(submission["result"]))
    if submission["time"] is None:
        submission["time"] = -1.0
    print("Time     : {:.3}s".format(submission["time"]))
    print("Language : {}".format(submission["language"]))
    print("Memory   : {}".format(readable_memory(submission["memory"])))

    return submission_num


def results(session, submission_num):
    response = session.get("https://dmoj.ca/submission/" + str(submission_num))
    html = bs4.BeautifulSoup(response.text, "html.parser")
    table = html.find("table")
    if table is None:
        # This sometimes happens when submissions get CE (compilation errors)
        print("\nNo results available")
        return

    print()
    # TODO: Display all the batches
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
