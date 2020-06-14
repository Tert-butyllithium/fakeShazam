# FakeShazam

Name specific song in hours

## Requirements

- ffmpeg
- python 3
- see [requirements.txt](requirements.txt)

## Use Manner

0. start with some `.mp3` files in the `data/music` directory.
1. first run [init.py](init.py) to initialize the inverted index (which takes longer to run). The generated file will be under `data/metadata` (this process takes a long time).
2. then run [gao.py](gao.py) and pass the auto file you want to search for. 

## Process

1. generate fingerprints for each sound file, referencing [shazam](https://www.ee.columbia.edu/~dpwe/papers/Wang03-shazam.pdf) and [worldeil](https://github.com/worldveil/dejavu) 
2. create an inverted index for each music file based on the fingerprint.
3. for the audio file to be searched, considering its fingerprint occurrence in inverted index and retrieval the result
