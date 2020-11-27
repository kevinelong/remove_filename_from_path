# How do you remove a filename from a path in Python?

def root_without_name(text):
    parts = text.split("/")
    if len(parts) > 0:
        return "/".join(parts[:-1])
    return text


print(root_without_name("/foo/bar/name.txt"))
print(root_without_name("foo/name.txt"))
print(root_without_name("foo/bar/name.txt"))
print(root_without_name("name.txt"))
