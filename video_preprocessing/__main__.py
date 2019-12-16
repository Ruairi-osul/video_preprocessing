#!/usr/bin/env python3

import sys
import json
import moviepy.editor as mp
import moviepy.video.fx.all as vfx
from pathlib import Path
from .utils import json_to_dict


def preprocess_a_video(
    videos,
    output_name=None,
    output_dir=None,
    output_bitrate="500k",
    to_black_white=True,
    output_fps=30,
    contrast_luminosity=None,
):
    """
    Takes a list of video paths. It compresses them to a specified bitrate
    and concatenates them together and saving them to a file

    Parameters:
        - videos: a list of paths to video files to work on (should be in order for concatenation)
        - output_name: the name of the output video file to be saved
        - output_bitrate: The bitrate of the output video file. 
                          This corresponds to the quality of the output video 
        - to_black_white: Boolean of whether to convert to black and white or not
        - output_fps: fps of the output video 
        - contrast_luminosity: a dict of contrast and luminosity valus for adjustment
    """
    if not output_dir:
        output_dir = Path(".").absolute()
    if not output_name:
        root = str(Path(videos[0]).name)
        curname = root if ".mp4" in root.lower() else root.split(".")[
            0] + ".mp4"
        output_name = "".join(["processed", curname])
    videos = list(map(lambda x: mp.VideoFileClip(x), videos))
    output_video = mp.concatenate_videoclips(videos)

    if to_black_white:
        output_video = output_video.fx(vfx.blackwhite)
    if contrast_luminosity is not None:
        output_video = output_video.fx(
            vfx.lum_contrast,
            contrast=contrast_luminosity["contrast"],
            lum=contrast_luminosity["lum"],
        )

    output_video.write_videofile(
        output_name, bitrate=output_bitrate, fps=output_fps)

def main(args=None):
    for input_json in sys.argv[1:]:
        config_options = json_to_dict(input_json)
        preprocess_a_video(**config_options)
    

if __name__ == "__main__":
    main()
