# Bird ascii art link with attributions: https://www.asciiart.eu/animals/birds-land
# Simpleaudio package: https://simpleaudio.readthedocs.io/en/latest/

import simpleaudio as sa
import time

birds = [
	"""
	 /\\ /\\ 
	((ovo))
	():::()
	  VVV	
	""",
	"""
	   \\\\
	   (o>
	\\\\_//)
	 \\_/_)
	  _|_
	""",
	"""
	 /""\\      ,
	<>^  L____/|
	 `) /`   , /
	  \\ `---' /
	   `'";\\)`
	     _/_Y
	"""
]

sound_mapping = {
	"o": "sine",
	":": "sine",
	"(": "sine",
	")": "sine",
	"v": "triangle",
	"V": "triangle",
	"<": "triangle",
	">": "triangle",
	"^": "triangle",
	"_": "square",
	"-": "square",
	"L": "square",
	"'": "square",
	"|": "square",
	"\"": "square",
	"/": "saw",
	"\\": "saw",
	",": "noise",
	"`": "noise",
	";": "noise",
	"Y": "noise",
	" ": "empty",
	"\t": "empty",
	"\n": "empty",
}

sine_sample = sa.WaveObject.from_wave_file("samples/sine.wav")
triangle_sample = sa.WaveObject.from_wave_file("samples/triangle.wav")
square_sample = sa.WaveObject.from_wave_file("samples/square.wav")
saw_sample = sa.WaveObject.from_wave_file("samples/saw.wav")
noise_sample = sa.WaveObject.from_wave_file("samples/noise.wav")
empty_sample = sa.WaveObject.from_wave_file("samples/empty.wav")

def log(s):
	with open("log.txt", "w") as f:
		f.write(s)

def load_sample(ch):
	if ch in sound_mapping:
		waveform = sound_mapping[ch]
		match waveform:
			case "sine":
				return sine_sample
			case "triangle":
				return triangle_sample
			case "square":
				return square_sample
			case "saw":
				return saw_sample
			case "noise":
				return noise_sample
			case "empty":
				return empty_sample
			case _:
				log("It broke LOL!!")
				return empty_sample
	else:
		log(f"Character {ch} not found in sound_mapping.")
		return empty_sample

def play_sample(ch):
	sample = load_sample(ch)
	play_obj = sample.play()
	play_obj.wait_done()

def print_and_play_birds():
	for bird in birds:
		print(bird)
		time.sleep(1)
		for ch in bird:
			play_sample(ch)
		time.sleep(1)

def main():
	print_and_play_birds()

if __name__ == "__main__":
	main()
