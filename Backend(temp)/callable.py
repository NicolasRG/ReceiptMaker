import main
import sys
import json
#travers the input as json if needed
items = json.loads(sys.argv[1])
# TODO add tax as a sys.argv
for key in items:
    print(key["item"])


main._main(items)
print("done")