# import os

# BASE_DIR = os.path.dirname(__file__)
# file_path = os.path.join(BASE_DIR, "my_file.txt")

# file = open(file_path)
# contents = file.read()
# print(contents)
# file.close()

# import os

# BASE_DIR = os.path.dirname(__file__)
# file_path = os.path.join(BASE_DIR, "my_file.txt")

# with open(file_path) as file:
#     contents = file.read()
#     print(contents)


# import os

# BASE_DIR = os.path.dirname(__file__)
# file_path = os.path.join(BASE_DIR, "my_file.txt")

# with open(file_path, mode = "w") as file: ## w for write - but it overwrites.
#     file.write("New text.")

## when you try to open a file that doesn't exist while in "write mode," it'll make a new file.


# import os

# BASE_DIR = os.path.dirname(__file__)
# file_path = os.path.join(BASE_DIR, "my_file.txt")

# with open(file_path, mode = "a") as file: # a for append
#     file.write("\nNew text.")
