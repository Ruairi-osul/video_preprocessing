from setuptools import setup, find_packages


description = ""
long_description = ""
setup(
    name="video_preprocessing",
    description=description,
    long_description=long_description,
    version="0.0.1",
    url="https://github.com/Ruairi-osul/video_preprocessing",
    author="Ruairi O'Sullivan",
    author_email="ruairi.osullivan.work@gmail.ie",
    license="GNU GPLv3",
    keywords="video",
    project_urls={"Source": "https://github.com/Ruairi-osul/video_preprocessing"},
    packages=find_packages(),
    python_requires=">=3",
    install_requires="ffmpeg-python==0.2.0",
    entry_points={
        "console_scripts":[
            "video_preprocessing = video_preprocessing.__main__:main"
        ]    
}
)
