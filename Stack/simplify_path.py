""" https://leetcode.com/problems/simplify-path/ """


def simplify_path(path: str) -> str:
    path_split = path.split("/")
    path_split = [p for p in path_split if p]
    stack = []
    for fd in path_split:
        if fd == "..":
            if stack:
                stack.pop()
        elif fd == ".":
            continue
        else:
            stack.append(fd)

    canonical_path = ""
    for fd in stack:
        canonical_path += "/" + fd

    return canonical_path if canonical_path else "/"
