import os

directory = input("\nEnter the Directory Name : ")

saveDirectory = input("\nEnter the Directory Name to Save Renamed Files : ")

name = input("\nEnter the Characters to Remove \n\n\tE.x !@#$%^&* \n \t\t\t:")
Characters = list(name)

for (dirpath, dirnames, filenames) in os.walk(directory):
    for filename in filenames:
        oldName = str(os.path.join(dirpath, filename))
        newFile = ''
        for name in filename:
            if name in Characters:
                pass
            else:
                newFile = newFile + name
        
        newName = str(os.path.join(saveDirectory , newFile))
        print("\n\n\t\tOld Name : ", oldName)
        print("\t\tNew Name : ", newName)
        os.rename(oldName , newName )
        print("\t\tFile Renamed Successfully")






