import zipfile
import pathlib

# 找到 dist 目录下的第一个 whl 文件
whl = next(pathlib.Path("dist").glob("*.whl"))
print(f"Checking {whl} ...")

with zipfile.ZipFile(whl) as z:
    for name in z.namelist():
        if "METADATA" in name:
            print("--- METADATA content ---")
            print(z.read(name).decode())
