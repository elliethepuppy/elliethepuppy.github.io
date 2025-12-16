#!/usr/bin/python


import subprocess

def main() -> None:
    with open("./blog/index.html", "w") as blog_home:
        with open("./blog/blog.html", "r") as bh:
            blog_home.writelines(bh)
        bh.close()
    blog_home.close()

    commit_msg = input("Enter commit msg > ")

    subprocess.run(
        ["git", "add", "."]
    )

    subprocess.run(
        ["git", "commit", "-m", f"{commit_msg}"]
    )

    subprocess.run(
        ["git", "push", "-u", "origin", "main"]
    )
if __name__ == "__main__":
    main()
