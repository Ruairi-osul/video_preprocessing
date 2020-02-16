Quickstart
===========


It is easy to get started with Video Preprocessing.

Basic Usage
^^^^^^^^^^^^

Convert a video to black and white:

::

  $ video_preprocessing --video <path_to_video> --to_black_white --output_name <desired_output_name>


Change the frame rate of a video:

::

  $ video_preprocessing --video <path_to_video> --output_fps <desired_fps> --output_name <desired_output_name>

Change the bitrate (video quality) of a video:

::

  $ video_preprocessing --video <path_to_video> --output_bitrate <desired_output_bitrate> --output_name <desired_output_name>


You can perform preprocessing on multiple videos by setting the input to be a directory

::

  $ video_preprocessing --video_dir <directory> --video_suffix <input_videos_file_format> --to_black_white --ouput_dir <directory>


Using JSON input
^^^^^^^^^^^^^^^^^

You can also specify Video Preprocessing's behaviour using JSON input. One reason you might want to do this is so that you can remember how the output file was created.

See the following example:

::
 
  $ video_preprocessing -j input_json.json


where input_json may look like the following


::

  {
    "video": "/path/to/video",
    "to_black_white": true,
    "output_name": "name.avi"
  }

  
To batch process files in this way, you can specify a directory of similar json files:

:: 

  $ video_preprocessing --json_dir <directory>

where <directory> contains multiple json files.

::

  .
  ├ a_final_video.json
  ├ another_video.json
  └ one_video.json


Other Options
^^^^^^^^^^^^^^
Check out all of the options in the :doc:`API Reference <api>` for a list of all of the options.
