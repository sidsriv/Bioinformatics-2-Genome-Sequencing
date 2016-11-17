__author__ = 'Siddhant Srivastava'

import sys

file_name = sys.argv[1]

def suffix(t):
	return t[1:]

def prefix(t):
	return t[:-1]



def overlap_graph(reads):
	overlaps = []
	for j in sorted(reads):
		for i in reads:
			if suffix(i) == prefix(j):
				overlaps.append(i + " -> " + j)
	return overlaps


def main():
	seqs = []
	with open(file_name) as file:
		for line in file:
			seqs.append(line[:-1])

	ans = overlap_graph(seqs)
	for s in ans:
		print s

if __name__ == '__main__':
	main()