# General description:
# Open an image and receive a pixels color by clicking on it
# The image is given as an keyword argument

import argparse     # read input image path
import cv2  # image manipulation
from tkinter import Tk  # get monitor size

def main(args):

    win = cv2.namedWindow('ColorPicker', cv2.WINDOW_NORMAL)
    if args.verbose:
        print("Read image "+args.imagepath)
        print("Zoom in      <CTRL>+<+>")
        print("Zoom out     <CTRL>+<->")
        print("Save         <CTRL>+<s>")
        print("Quit         <q>")
    img = cv2.imread(args.imagepath, 1)   # import image colored withouth transparency
    # (:,:,0) blue channel
    # (:,:,1) green channel
    # (:,:,2) red channel

    #  print('Image dimensions : ', img.shape)
    #  img_scale = img.shape[0]/img.shape[1]   # width/height

    # # get monitor size
    # root = Tk()
    # monitor_width = root.winfo_screenwidth()
    # monitor_height = root.winfo_screenheight()
    # print('monitor width  ', monitor_width)
    # print('monitor height ', monitor_height)

    # # rescale image to adequate size
    # # 90% of monitor width or height, depending which side is longer
    # height = int(0.9*monitor_height)
    # width = int(height/img_scale)
    # if width > (0.95*monitor_width):
    #     print("TEST")
    #     width = int(0.9*monitor_width)
    #     height = int(width*img_scale)
    # img = cv2.resize(img, (width, height))

    # show image
    cv2.imshow('ColorPicker', img)
    terminated = False
    while not terminated:
        if (cv2.waitKey(0) & 0xFF == 113):
            cv2.destroyWindow('ColorPicker')
            terminated = True
            if args.verbose:
                print("<q> pressed, program terminated")


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
            description="A script to pick a color from a picture.")
    parser.add_argument("imagepath", type=str,
            help="path to image to pick a color from")
    parser.add_argument("-v", "--verbose", action="store_true",
            help="increase output verbosity")

    args = parser.parse_args()

    try:
        main(args)
    except KeyboardInterrupt:
        if args.verbose:
            print('Program terminated by KeyboardInterrupt')
