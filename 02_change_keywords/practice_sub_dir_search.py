import os
import pathlib
import re


def search(fpath):
    try:
        dir_names = os.listdir(fpath)
        print(dir_names)
        for filename in dir_names:
            full_filename = os.path.join(fpath, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                # print(ext)
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass


def check_word(fpath, find_str):
    pat = re.compile(r'{0}'.format(find_str))
    with fpath.open('r') as fp:
        return pat.search(fp.read()) is not None


path = '/'
# search(path)
# check_word(path, 'print')


# print('\n\n\n')
for path, dir, files in os.walk(path):
    # print(path, dir, files)
    for filename in files:
        # print (f'filename >> {filename}')
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            fpath = f'{path}/{filename}'
            # print(f'{path}/{filename}')
            fpath = pathlib.Path(fpath)
            is_exist = check_word(fpath, 'yoyoyoyo')
            print(f'{fpath.as_posix()}: {is_exist}')


    # print (f'path >> {path}\ndir >> {dir}\nfiles >> {files}')
