import os
import sys
import json
import subprocess

CREATE_NO_WINDOW = 0x08000000

def main():

    if len(sys.argv) != 2:
        raise Exception("No input file specified")
        sys.exit(0)

    path = sys.argv[0].replace('webp-auto-convert.exe', '')
    fpath = sys.argv[1]
    fext = fpath.split('.')[-1]

    config = json.load(open(path + 'config.txt'))

    output_format = '.'+config['output-format']

    c = f'ffmpeg.exe -y -i "{fpath}" "{fpath.replace("."+fext, output_format)}" -hide_banner'

    if config['hideconsole']:
        subprocess.call(c, creationflags=CREATE_NO_WINDOW)
    else:
        os.system(c)

    if config['remove-on-completion']: os.remove(fpath)
    if config['open-on-completion']: 
        c = f'explorer.exe "{fpath.replace("."+fext, output_format)}"'
        if config['hideconsole']:
            subprocess.call(c, creationflags=CREATE_NO_WINDOW)
        else:
            os.system(c)

    sys.exit(0)

main()