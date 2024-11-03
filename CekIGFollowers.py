import json

# Gantilah path ini dengan path file pada device anda
with open(r"path\to\your\file\followers_1.json") as f:
    followers_data = json.load(f)

followers = []
for entry in followers_data:
    if "string_list_data" in entry:
        for item in entry["string_list_data"]:
            followers.append(item["value"].strip())

with open(r"path\to\your\file\following.json") as f:
    following_data = json.load(f)

following = []
for entry in following_data["relationships_following"]:
    if "string_list_data" in entry:
        for item in entry["string_list_data"]:
            following.append(item["value"].strip())

# Mengidentifikasi pengguna yang anda ikuti tetapi tidak mengikuti anda kembali
unfollowers = [user for user in following if user not in followers]

# Menampilkan hasilnya
for user in unfollowers:
    print("https://www.instagram.com/" + user)