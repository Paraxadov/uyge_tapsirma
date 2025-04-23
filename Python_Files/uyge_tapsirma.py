from pathlib import Path
import shutil
import os


sorawshi = input("File lardi jiynap dublikatlarin oshiriw [awa/yaq]:  ")


def file_sort():
    Path("Python_Files").mkdir(exist_ok=True)
    for file in Path(".").glob("*.py"): 
        shutil.copy(file, "Python_Files")


def dublicate_remove():
    for file in Path(".").glob("*.py"):
        if file.name != "uyge_tapsirma.py":
            file.unlink()
    

if sorawshi == "awa":
    file_sort()
    dublicate_remove()
    print("Sizin file lariniz Python_Files atli papkag'a koshirildi")

elif sorawshi == "yaq":
    print("Process juwmaqlandi")
    exit()

else:
    print("Juwapti qayta kirgiz")