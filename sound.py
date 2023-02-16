import os
import platform
from pathlib import Path
from pydub import AudioSegment
from pydub.playback import play
platform_name = platform.system()
def path_to_ffmpeg():
	SCRIPT_DIR = Path(__file__).parent 
	return str(Path("C:\\ffmpeg\\bin", "ffmpeg.exe"))
	# if platform_name == 'Windows':
	# 	return str(Path(SCRIPT_DIR, "win", "ffmpeg", "ffmpeg.exe"))
	# elif platform_name == 'Darwin':
	# 	return str(Path(SCRIPT_DIR, "mac", "ffmpeg", "ffmpeg"))
	# else:
	# 	return str(Path(SCRIPT_DIR, "linux", "ffmpeg", "ffmpeg"))
AudioSegment.ffmpeg = path_to_ffmpeg()

if platform_name == 'Windows':
	os.environ["PATH"] += os.pathsep + str(Path(path_to_ffmpeg()).parent)
else:
	os.environ["LD_LIBRARY_PATH"] += ":" + str(Path(path_to_ffmpeg()).parent)



song = AudioSegment.from_mp3('1.mp3')
# print(song)
# play(song)
song.export("1.wav", format="wav")
