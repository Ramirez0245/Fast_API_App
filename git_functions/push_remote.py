import subprocess
import os

def main():
    load_branch()

def load_branch():
    COMMIT_MESSAGE = input("Enter your commit message/note: ")
    os.chdir(os.path.dirname(__file__))
    PUSH = [
        ["git", "add", "."],
        ["git", "commit", "-m", f'"{COMMIT_MESSAGE}"'],
        ["git", "push",  "origin", "master:main"],
        ]
    loop_actions(PUSH)
    
def loop_actions(command):
    for actions in command:
        print(actions)
        result = subprocess.run(actions, shell=True, capture_output=True, text=True)
        print(result)
        print(type(result))
        print(result.stdout)   

if __name__ == '__main__':
    main()