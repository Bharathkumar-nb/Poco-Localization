src, ref, dst = None, None, None

with open('requirements.txt', 'r') as f:
	src = f.readlines()
with open('output.txt', 'r') as f:
	ref = f.readlines()

for line in src:
	for x in range(len(ref)):
		pat = ref[x].split()[0]
		if pat in line:
			del ref[x]
			with open('new_requirements.txt', 'a') as f:
				f.write(line)
			break
