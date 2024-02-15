import re
import os
import pathlib


class FindFiles:
    def __init__(self, parent_dir: pathlib.Path, pattern_ext: list):
        self.__parent_dir = parent_dir
        self.__pattern_ext = pattern_ext

    @property
    def parent_dir(self):
        return self.__parent_dir

    @parent_dir.setter
    def parent_dir(self, val):
        self.__parent_dir = val

    @property
    def pattern_ext(self):
        return self.__pattern_ext

    @pattern_ext.setter
    def pattern_ext(self, val):
        self.__pattern_ext = val

    def get_files(self):
        for file in self.parent_dir.glob('**/*'):
            if not file.is_file():
                continue
            if file.suffix in self.pattern_ext:
                yield file

    def get_files_lst(self):
        lst = list()
        for file in self.parent_dir.glob('**/*'):
            if not file.is_file():
                continue
            if file.suffix in self.pattern_ext:
                lst.append(file)
        return lst

    def get_files_recursion(self, lst: list):
        for file in self.parent_dir.glob('**/*'):
            if file.is_dir():
                self.get_files_recursion(lst)
            elif file.is_file():
                if file.suffix in self.pattern_ext:
                    lst.append(file.as_posix())
                    # print(lst)
        yield from lst


if __name__ == '__main__':
    path = '/Users/yeko/Desktop/netflix_TD/self_study/qt_study'
    ll = []
    ff = FindFiles(pathlib.Path(path), ['.py'])
    a = ff.get_files_recursion(ll)
    print(list(a))
    # yoyoyoyoyo

