import sys

def run(argv):
    print(len(argv), argv)

if __name__ == '__main__':
    print(__name__)
    run(sys.argv)