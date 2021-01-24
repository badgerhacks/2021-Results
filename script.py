#imports
import csv
import requests

# declare histogram
results = dict()

# declare judges
judges = []
guest_judges = ['Guest Judge 1', 'Guest Judge 2']
judge_multiplier = 1.5

# download csv
sheet_url = "https://docs.google.com/spreadsheet/ccc?key=1LTE79QybOVBJHwNXBD7mxkop_wl60PM7eQ2dNId9AhQ&output=csv"
response = requests.get(sheet_url)
assert response.status_code == 200, 'Wrong status code'
open('sheet.csv', 'wb').write(response.content)

# print stuff
print("\nRESULTS:")

# go through csv
with open('sheet.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    row_number = 1
    running_score = 5
    for row in reader:
        if row_number > 1:
            for i in range(1, len(row)):
                judge = judges[i-1]
                cell = row[i]
                project = cell.strip()
                if project != "":
                  cur_score = results.get(project, 0)
                  if judge in guest_judges:
                    results[project] = cur_score + running_score * judge_multiplier
                  else:
                    results[project] = cur_score + running_score
                  print(judge + " gave " + project + " " + str(results[project]-cur_score) + " points")
            running_score -= 1
        else:
            judges = row[1::]
        row_number += 1

# display results
print("\nFINAL RESULTS:")
print(results)
print("\n")