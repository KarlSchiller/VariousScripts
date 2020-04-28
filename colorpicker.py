# General description:
# Open an image and receive a pixels color by clicking on it
# The image is given as an keyword argument

import cv2
import argparse


def main(args):
    pass


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
            description="A script to pick a color from a picture.")
    parser.add_argument("imagepath", type=str,
            help="path to image to pick a color from")
    parser.add_argument("-v", "--verbose", action="store_true",
            help="increase output verbosity")

    args = parser.parse_args()

    main(args)
    pass
