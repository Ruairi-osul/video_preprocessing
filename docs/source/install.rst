Installation
=============
Video Preprocessing should work on linux systems. It has not been tested on Windows or Mac-OS.

Before installing Video Preprocessing, you should first install `ffmpeg <https://www.ffmpeg.org/>`_. This is the software which is called under the hood by Video Preprocessing. On Ubuntu and Debian linux, you can install ffmpeg by excuting the following in a terminal.

::
  
  $ sudo apt-get install ffmpeg


Then to install Video Preprocessing:

:: 
  
  $ git clone https://github.com/Ruairi-osul/video_preprocessing.git
  $ cd video_preprocessing && pip install .


If the above executed without any errors, you can now start preprocessing videos.
