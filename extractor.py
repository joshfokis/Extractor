import os
import logging

locations = [
    os.getcwd() + '/TV',
    os.getcwd() + '/Movies',
]

logging.basicConfig(
    filename='extractor.log',
    level=logging.DEBUG,
    format='%(asctime)s %(name)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)


def finished(msg=False):

    if msg:
        print('files already extracted, moving on\n\n\n')
        logging.info('files already extracted, moving on\n\n\n')

    elif not msg:
        print('files finished extracting')
        logging.info('files finished extracting')

    else:
        print(msg)


def extractor(rar=None, found=False):

    if not found:

        os.system('unrar e ' + rar)
        os.system('touch ignore')

    else:

        finished(True)
        # logging.critical('something went wrong!')


def parser(path=None, files=None):

    print('checking rar status started')

    ext = []
    rar = ''

    logging.info('adding file types to list')

    for x in files:

        if x.split('.')[-1] == 'rar':

            rar = x

        ext.append(x.split('.')[-1])

    print('added file types to list completed')
    logging.info('added file types to list completed')
    print('checking for video file')
    logging.info('checking for video file')

    if 'ignore' not in files:

        rar = path.replace(' ', '\\ ') + '/' + rar

        print('calling extractor for ' + rar)
        logging.info('calling extractor for ' + rar)

        extractor(rar)

    else:

        finished(True)


def filing(path=None):

    print('parsing files started in ' + path)
    logging.info('parsing files started in ' + path)

    file_list = []

    for files in os.listdir(path):

        file_list.append(files)

    print(
        'parsing files complete now checking \
        if rar has already been extracted.'
    )

    logging.info(
        'parsing files complete now checking \
        if rar has already been extracted.'
    )

    parser(path, file_list)


def main(location=None):

    print('starting path searching for rar files in '
          + location)
    logging.info('starting path searching for rar files in '
                 + location)

    paths = []

    for path, dirs, files in os.walk(location):

        for f in files:

            if os.path.splitext(f)[-1] == '.rar':

                paths.append(path)

    print('found rar files in path now parsing files')
    logging.info('found rar files in path now parsing files')

    for p in paths:

        os.chdir(p)

        filing(p)


if __name__ == '__main__':

    for x in locations:

        main(x)
