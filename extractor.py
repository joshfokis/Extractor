import os
import subprocess


def main():
    """
    this is the main function to extract rar files.
    """

    # location to walk and get all rar files to extract
    location = input('which folder to extract?\n\n>>>')

    # find all paths directories adn files in the location
    # requested.
    for path, dirs, files in os.walk(location):
        # check if a blank file named ignore is or is not
        # in the folder
        if 'ignore' not in files:
            for file in files:
                # search for a rar file extention in the
                # folder
                if os.path.splitext(file)[-1] == '.rar':
                    # change directory to extract in the
                    # same directory
                    os.chdir(path)
                    # run the command line application unrar
                    # to extract the file but not to overwrite
                    extract = subprocess.Popen(
                                ['unrar', 'e', '-o-', file],
                                stdout=subprocess.PIPE
                                )
                    # create the blank ignore file to skip
                    # the folder on the next run.
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
`
