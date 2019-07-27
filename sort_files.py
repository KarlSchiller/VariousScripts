import os
import time
import argparse


def get_filelist(input_folder, descending):
    '''Get a list of files in folder @input_folder'''
    # directory with files to be renamed
    filelist = os.listdir(input_folder)

    # ignore folder
    for index,item in enumerate(filelist):
        if os.path.isdir(os.path.join(input_folder,item)):
           files.pop(index)

    filelist.sort(reverse=descending)
    return filelist


def main(args):
    if not args.quiet:
        print("Sort " + args.input_folder)

    files = get_filelist(args.input_folder, args.descending)

    sort_files(files, args)


def sort_files(files, args):
    #  get timestamps
    mod_time = []
    for picture in files:
        if args.modification:
            mod_time.append(str(int(os.stat(args.input_folder+'/'+picture).st_mtime)))
        else:
            mod_time.append(str(int(os.stat(args.input_folder+'/'+picture).st_ctime)))

    for index,item in enumerate(files):
        last_index = 0
        extension = ""
        if '.' in item:
            extension = '.' + item.split('.')[-1]
        old_file = os.path.join(args.input_folder,item)
        new_file = os.path.join(args.input_folder,mod_time[index] + extension)
        while os.path.isfile(new_file):
              last_index += 1
              new_file = os.path.join(args.input_folder,mod_time[index]+str(last_index)+extension)
        os.rename(old_file,new_file)
        if args.verbose:
            print(old_file + ' renamed to ' + new_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A script to fix a broken order of pictures. \
    It will take all pictures in the given path and rename them according to \
    their creation date and time.")
    parser.add_argument("input_folder", type=str,
            help="Folder containing files to rename")
    group = parser.add_mutually_exclusive_group()   # either verbose or quiet
    group.add_argument("-v", "--verbose", action="store_true",
            help="increase output verbosity")
    group.add_argument("-q", "--quiet", action="store_true",
            help="decrease output verbosity")
    parser.add_argument("-m", "--modification", action="store_true",
            help="Use the last modification date and time instead")
    parser.add_argument("-d", "--descending", action="store_true",
            help="Sort files in descending order")

    args = parser.parse_args()

    main(args)
