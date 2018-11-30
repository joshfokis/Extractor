import os
import subprocess


def main():

    location = input('which folder to extract?\n\n>>>')

    for path, dirs, files in os.walk(location):
        if 'ignore' not in files:
            for file in files:
                if os.path.splitext(file)[-1] == '.rar':
                    os.chdir(path)
                    extract = subprocess.Popen(
                                ['unrar', 'e', '-o-', file],
                                stdout=subprocess.PIPE
                                )
                    ignore = subprocess.Popen(
                                ['touch', 'ignore'],
                                stdout=subprocess.PIPE
                                )
                    try:
                        extract.communicate()
                        ignore.communicate()
                    except Exception as e:
                        print('Could not extract: {}'.format(e))
                        continue
        else:
            continue


if __name__ == "__main__":
    main()
