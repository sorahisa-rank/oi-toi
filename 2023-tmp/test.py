import json

problem_names = ["house", "storm", "game", "molecule", "road"]
problem_subtasks = [3, 6, 4, 4, 4]

###### read scoreboard ######

with open("meow.txt", 'r') as f_scoreboard:
    id_list = [x.split() for x in f_scoreboard.readlines()]
    id_dict = {x[1] : {"school": x[2], "score": [x[3], x[4], x[5], x[6], x[7]], "total": x[8]} for x in id_list}

id_dict["T23164"]["score"][3] = "21"
id_dict["T23164"]["total"]    = "261"
id_dict = dict(sorted(id_dict.items()))
# print(id_dict)

###### add ranking/users/index.json ######

users = {}
for id in id_dict:
    users[id] = {
        "f_name": id,
        "l_name": id_dict[id]["school"],
        "team": None
    }

with open("ranking/users/index.json", 'w') as f_users:
    json.dump(users, f_users, indent = 4)

###### add ranking/submissions/index.json ######

submissions = {}
submission_tok = 0
for id in id_dict:
    for i in range(5):
        submissions[submission_tok] = {
            "user": id,
            "task": problem_names[i],
            "time": 1677996000 + submission_tok
        }
        submission_tok += 1

with open("ranking/submissions/index.json", 'w') as f_submissions:
    json.dump(submissions, f_submissions, indent = 4)

###### add ranking/subchanges/index.json ######

subchanges = {}
submission_tok = 0
for id in id_dict:
    for i in range(5):
        subchanges[submission_tok] = {
            "submission": str(submission_tok),
            "time": 1677996000 + submission_tok,
            "score": float(id_dict[id]["score"][i]),
            "extra": ["0"] * problem_subtasks[i]
        }
        submission_tok += 1

with open("ranking/subchanges/index.json", 'w') as f_subchanges:
    json.dump(subchanges, f_subchanges, indent = 4)

###### add ranking/sublist/* ######

submission_tok = 0
for id in id_dict:
    sublist = []
    for i in range(5):
        sublist.append({
            "user": id,
            "task": problem_names[i],
            "time": 1677996000 + submission_tok,
            "key": submission_tok,
            "score": float(id_dict[id]["score"][i]),
            "token": False,
            "extra": ["0"] * problem_subtasks[i]
        })
        submission_tok += 1
    
    with open("ranking/sublist/" + id, 'w') as f_sublist:
        json.dump(sublist, f_sublist, indent = 4)

###### add ranking/history ######

history = []
submission_tok = 0
for id in id_dict:
    for i in range(5):
        if (float(id_dict[id]["score"][i]) < 0.01):
            submission_tok += 1
            continue
        history.append([
            id,
            problem_names[i], 
            1677996000 + submission_tok,
            float(id_dict[id]["score"][i])
        ])
        submission_tok += 1

history.sort(key = lambda event : event[2])

with open("ranking/history", 'w') as f_history:
    json.dump(history, f_history, indent = 4)

###### add ranking/scores ######

score = {}
for id in id_dict:
    if (float(id_dict[id]["total"]) < 0.01):
        continue
    score[id] = {}
    for i in range(5):
        if (float(id_dict[id]["score"][i]) < 0.01):
            continue
        score[id][problem_names[i]] = float(id_dict[id]["score"][i])

with open("ranking/scores", 'w') as f_score:
    json.dump(score, f_score, indent = 4)
