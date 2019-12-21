import json

# movie = {}
# movie["title"] = "minority report"
# movie["director"] = "Steven Spielberg"
# movie["duration"] = "1:45"
#
# file2 = open("D:\\3Pillar\\Python\\Beginner DevOps\\Jason1.txt", "w", encoding="utf=8")
#
# json.dump(movie, file2)
#
# file2.close()

file1 = open("D:\\3Pillar\\Python\\Beginner DevOps\\Jason1.txt", "r", encoding="utf=8")
print(json.load(file1))
file1.close()
