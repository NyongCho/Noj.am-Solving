import sys
input = sys.stdin.read

keys = {'A': 0, 'A#': 'Bb', 'Bb': 'A#', 'B': 0, 'C': 0, 'C#':'Db','Db':'C#', 'D': 0, 'D#': 'Eb','Eb': 'D#', 'E': 0, 'F': 0, 'F#': 'Gb','Gb': 'F#', 'G': 0, 'G#': 'Ab','Ab': 'G#'}

datas = input().splitlines()

for i, data in enumerate(datas):
    key, scale = data.split()
    if 0 != keys[key]:
        print(f'Case {i+1}: {keys[key]} {scale}')
    else:
        print(f'Case {i+1}: UNIQUE')