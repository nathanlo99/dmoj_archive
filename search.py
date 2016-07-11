
import requests

from dmoj import login


def main():
    username, session = login(quiet=True)
    # Gets all submissions by the user
    subs = session.get("https://dmoj.ca/api/user/submissions/" + username).json()

    ac_subs = set(data["problem"]
                  for submission_num, data in subs.items() if data["result"] == "AC")

    problem_list = session.get("https://dmoj.ca/api/problem/list").json()
    unsolved = []
    for problem, info in problem_list.items():
        if problem not in ac_subs:
            unsolved.append((info["points"], problem))
    unsolved.sort()
    print("\n".join("{:2}p -> {}".format(int(p[0]), p[1]) for p in unsolved[:10]))

    session.close()

if __name__ == "__main__":
    main()
