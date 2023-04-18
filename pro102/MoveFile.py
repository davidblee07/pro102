import os;
import shutil;

from_dir = "C:/Users/PC/Downloads"
to_dir = "C:/Users/PC/Desktop/Byjus David/Arquivos_Documentos"
listOfFiles = os.listdir(from_dir)
#print(listOfFiles)

for file_name in listOfFiles:  
  name,extension = os.path.splitext(file_name)

  if(extension==" "):
    continue
  if(extension in [".gif",".png", ".jpg", ".jpeg", ".jfif"]):
    path1 = from_dir+"/"+file_name
    path2 = to_dir+"/"+"Arquivos_Documentos"
    path3 = to_dir+"/"+"Arquivos_Documentos"+"/"+file_name
    print(path1)
    print(path3)
    if(os.path.exists(path2)):
      print("movendo " + file_name + ".....")
      shutil.move(path1, path3)
    else:
      os.makedirs(path2)  
      print("movendo " + file_name + ".....")
      shutil.move(path1, path3)