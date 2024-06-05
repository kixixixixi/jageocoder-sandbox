import sys
import jageocoder

jageocoder.init()

def fetch(adrr: str):
    return jageocoder.search(adrr)

if __name__ == "__main__":
    args = sys.argv

    print(fetch(args[len(args) - 1]))