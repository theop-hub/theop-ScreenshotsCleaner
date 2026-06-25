from pathlib import Path
from datetime import datetime
from send2trash import send2trash
import shutil
toDelete = Path("OldScreenshots")

def createFolder():
    try:
        toDelete.mkdir()
        print(f"Directory '{toDelete}' created successfully.")
    except FileExistsError:
        print(f"Directory '{toDelete}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{toDelete}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


def clean():
    count = 0
    folder = Path.home() / "Pictures" / "Screenshots"
    date = datetime.now()
    for file in folder.iterdir():
        if file.is_file() and file.name != "desktop.ini":
            fileDate = file.name.split(" ")[1]
            fileDate = datetime.strptime(fileDate, "%Y-%m-%d")
            difference = date - fileDate
            if difference.days > 90:
                count += 1
                newPath = toDelete / file.name
                shutil.move(file, newPath)
    print(f"{count} old screenshots found!")

createFolder()
clean()
send2trash(toDelete)
print("Screenshots deleted.")