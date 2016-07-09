#! /usr/local/bin/pypy3
import sys # for exit
import requests # for everything HTTP
import getpass # for getpass
import bs4 # for html parsing and searching
import time # for sleeping while waiting for judging
import base64 # for encoding passwords into client-side cache file
import os # for checking if a file exists

def login(session, read_cache):
	login_url = "https://dmoj.ca/accounts/login/"
	CHECK_URL = "https://dmoj.ca/user"

	CACHE_FILE = ".dmoj_creds"
	if not os.path.isfile(CACHE_FILE) or not read_cache:
		print("CACHE FILE NOT FOUND: CREATING...")
		with open(CACHE_FILE, "wb") as CACHE:
			USERNAME = input("USERNAME: ").strip()
			PASSWORD = getpass.getpass("PASSWORD: ").strip()
			CACHE.write(base64.b64encode(bytes(USERNAME + "å" + PASSWORD, "utf-8")).decode("utf-8"))

	else:
		with open(CACHE_FILE, "r") as CACHE:
			print("USING CACHED PASSWORD")
			USERNAME, PASSWORD = base64.b64decode(CACHE.readline().encode("utf-8")).decode("utf-8").split("å")

	# To fetch csrftoken (DMOJ requires this in order to log in)
	session.get(login_url)

	# Payload to post to server
	login_data = {
		"username": USERNAME,
		"password": PASSWORD,
		"csrfmiddlewaretoken": session.cookies["csrftoken"],
	}

	# Posts the payload
	session.post(login_url, data=login_data, headers={"Referer": login_url})

	# Gets a private page to check if login was successful.
	response = session.get(CHECK_URL)

	# If redirected to login page, login was unsuccessful.
	if (response.text.find("Login")) == -1:
		print("LOGIN SUCCESSFUL\n")
		return USERNAME
	else:
		print("LOGIN FAILED\n")
		return None

def problemExists(session, problem):
	response = session.get("https://dmoj.ca/problem/" + problem)
	return response.text.find("No such problem") != -1

def getFile(session):
	source_file = input("FILE: ").strip()
	while not os.path.isfile(source_file):
		print("FILE NOT FOUND")
		source_file = input("FILE: ").strip()

	file_name = source_file.split("/")[-1]
	problem_name = ".".join(file_name.split(".")[:-1])
	print(problem_name)
	source_text = open(source_file, "r").read()

	info_url = "https://dmoj.ca/api/problem/info/" + problem_name
	submit_url = "https://dmoj.ca/problem/" + problem_name + "/submit"
	info = session.get(info_url).json()

	language = input("LANGUAGE: ")
	available_languages = info["languages"]
	while language not in available_languages:
		language = input("LANGUAGE: ")
		print("Language '", language, "' not allowed or incorrectly spelled")

	print()
	print("############## SUBMITTED SOURCE ##############")
	print(source_text)
	print("############## SUBMITTED SOURCE ##############")
	print("\nLANGUAGE: ", language)

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
	problem_num = int(soup.find_all("input", {"id":"id_problem"})[0].get("value"))

	print("PROBLEM NAME: ", info["name"])
	print("PROBLEM#: ", problem_num)
	print("TIME LIMIT: ", info["time_limit"])

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
		'FORTRAN': 19,
		'TURING': 24,
		'NASM': 20,
		'BF': 30,
	}

	submit_payload = {
		"problem":problem_num,
		"source":source,
		"language":language_nums[language],
		"csrfmiddlewaretoken": session.cookies["csrftoken"],
	}

	response = session.post(submit_url, data=submit_payload, headers={"referer": login_url}, allow_redirects=True)
	if (response.status_code != requests.codes.ok):
		print("COULD NOT SUBMIT!")
		sys.exit(4)

	submission_num = response.url.split("/")[-1]

	if submission_num == "submit":
		print("\nSUBMISSION ERROR")
		sys.exit(5)
	print("\nSUBMITTED SUBMISSION #", submission_num, "\n")

	submissions_url = "https://dmoj.ca/api/user/submissions/" + username

	response = session.get(submissions_url)
	submission = response.json()[str(submission_num)]

	while submission["status"] not in ["CE", "D"]:
		print("\rGRADING STATUS:", submission["status"])
		time.sleep(1)
		response = session.get(submissions_url)
		submission = response.json()[str(submission_num)]

	print("RESULT: ", submission["result"])
	print("TIME: ", submission["time"])
	print("LANGUAGE: ", submission["language"])
	print("MEMORY: ", submission["memory"])

	return submission_num

def results(session, submission_num):
	response = session.get("https://dmoj.ca/submission/" + str(submission_num))
	html = bs4.BeautifulSoup(response.text, "html.parser")
	table = html.find("table")
	print()
	for entry in table.find_all("tr"):
		print(" ".join(entry.get_text().split()))

def main():
	# To preserve session cookies
	session = requests.session()

	username = login(session, True)
	while not username: username = login(session, False)

	source, language, problem = getFile(session)
	submission_num = submit(session, username, problem, source, language)
	results(session, submission_num)
	session.close()

if __name__ == "__main__":
	main()
