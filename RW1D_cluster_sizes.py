#!/usr/bin/python
#
# Escape time of a random walker from a cylinder with reflecting
# boundaries on the left and open boundaries on the right.
# PNG output of a single trajectory.
# Habib Rehmann and Gunnar Pruessner
#

import random

# https://docs.python.org/2/howto/argparse.html
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--seed", type=int, help="seed of the RNG", default=7)
parser.add_argument("-L", "--Length", type=int, help="length of the system (PBC apply)", default=200)
parser.add_argument("-i", "--iterations", type=int, help="iterations", default=100)
args = parser.parse_args()


print "# Info: seed = ", args.seed
print "# Info: Length = ", args.Length
print "# Info: iterations = ", args.iterations
 
xStart = 0

random.seed(args.seed)  # set random seed
for i in range(args.iterations):
  x = xStart   # x coordinate of point.

  # Generate a randomwalk
  s=0
  while True:
      s += 1
      if (bool(random.getrandbits(1))):
        x += 1
      else:
	x -= 1
      if (x >= args.Length):
	  x -= args.Length
      if (x < 0):
	  x += args.Length
      if (x==xStart):
      	print s
	break

