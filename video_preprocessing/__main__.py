#!/usr/bin/env python3

import sys
import json
import moviepy.editor as mp
import moviepy.video.fx.all as vfx
from pathlib import Path
from .utils import json_to_dict
import argparse
from glob import glob

def preprocess_a_video(
    videos,
    output_bitrate: str = "500k",
    to_black_white=True,
    output_fps=30,
    output_file_format: str = ".mp4",
    contrast_luminosity=None,
    brightness_factor=None,
    output_name: str = None,
    output_dir: str = None,
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
        output_name = "_".join(["processed", curname])
    
    output_name = Path(output_dir) / output_name
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
    if brightness_factor:
        output_video = output_video.fx(
            vfx.colorx,
            factor=brightness_factor
        )

    output_video.write_videofile(
        str(output_name), bitrate=output_bitrate, fps=output_fps)

def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("-j", "--json", required=False,
        help="path to json file containing instructions for individual files")
    parser.add_argument("--json_dir",
        help="path to directory to be searched for json files for processing")
    parser.add_argument("--video", required=False,
        help="path to video file to be processed")
    parser.add_argument("--video_dir",  required=False,
        help="path to directory to be searched for video files for processing")
    parser.add_argument("--output_dir", required=False, 
        default="/mnt/86f4d28f-2b08-48b6-9bc1-b8e030877e3b/preprocessed_videos",
        help="path to directory where processed videos will be saved")
    parser.add_argument("--output_bitrate", required=False, 
        default="750k",
        help="bitrate of the processed video file e.g. '500k'")
    parser.add_argument("--to_black_white", required=False,
        default=True,
        help="whether to convert video to black and white")
    parser.add_argument("--brightness_factor", required=False, 
        default=2.5,
        help="factor for increasing the brightness")
    parser.add_argument("--video_suffix", required=False,
        help="suffix to search for when searching for video files")
    parser.add_argument("--output_name", required=False,
        help="if processing a single video, its output file name can be specified here")
    parser.add_argument("--output_file_format", required=False,
        default=".mp4",
        help="format of output file")
    parser.add_argument("--output_fps", required=False,
        default=30,
        help="desired output_fps")

    args = vars(parser.parse_args())
    args = {k: v for k, v in args.items() if v is not None}

    if args.get("json"):
        config_options = json_to_dict(args["json"])
        preprocess_a_video(**config_options)
    elif args.get("json_dir"):
        input_jsons = glob(f"{args['json_dir']}/*.json")
        for input_json in input_jsons:
            config_options = json_to_dict(input_json)
            preprocess_a_video(**config_options)
    elif args.get("video"):
        video = [args["video"]]
        del args["video"]
        preprocess_a_video(videos=video, **args)
    elif args.get("video_dir"):
        if "video_suffix" not in args:
            args["video_suffix"] = '.mp4'
        input_videos = glob(f"{args['video_dir']}/*{args['video_suffix']}")
        del args["video_dir"]
        del args["video_suffix"]

        for video in input_videos:
            preprocess_a_video(videos=[video], **args)

if __name__ == "__main__":
    main()
