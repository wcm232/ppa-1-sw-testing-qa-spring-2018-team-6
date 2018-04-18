import console
import host
import sys

if len(sys.argv) < 2:
    print("Usage: main.py <console|host>")
else:
    if sys.argv[1] == "console":
        console.main()
    elif sys.argv[1] == "host":
        host.main()
    else:
        print("Unknown argument '" + sys.argv[1] + "'. Usage: main.py <console|host>")
    
