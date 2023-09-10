import argparse
import sys

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('-f', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
sys.stderr.write('Warning, log file not found starting a new one\n')
sys.exit(130)