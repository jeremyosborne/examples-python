"""Lab:

Ask the user for their name.
Ask the user for their favorite color.
Fail politely if the user puts a ":" character in the name or color.
Write the name:color to the file "echo_out.txt".
Use a try/except and watch for IOError.
Before exiting, echo back all of the contents of the file, splitting
on the colon and formatting the name in a left aligned fixed width field of 20.
Run this multiple times to make sure it is working as expected.
"""

import sys

name = raw_input("What is your name?\n")
color = raw_input("What is your favorite color?\n")

if ":" in name or ":" in color:
    print "Sorry, the : character is not allowed in the name or color."
    sys.exit(0)

try:
    with open("echo_out.txt", "a+") as f:
        f.write(name+":"+color+"\n")
        f.seek(0)
        print "Previous favorite colors:"
        for line in f:
            name, color = line.rstrip().split(":")
            print "{:<20} {}".format(name, color)
except IOError as err:
    print "File Error:", err
