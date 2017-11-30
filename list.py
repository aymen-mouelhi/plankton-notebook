import os, sys

if __name__ == '__main__':
    # Set workdir
    path = sys.argv[1]
    os.chdir(path)

    file = open("list.txt","w")
    for filename in os.listdir('.'):
        file.write(str(filename) + "\n")
        print("Folder: " + str(filename))

    file.close()
