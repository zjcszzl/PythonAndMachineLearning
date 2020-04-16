import shutil
from time import ctime
from pathlib import Path

path = Path("ecommerce/__init__.py")
path.exists()
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
p1 = path.with_name("file.txt")
print(p1)
print(p1.absolute())


path = Path("ecommerce")
print(path.iterdir())
for p in path.iterdir():
    print(p)
paths = [p for p in path.iterdir() if p.is_dir()]
l = [p for p in path.glob("*.py")]
print(l)
print(paths)

path = Path("ecommerce/__init__.py")
# path.exists()
# path.rename("init.txt")
print(ctime(path.stat().st_ctime))

# with open("__init__.py","r") as file
# path.read_text()
# path.write_text("...")

source = Path("ecommerce/__init__.py")
target = Path() / "__init__.py"
shutil.copy(source, target)
