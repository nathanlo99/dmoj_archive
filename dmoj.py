#!/usr/bin/env python3
import requests    # The base module for GET and POST requests
import getpass     # Gets the password securely
import base64      # To 'encode' the DMOJ credentials
import os          # To inspect the file system
import os.path     # For 'isfile' and 'join' methods

# The extensions for each source langauge, used when extracting the source into a file
# INCOMPLETE
extensions = {
    "PYPY3": "py",
    "PYPY": "py",
    "PY3": "py",
    "PY2": "py",
    "C": "c",
    "CLANG": "c",
    "CLANGX": "cpp",
    "CPP03": "cpp",
    "CPP11": "cpp",
    "CPP14": "cpp",
    "BF": "bf",
    "NASM": "asm",
    "TUR": "t",
    "TEXT": "txt",
}


def try_login(username, password, quiet=False):
    if not quiet:
        print("Attempting login...")
    session = requests.Session()
    # Fetches the csrftoken from dmoj.ca
    session.get("https://dmoj.ca")
    if "csrftoken" not in session.cookies:
        raise Exception("Login failed: Could not fetch csrf token")
    payload = {
        "username": username,
        "password": password,
        "csrfmiddlewaretoken": session.cookies["csrftoken"],
    }
    session.headers.update({"Referer": "https://dmoj.ca/"})
    # Logs in with the session
    session.post("https://dmoj.ca/accounts/login/?next=/", data=payload)
    response = session.get("https://dmoj.ca/edit/profile/")
    # If the HTML returned contains the word "login", DMOJ probably redirected us to the login page
    # Therefore, login was unsucessful
    return (session, response.text.find("login") == -1)


def login(quiet=False):
    # Get credentials, either from cache or from user
    if os.path.isfile(".dmoj_creds"):
        with open(".dmoj_creds", "r") as f:
            username, password = base64.b64decode(
                f.readline().encode("utf-8")).decode("utf-8").split("å")
    else:
        username = input(" -> Username: ")
        password = getpass.getpass(" -> Password: ")

    session, login_successful = try_login(username, password, quiet=quiet)
    while not login_successful:
        print("Login unsuccessful... ")
        username = input(" -> Username: ")
        password = getpass.getpass(" -> Password: ")
        session, login_successful = login(username, password)

    if not quiet:
        print("Login successful!")

    with open(".dmoj_creds", "w") as f:
        f.write(base64.b64encode(bytes(username + "å" + password, "utf-8")).decode("utf-8"))

    return username, session


def extract_src(session, file_name, submission_num):
    """
    Fetchs the source from submission #(submission_num) and dumps it into file (file_name)
    """
    # Gets the HTML page for the submission page
    response = session.get("https://dmoj.ca/src/" + submission_num + "/raw")
    with open(file_name, "w") as f:
        f.write(response.text)

def get_files(home):
    # raw_name("source_file_name.extension") => "source_file_name"
    raw_name = lambda extended: ".".join(extended.split(".")[:-1])

    files, raw_names = [], []
    if os.path.isdir(home):
        # FIXME Apparently crashes on Windows because of '.' and '..'
        for f in os.listdir(home):
            if os.path.isfile(os.path.join(home, f)):
                files.append(f)
                raw_names.append(raw_name(f))
    else:
        os.mkdir(home)
    return files, raw_names

def main():

    print()
    print("Nathan Lo's DMOJ working directory manager")
    print("==========================================")
    print()

    # Gets the raw file_names of all the files in 'done' and 'working' directories
    done_files, done = get_files("done")
    working_files, working = get_files("working")

    username, session = login()

    # Gets all submissions by the user
    subs = requests.get("https://dmoj.ca/api/user/submissions/" + username).json()
    sub_info = {}
    submission_nums = {}

    # Gets the fastest AC submission with the most points and notes the
    # submission number and source language
    for submission_num, data in subs.items():
        if data["result"] != "AC":
            continue
        info = {
            "num": submission_num,
            "lang": data["language"],
            "time": data["time"],
            "points": data["points"],
        }
        if data["problem"] not in sub_info:
            sub_info[data["problem"]] = info
            submission_nums[data["problem"]] = submission_num
        else:
            current_info = sub_info[data["problem"]]
            if (data["points"] > current_info["points"] or
                    (data["points"] == current_info["points"] and data["time"] < current_info["time"])):
                sub_info[data["problem"]] = info
                submission_nums[data["problem"]] = submission_num

    # If something is in 'done' but not AC'ed, move those files to 'working'
    print()
    print("The following problems were marked done while not AC'ed on DMOJ:")
    print("================================================================")
    c = 0
    for number, done_problem in enumerate(done):
        if done_problem not in submission_nums:
            print("\t{}".format(done_problem))
            os.remove(os.path.join("done", done_files[number]))
            c += 1
    print(" -> {} files removed from 'done/'".format(c))
    print()

    # If something is marked 'in progress' when actually AC'ed, move to 'done'
    print("The following problems were marked in progress while AC'ed on DMOJ:")
    print("===================================================================")
    c = 0
    for number, working_problem in enumerate(working):
        if working_problem in submission_nums:
            print("\t{}".format(working_problem))
            os.remove(os.path.join("working", working_files[number]))
            c += 1
    print(" -> {} files removed from 'working/'".format(c))
    print()

    # Extracts AC problem sources that were not found in 'done'
    print("The following problems were AC'ed but the source was not found locally:")
    print("=======================================================================")
    c = 0
    for ac_problem in submission_nums:
        if ac_problem not in done:
            lang = sub_info[ac_problem]["lang"]
            extension = extensions.get(lang, lang.lower())
            file_name = os.path.join("done", ac_problem + "." + extension)
            submission_num = submission_nums[ac_problem]
            extract_src(session, file_name, submission_nums[ac_problem])
            print(" -> Wrote {}".format(file_name))
            c += 1
    print(" -> {} files written".format(c))
    print()

    # Closes the session
    session.close()

if __name__ == "__main__":
    main()
