#! /usr/local/bin/pypy3
import requests
import getpass
import base64
import bs4
import os
import os.path

extensions = {
    "PYPY3": "py",
    "PYPY": "py",
    "PY3": "py",
    "PY2": "py",
    "C": "c",
    "CPP": "cpp",
    "CPP03": "cpp",
    "CPP11": "cpp",
    "CPP14": "cpp",
    "BF": "bf",
    "NASM": "asm",
    "TUR": "t",
}

session = None
username, password = None, None

def extract_src(file_name, submission_num):
    global session, username, password
    if session is None:
        session = requests.Session()
        session.get("https://dmoj.ca")
        data = {
            "username": username,
            "password": password,
            "csrfmiddlewaretoken": session.cookies["csrftoken"],
        }
        headers = {
            "Referer": "https://dmoj.ca/",
            "Upgrade-Insecure-Requests": "1",
        }
        session.headers.update(headers)
        r = session.post("https://dmoj.ca/accounts/login/?next=/", data=data)
    response = session.get("https://dmoj.ca/src/" + submission_num)
    html_parser = bs4.BeautifulSoup(response.text, "html.parser")
    code_element = html_parser.find("code")
    if code_element is None:
        code_element = html_parser.find("td", "source-code")
    if code_element is None:
        print("WARNING: No code found for submission {}, dumping HTML".format(submission_num))
        print(response.text)
        return
    raw_code = code_element.get_text()
    with open(file_name, "w") as f:
        f.write(raw_code)

def main():
    print()
    print("Nathan Lo's DMOJ working directory manager")
    print("==========================================")
    print()

    global session, username, password

    raw_name = lambda extended: ".".join(extended.split(".")[:-1])
    done = [raw_name(f) for f in os.listdir("done") if os.path.isfile(os.path.join("done", f))]
    working = [raw_name(f) for f in os.listdir("working") if os.path.isfile(os.path.join("working", f))]

    if input("Use cached creds?  ") in ["y", "Y"] and os.path.isfile(".dmoj_creds"):
        with open(".dmoj_creds", "r") as f:
            username, password = base64.b64decode(f.readline().encode("utf-8")).decode("utf-8").split("å")
    else:
        username = input("Username: ")
        password = getpass.getpass("Password: ")
        with open(".dmoj_creds", "w") as f:
            f.write(base64.b64encode(bytes(username + "å" + password, "utf-8")).decode("utf-8"))

    subs = requests.get("https://dmoj.ca/api/user/submissions/" + username).json()
    sub_info = {}
    submission_nums = {}
    for submission_num, data in subs.items():
        if data["result"] != "AC": continue
        if data["problem"] not in sub_info or data["time"] < sub_info[data["problem"]]["time"]:
            sub_info[data["problem"]] = {
                "num": submission_num,
                "lang": data["language"],
                "time": data["time"],
            }
            submission_nums[data["problem"]] = submission_num

    completed_problems = list(submission_nums.keys())

    print("The following problems were marked done while not AC'ed on DMOJ:")
    print("================================================================")
    c = 0
    for done_problem in done:
        if done_problem not in completed_problems:
            print("\t {}".format(done_problem))
            os.rename(join("done", done_problem), join("working", done_problem))
            c += 1
    print(" -> {} files moved from 'done/' to 'working/'".format(c))
    print()

    print("The following problems were marked in progress while AC'ed on DMOJ:")
    print("===================================================================")
    c = 0
    for working_problem in working:
        if working_problem in completed_problems:
            print("\t {}".format(working_problem))
            os.rename(join("working", working_problem), join("done", working_problem))
            c += 1
    print(" -> {} files moved from 'working/' to 'done/'".format(c))
    print()

    print("The following problems were AC'ed but the source was not found locally:")
    print("=======================================================================")
    for ac_problem in completed_problems:
        if ac_problem not in done:
            file_name = join("done", ac_problem) + "." + extensions[sub_info[ac_problem]["lang"]]
            submission_num = submission_nums[ac_problem]
            extract_src(file_name, submission_nums[ac_problem])
            print(" -> Wrote {}".format(file_name))

    if session is not None:
        session.close()

if __name__ == "__main__":
    main()
