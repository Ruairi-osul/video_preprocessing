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
