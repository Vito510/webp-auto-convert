import os
import sys
import json

def main():
    print("WebP Auto Convert")

    print("Usage: webp-auto-convert.exe <file>")

    x = input("Press enter to close")

def start():

    if len(sys.argv) == 1:
        main()
        return None

    path = sys.argv[0].replace('webp-auto-convert.exe', '')
    fpath = sys.argv[1]
    fext = fpath.split('.')[-1]

    config = json.load(open(path + 'config.txt'))

    print(sys.argv)

    os.system(f'ffmpeg.exe -y -i "{fpath}" "{fpath.replace("."+fext,".png")}"')

    if config['remove-on-completion']: os.remove(fpath)
    if config['open-on-completion']: os.system(f'explorer "{fpath.replace("."+fext,".png")}"')

    sys.exit(0)

start()