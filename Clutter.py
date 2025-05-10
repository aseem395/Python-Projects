import os
files = os.listdir("D:/Coding")
i = 1
for file in files:
    print(file)
    if (file.endswith(".png")):
        os.rename(f"D:/Coding/{file}", f"D:/Coding/{i}.png")
        i = i + 1