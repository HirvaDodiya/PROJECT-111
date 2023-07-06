import os
import shutil
source="C:/Users/LENOVO/Downloads/issLocation.jpeg"
destination="C:/Users/LENOVO/Downloads/copyissLocation.jpeg"
#route,extention=os.path.splitext(path)
#print(route)
#print(extention) 
path="C:/Users/LENOVO/Downloads"
dest=shutil.copy(source,destination)
print(os.listdir(path))
