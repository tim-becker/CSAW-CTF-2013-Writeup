# Tim Becker - 0x90.avi

import os
from operator import add

BLOCKSIZE = 256

def max_zero_bytes(files):
    counts = [0 for f in files]

    for i in xrange(len(files)):
        f = open(files[i])

        counts[i] = len([b for b in f.read() if ord(b) == 0])

    return files[counts.index(max(counts))]

def find_frequencies(f):
    byte_frequency = [[0 for i in xrange(265)] for j in xrange(256)]

    while True:
        block = f.read(BLOCKSIZE)

        block = map(ord, block)

        if len(block) != BLOCKSIZE:
            break

        for i in xrange(256):
            byte_frequency[i][block[i]] += 1

    return byte_frequency 

def guess_key(freqs):
    key = ""

    for i in xrange(256):
        key += chr(freqs[i].index(max(freqs[i])))

    return key


def xor(key, data):
    res = ""
    for i in xrange(len(data)):
        res += chr(ord(key[i]) ^ ord(data[i]))

    return res

def main():
    files = ["file{0}.enc".format(i) for i in xrange(9)]
    max_file = max_zero_bytes(files)
    f = open(max_file)
    byte_frequency = find_frequencies(f) 
    f.close()
    key = guess_key(byte_frequency)

    for i in xrange(9):
        in_file = open("file{0}.enc".format(i))
        out_file = open("file{0}.out".format(i), "w+")

        while True:
            data = in_file.read(256)
            out_file.write(xor(key[0:len(data)], data))

            if(len(data) != 256):
                break

        out_file.close()
        in_file.close()

if __name__ == "__main__":
    main()
