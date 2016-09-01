#! /usr/bin/env python3

# graph.py will take an arbitrary number of command-line arguments, representing users,
#   and plot their points over time in a pyplot graph.

import collections
import sys
import matplotlib.pyplot as plt
import requests
import bs4

# TODO: Clean up code and use better variable names
users = sys.argv[1:]
for user in users:
    print("Crunching data for '{}'".format(user))
    reply = requests.get("https://dmoj.ca/api/user/submissions/{}".format(user))
    if reply.status_code != requests.codes["OK"]:
        print("User not found: {}, skipping".format(user))
        continue
    subs_json = reply.json()
    best_submission = {}
    for num, data in subs_json.items():
        num = int(num)
        problem_name = data["problem"]
        points = data["points"]
        if points is None or points == 0:
            continue
        if problem_name not in best_submission:
            best_submission[problem_name] = (num, points)
        elif points > best_submission[problem_name][1]:
            best_submission[problem_name] = (num, points)
    total_points = 0
    data_x = []
    data_y = []
    for submission_number, points_earned in sorted(best_submission.values()):
        total_points += points_earned
        data_x.append(submission_number)
        data_y.append(total_points)
    print("Total points for '{}': {}".format(user, total_points))
    plt.plot(data_x, data_y, label=user)

    # BIG TODO:
    # Once DMOJ's API makes finding out the date a submission was submitted, I will 
    # make the x-axis time instead of submission number, although they correlate roughly
    # linearly (??)
    
    # [ Incomplete attempt at parsing submissions page ]
    # page = 1
    # reply = requests.get("https://dmoj.ca/user/{}/submissions/{}".format(user, page))
    # html = bs4.BeautifulSoup(reply.text, "html.parser")
    # print(html.find_all("table", id="submissions-table"))

plt.xlabel("Submission number")
plt.ylabel("Points")
plt.legend(loc=2)
print("Plotting...")
plt.show()
