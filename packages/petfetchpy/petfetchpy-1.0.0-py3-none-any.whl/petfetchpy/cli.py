
import sys
import os
import platform
import cpuinfo # type: ignore
import distro # type: ignore
from pathlib import Path
import random

from .colors import *


def app():
	info: list[str]
	sysinfo: dict[str, str] = {
		"SYSTEM": " ".join([distro.name(), distro.version()]),
		"KERNEL": " ".join([platform.system(), platform.release()]),
		"PROCESSOR": cpuinfo.get_cpu_info()["brand_raw"],
	}
	
	info = [
		"Petfetch",
		sysinfo["SYSTEM"],
		sysinfo["KERNEL"],
		sysinfo["PROCESSOR"],
	]

	petPath: Path = Path.joinpath(Path(__file__).resolve().parent, 'ascii-pets')
	petList: list = list(filter(lambda file: not file.startswith('.'), os.listdir(petPath)))
	petSpecDict: dict[str, tuple[str, str]] = {
		'blahaj': ('shark', 'tra'),
		'BLAHAJ': ('SHARK', 'tra'),
		'frogay': ('frog', 'gay'),
		'rubberduck': ('bird', 'yel'),
		'RUBBERDUCK': ('BIRD', 'yel'),
	}

	pet: str = random.choice(petList)[:-6]
	petFile: str = pet + '.ascii'
	col = 'res'
	
	# List of CLI args
	args: list[str] = sys.argv[1:]

	# Loop through all params
	while len(args) > 0:
		a = args[0]
		args = args[1:]

		# Help flag
		if (a == '-h' or a == '--help'):
			print(__doc__)
			exit()
		# Handle colors
		if ((a == '-c' or a == '--color') and len(args)):
			colArg = args[0]
			if colArg in colors.keys() or colArg in colorSets.keys():
				col = colArg
			else:
				print("Invalid color param")
				exit()
			
			args = args[1:]
			continue

		# Handle pets
		if ((a == '-p' or a == '--pet') and len(args)):
			# Get the pet arg
			petArg = args[0]
			# Check if the pet is in the special list
			if petArg in petSpecDict.keys():
				pet = petArg
				petFile = petSpecDict[petArg][0] + '.ascii'
				col = petSpecDict[petArg][1]
			# Check if the pet is in the normal list
			elif (petArg + '.ascii') in petList:
				pet = petArg
				petFile = petArg + '.ascii'
			# Otherwise invalid pet
			else:
				print('Invalid pet arg passed')
				exit()

			args = args[1:]
			continue

	
	lines: list[str]
	with open(Path.joinpath(petPath, petFile)) as file:
		lines = file.read().split('\n')


	info[0] = "Petfetch.py - " + pet[:1].upper() + pet[1:]
	pl: int = 0
	for l in lines:
		if len(l) > pl:
			pl = len(l)
	
	cols: list[str] = []
	if col in colorSets.keys():
		cols = colorSets[col].split(',')
	elif col in colors.keys():
		cols = [col]
	else:
		cols = ['res']
		
	colRatio: float = len(lines) / len(cols)

	print()
	for i in range(len(lines)):
		c = colors[cols[int(i / colRatio)]]
		l: str = lines[i]
		inf: str = ""
		if i in range(len(info)):
			inf = info[i]
		
		print(c, l.ljust(pl, " "), colors['res'], " : ", inf, sep='')
	print()