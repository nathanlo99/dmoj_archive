#! /usr/bin/env python3

# graph.py will take an arbitrary number of command-line arguments, representing users,
#   and plot their points over time in a pyplot graph.

import sys
import matplotlib.pyplot as plt
import requests


def main():
    # TODO: Clean up code and use better variable names
    users = sys.argv[1:]
    if users == []:
        print("Usage: graph.py user1 [user2] ...")
        return 0
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
            if problem_name not in best_submission or points > best_submission[problem_name][1]:
                best_submission[problem_name] = (num, points)

        total_points = 0
        data_x, data_y = [], []
        i = 1
        ppp_y = []
        for submission_number, points_earned in sorted(best_submission.values()):
            total_points += points_earned
            ppp_y.append(total_points / i)
            i += 1
            data_x.append(submission_number)
            data_y.append(total_points)
        print("Total points for '{}': {}".format(user, total_points))
        plt.plot(data_x, data_y, label=user)
        # plt.plot(data_x, ppp_y, label=user + "PPP")

    # BIG TODO:
    # Once DMOJ's API makes finding out the date a submission was submitted, I will
    # make the x-axis time instead of submission number, although they correlate roughly
    # linearly (??)

    plt.xlabel("Submission number")
    plt.ylabel("Points")
    plt.legend(loc = 2)
    print("Plotting...")
    plt.show()
    return 0

if __name__ == "__main__":
    sys.exit(main())
