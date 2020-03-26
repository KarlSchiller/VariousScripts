# It will print output to stdout before renaming each file
# This version pushes index until it is found that filename with such index is not taken.
# Although filenames may start at different index upon successive iterations of the script,
# the files themselves remain unchanged.

# Requires Python 3.7 -> dicts have to be ordered

import os
import time
import argparse


def get_filelist(input_folder):
    '''Get a list of files in folder @input_folder'''
    # directory with files to be renamed
    filelist = os.listdir(input_folder)

    # ignore folder
    for index,item in enumerate(filelist):
        if os.path.isdir(os.path.join(input_folder,item)):
           files.pop(index)

    filelist.sort()
    return filelist


def get_filename(fullname):
    '''Split the file extension from the filename'''
    if "." in fullname:
        return fullname.split(".")[0]
    else:
        return fullname


def rename_files(filelist, args):
    '''Rename all files in filelist as specified in args'''
    # list of filenames without extension to check for dublicates
    filenames = list(map(get_filename, filelist))
    current_index = 0

    for index,item in enumerate(filelist):

        extension = ""
        if "." in item:
            extension = "." + item.split(".")[-1]

        old_file = os.path.join(args.input_folder,item)
        if not args.individual:
            if filenames[index-1]==filenames[index]:
                current_index -= 1
        new_file = os.path.join(args.input_folder,args.prefix + "{:0>4d}".format(current_index) + extension)

        while os.path.isfile(new_file): # is there already a file named new_file?
              current_index += 1
              new_file = os.path.join(args.input_folder,args.prefix + "{:0>4d}".format(current_index) + extension)

        os.rename(old_file,new_file)
        if args.verbose:
            print(old_file + " renamed to " + new_file)
        current_index += 1


def main(args):
    files = get_filelist(args.input_folder)

    #  prevent dublicate filenames by adding timestamp to old ones
    timestamp = str(int(time.time()))
    for item in files:
        os.rename(os.path.join(args.input_folder,item),
                  os.path.join(args.input_folder,timestamp + item))

    # update filelist to files with timestamp
    files = get_filelist(args.input_folder)

    rename_files(files, args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A script to rename multiple files. \
            Files with the same name will be renamed same as well with default options.")
    parser.add_argument("input_folder", type=str,
            help="Folder containing files to rename")
    group = parser.add_mutually_exclusive_group()   # either verbose or quiet
    group.add_argument("-v", "--verbose", action="store_true",
            help="increase output verbosity")
    #  group.add_argument("-q", "--quiet", action="store_true",
            #  help="decrease output verbosity")
    parser.add_argument("-p", "--prefix", type=str, default="",
            help="String in each filename before ongoing number")
    parser.add_argument("-i", "--individual", action="store_true",
            help="Rename each file individually")

    args = parser.parse_args()

    main(args)
