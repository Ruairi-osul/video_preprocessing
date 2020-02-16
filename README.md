# video_preprocessing

A small installable python script for compressing video files. Read the docs [here](https://video-preprocessing.readthedocs.io/en/latest/).


## Installation

~~~
$ git clone https://github.com/Ruairi-osul/video_preprocessing.git
$ cd video_preprocessing
$ pip3 install .
~~~
or
```
$ git clone https://github.com/Ruairi-osul/video_preprocessing.git
$ cd video_preprocessing
$ pip install .
```

### Quickstart

##### Process a single video

```
$ video_preprocessing --video PATH_TO_YOUR_VIDEO 
```

##### Process a directory of videos

```
$ video_preprocessing --video_dir PATH_TO_DIRECTORY_CONTAINING_YOUR_VIDEOS --video_suffix .mp4
```

##### Specify options

```
$ video_preprocessing --video_dir SOME_DIR --video_suffix .avi --to_black_white --brightness 2
```

##### See available options

```
$ video_preprocessing --help
```

##### Set parameters for a video in a json file

```
$ video_preprocessing -j PATH_TO_JSON
```

##### Pass a directory of json files for batch processing

```
$ video_preprocessing --json_dir PATH_TO_DIRECTORY_CONTAINING_JSONS
```
