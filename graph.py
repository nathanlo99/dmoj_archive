#! /usr/bin/env python3

# graph.py will take an arbitrary number of command-line arguments, representing users,
#   and plot their points over time in a pyplot graph.

import collections
import sys
import matplotlib.pyplot as plt
import requests
import bs4
import json

# WARNING: SKETCHY AND INCOMPLETE
def get_submission_dates(read_file=None, write_file=None):
    f = None
    date_mapping = {}
    if read_file is not None:
        f = open(read_file, "r")
        data = json.loads(f.read())
        date_mapping.update(data)
        f.close()
    print(date_mapping) 
    page = 1
    done = False
    data_gap = 100 # Gap between submission numbers in the mapping
    # (for example, if this is 100, we will only store submissions
    # which are multiples of 100

    while not done:
        reply = requests.get("https://dmoj.ca/submissions/{}".format(page))
        if reply.status_code != 200:
            break
        html_parser = bs4.BeautifulSoup(reply.text, "html.parser")
        submissions_table = html_parser.find_all("table", id="submissions-table")
        submission_nums = []
        unix_times = []
        submission_nums = html_parser.find_all("tr", {"id": True})
        unix_times = html_parser.find_all("span", {"data-unix": True})
        for submission_num, unix_time in zip(submission_nums, unix_times):
            submission_num = submission_num["id"]
            unix_time = unix_time["data-unix"]
            if int(submission_num) % data_gap == 0:
                if submission_num in date_mapping:
                    done = True
                    break
                date_mapping[submission_num] = unix_time
        print("Finished parsing page {}".format(page))
        page += 1

    if write_file is not None:
        f = open(write_file, "w")
        f.write(json.dumps(date_mapping))
        f.close()
    
        

def main():
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

    plt.xlabel("Submission number")
    plt.ylabel("Points")
    plt.legend(loc=2)
    print("Plotting...")
    plt.show()

if __name__ == "__main__":
    main()
    # get_submission_dates(None, "cache.txt")
