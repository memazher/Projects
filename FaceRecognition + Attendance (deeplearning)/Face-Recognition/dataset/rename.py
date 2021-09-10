import os
from os import path
import shutil

Source_Path = './dataset/Virat Kohli2'
Destination = './dataset/Virat Kohli2'
#dst_folder = os.mkdir(Destination)


def main():
    for count, filename in enumerate(os.listdir(Source_Path)):
        dst =  "Virat dark" + str(count) + ".jpg"

        # rename all the files
        os.rename(os.path.join(Source_Path, filename),  os.path.join(Destination, dst))


# Driver Code
if __name__ == '__main__':
    main()