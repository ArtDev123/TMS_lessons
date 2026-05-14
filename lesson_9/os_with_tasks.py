import os

current_folder = os.getcwd()

backups_dir = os.path.join(current_folder, "backups")
if not os.path.exists(backups_dir):
    os.mkdir(backups_dir)


txt_paths = []
for name in os.listdir(current_folder):
    path = os.path.join(current_folder, name)
    if os.path.isfile(path) and name.endswith(".txt"):
        txt_paths.append(os.path.abspath(path))


paths_file = os.path.join(backups_dir, "paths_list.txt")
with open(paths_file, "w", encoding="utf-8") as f:
    f.write("\n".join(txt_paths))
