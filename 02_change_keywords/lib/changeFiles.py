import pathlib
import re
import random


class ChangeFiles:
    def __init__(self, change_str: str, pattern: str):
        self.__pattern = pattern
        self.__change_str = change_str

    @property
    def pattern(self):
        return self.__pattern

    @pattern.setter
    def pattern(self, val):
        self.__pattern = val

    @property
    def change_str(self):
        return self.__change_str

    @change_str.setter
    def change_str(self, val):
        self.__change_str = val

    def change_files(self, fpath: pathlib.Path, is_override=False) -> bool:
        try:
            with open (fpath.as_posix(), 'r') as fp:
                read = fp.read()

                changed_contents = re.sub(
                    r'{0}'.format(self.pattern),
                    f'{self.change_str}\g<1>',
                    read)

            if is_override:
                with open(fpath.as_posix(), 'w') as fp:
                    fp.write(changed_contents)
                    return True
            else:
                # with_name(): path 객체를 변경하지 않고도
                # 파일 이름을 변경한 새로운 경로를 쉽게 얻을 수 있는 method
                new_file_name = f'{random.randrange(100)}_{fpath.name}'
                with open(fpath.with_name(new_file_name), 'w') as fp:
                    fp.write(changed_contents)
                    return True
        except (FileNotFoundError, IOError) as err:
            print(err)
            return False


if __name__ == '__main__':
    cf = ChangeFiles('#include "PXR2', '#include "pxr(.+)')
    cf.change_files(pathlib.Path(''))