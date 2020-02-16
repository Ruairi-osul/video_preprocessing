#!/usr/bin/env python3

import sys
import json
import ffmpeg 
from pathlib import Path
from .utils import json_to_dict
import argparse
from glob import glob

def preprocess_a_video(
    video: str,
    output_bitrate: str = "1000k",
    to_black_white=True,
    output_fps=30,
    output_file_format: str = "avi",
    brightness: int = 1,
    contrast: int = 1,
    output_name: str = None,
    output_dir: str = None,
    overwrite: bool = True,
    verbose: bool = False,
):
    """
    Takes a list of video paths. It compresses them to a specified bitrate
    and concatenates them together and saving them to a file

    Args:
        - videos: a list of paths to video files to work on (should be in order for concatenation)
        - output_bitrate: The bitrate of the output video file. 
                          This corresponds to the quality of the output video 
        - output_name: the name of the output video file to be saved
        - output_bitrate: The bitrate of the output video file. 
                          This corresponds to the quality of the output video 
        - to_black_white: Boolean of whether to convert to black and white or not
        - output_fps: fps of the output video 
    """
    # create output file name
    if not output_dir:
        output_dir = Path(".").absolute()
    else:
        output_dir = str(Path(output_dir).absolute())
    if not output_name:
        root = str(Path(video).name)
        output_name = f"{root.split('.')[0]}.{output_file_format}"
        output_name = "_".join(["processed", output_name])
    output_name = Path(output_dir) / output_name
    
    # create ffmpeg stream
    stream = ffmpeg.input(str(video))
    
    # add vfx
    if output_fps:
        stream = ffmpeg.filter(stream, "fps", fps=int(output_fps))

    if to_black_white:
        stream = ffmpeg.hue(stream, s=0)

    if brightness:
        stream = ffmpeg.hue(stream, b=int(brightness))

    if contrast:
        stream = ffmpeg.filter(stream, "eq", contrast=int(contrast))
    
    # create output stream and specify bitrate
    stream = ffmpeg.output(stream, str(output_name), **{"b:v": output_bitrate}, 
                                format=output_file_format)
    if overwrite:
        stream = ffmpeg.overwrite_output(stream)
    if verbose:
        print(stream.compile())
    
    # run ffmpex
    stream.run()

def return_parser():
    parser = argparse.ArgumentParser()
    
    # json options
    parser.add_argument("-j", "--json", required=False,
                        help="path to json file containing instructions for individual files")
    parser.add_argument("--json_dir",
                        help="path to directory to be searched for json files for processing")
    
    # single video options 
    parser.add_argument("--video", required=False,
                        help="path to video file to be processed")
    parser.add_argument("--output_name", required=False,
                        help="if processing a single video, its output file name can be specified here")
    
    # video directory options
    parser.add_argument("--video_dir",  required=False,
                        help="path to directory to be searched for video files for processing")
    parser.add_argument("--video_suffix", required=False,
                        help="if specifying a directory of videos, "
                             "suffix to search for when searching for video files")
    
    # output file options
    parser.add_argument("--output_dir", required=False,
                        help="path to directory where processed videos will be saved")
    parser.add_argument("--output_bitrate", required=False, 
                        default="750k",
                        help="bitrate of the processed video file e.g. '500k'")
    parser.add_argument("--output_file_format", required=False,
                        default="avi",
                        help="format of output file")
    
    # video effects options
    parser.add_argument("--to_black_white", action="store_true", required=False,
                        default=True,
                        help="whether to convert video to black and white")
    parser.add_argument("--brightness", required=False, default=1,
                        help="brightness level between -10 and 10")
    parser.add_argument("--output_fps", required=False,
                        default=30,
                        help="desired output frames per second")
    parser.add_argument("--contrast", required=False,
                        default="1",
                        help="Set the contrast expression. "
                             "The value must be a float value in range -1000.0 to 1000.0." 
                             "The default value is '1'")
    
    # program behaviour options
    parser.add_argument("--overwrite", required=False, default=True, action="store_true",
                        help="Overwrite output file if it exists")
    parser.add_argument("--verbose", default=False, action="store_true", 
                        help="print the call command to the terminal")

    return parser

def main(args=None):
    parser = return_parser()
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
        video = args["video"]
        del args["video"]
        preprocess_a_video(video=video, **args)
    elif args.get("video_dir"):
        if "video_suffix" not in args:
            args["video_suffix"] = '.mp4'
        input_videos = glob(f"{args['video_dir']}/*{args['video_suffix']}")
        del args["video_dir"]
        del args["video_suffix"]

        for video in input_videos:
            preprocess_a_video(video=video, **args)

if __name__ == "__main__":
    main()
