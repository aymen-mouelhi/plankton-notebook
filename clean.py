import os
import sys, getopt
import shutil
from PIL import Image

def crop(original):
    image = Image.open(original)
    width, height = image.size   # Get dimensions

    left = 0
    top = 0
    right = width
    bottom = height - 31

    cropped = image.crop((left, top, right, bottom))
    return cropped

def clean(source, output):

    # First copy the directories tree
    recursive_overwrite(source, output)

    # Set workdir
    for subdir, dirs, files in os.walk(output):
        for file in files:
            print("subdir: " + subdir)
            filename = os.path.join(subdir, file)
            if (filename.endswith('.png') or filename.endswith('.jpg')):
                image = crop(filename)
                # Save changes.
                #im.save(os.path.join('withLogo', filename))
                #image.save(output + '\/'+ subdir² file)
                image.save(filename)

    # Loop over all files in the working directory.
    # for filename in os.listdir('.'):
    #     print("Cropping images in " + str(os.path))
    #     print("Cropping image " + str(filename))
    #     if (filename.endswith('.png') or filename.endswith('.jpg')):
    #         image = crop(filename)
    #         # Save changes.
    #         #im.save(os.path.join('withLogo', filename))
    #         image.save(output + '\/'+ filename)
    # get images from given folder
    # for each crop and store in destination folder

def recursive_overwrite(src, dest, ignore=None):
    if os.path.isdir(src):
        if not os.path.isdir(dest):
            os.makedirs(dest)
        files = os.listdir(src)
        if ignore is not None:
            ignored = ignore(src, files)
        else:
            ignored = set()
        for f in files:
            if f not in ignored:
                recursive_overwrite(os.path.join(src, f),
                                    os.path.join(dest, f),
                                    ignore)
    else:
        shutil.copyfile(src, dest)

if __name__ == '__main__':
    source = None
    output = None

    try:
        argv = sys.argv[1:]
        opts, args = getopt.getopt(argv,"hs:o:",["source=","output="])
    except getopt.GetoptError:
      print('clean.py -s <source folder> -o <output folder>')
      sys.exit(2)

    for opt, arg in opts:
       if opt == '-h':
           print('clean.py -s <source folder> -o <output folder>')
           sys.exit()
       elif opt in ("-s", "--source"):
           source = arg
       elif opt in ("-o", "--output"):
           output = arg

    print('Source: ' + str(source))
    print('Output: ' + str(output))

    # Clean Images
    clean(source, output)
