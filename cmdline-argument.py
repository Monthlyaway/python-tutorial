import sys

if (len(sys.argv) < 2):
    print("Usage: cmdline-argument.py. No argument found.")
else:
    arguments = sys.argv[1:]
    print("Command line arguments: ", arguments)