import os
import re
import pathlib


# 부모 디렉토리
# 특정 확장자만 찾을 수 있는 옵션


class CheckWord:
    def __init__(self, fpath: str, depth: int):
        '''
        wrapper class
        :param fpath: 파일 경로
        :param depth: 파일이 저장되어 있는 깊이 값
        '''
        self.__fpath = fpath
        self.__depth = depth

    @property
    def fullpath(self) -> pathlib.Path:
        '''
        파일의 경로
        :return: 파일 경로(pathlib instance)
        '''
        return pathlib.Path(self.__fpath)

    @fullpath.setter
    def fullpath(self, val: str):
        self.__fpath = pathlib.Path(val)

    @property
    def depth(self) -> int:
        '''
        파일의 깊이 값
        :return: 깊이 값
        '''
        return self.__depth

    @staticmethod
    def is_check_word(fpath: pathlib.Path, find_str: str) -> bool:
        '''
        파일 내용 중 특정 문자열이 존재하는지
        :param fpath: 파일 경로
        :param find_str: 찾을 문자열
        :return: 찾았다면 true
        '''
        comp = re.compile(r'{0}'.format(find_str))
        with fpath.open('r') as fp:
            return comp.search(fp.read()) is not None

    def __str__(self):
        pass


class FindFiles:
    def __init__(self, parent_dir: pathlib.Path, pattern: list):
        '''
        사용자가 지정한 루트 디렉토리를 기준으로 특정 확장자의 파일들을 찾아내는 클래스
        :param parent_dir: 부모 디렉토리
        :param pattern: 필터링할 확장자
        '''
        self.__parent_dir = parent_dir
        self.__pattern = pattern

    @property
    def parent_dir(self) -> pathlib.Path:
        '''
        :return: 부모 디렉토리 (pathlib instance)
        '''
        return self.__parent_dir

    @parent_dir.setter
    def parent_dir(self, val):
        self.__parent_dir = val

    @property
    def pattern(self) -> list:
        '''
        :return: 확장자 패턴 (list)
        '''
        return self.__pattern

    @pattern.setter
    def pattern(self, val):
        self.__pattern = val

    def get_files(self):
        '''
        사용자가 지정한 부모 디렉토리로부터 모든 하위 디렉토리를 검색하여
        특정 확장자를 가진 파일들을 반환하는 제네레이터
        :return: 파일 경로 <generator>
        '''
        for f in self.parent_dir.glob('**/*'):
            # glob(f'{self.parent_dir}/**/*') 이라고 작성해도 괜찮음
            # .glob이 더 객체지향적이며 직관적 / glob()는 더 유연하며 간결함
            if not f.is_file():
                continue
            if '*' in self.pattern:
                yield f
            # else:
            #     if f.suffix in self.pattern:
            #         yield f

    def get_files_lst(self):
        '''
        사용자가 지정한 부모 디렉토리로부터 모든 하위 디렉토리를 검색하여
        특정 확장자를 가진 파일들을 반환하는 메서드
        :return: 파일 경로 <list>
        '''
        lst = list()
        for f in self.parent_dir.glob('**/*'):
            if not f.is_file():
                continue
            if '*' in self.pattern:
                lst.append(f)
            else:
                if f.suffix in self.pattern:
                    lst.append(f)
        return lst

    def get_files_recursion(self, dpath, depth=0):
        '''
        :param dpath: 부모 디렉토리
        :param depth: 깊이 값
        :return: file path generator
        '''
        lst = list()
        file_lst = os.listdir(dpath)
        for f in file_lst:
            # fullpath => '/home/rapa/workspace/usd/sdr/api.h'
            # fullpath => '/home/rapa/workspace/usd/sdr/testenv'
            fullpath = os.path.join(dpath, f)
            if os.path.isdir(fullpath):
                # lst += self.get_files_recursion(fullpath, depth+1)
                lst.extend(self.get_files_recursion(fullpath, depth+1))
                # yield from self.get_files_recursion(fullpath, depth+1)
            else:
                if os.path.isfile(fullpath):
                    if '*' in self.pattern:
                        lst.append(CheckWord(fullpath, depth))
                    else:
                        ext = f'.{fullpath.split(".")[-1]}'
                        if ext in self.pattern:
                            lst.append(CheckWord(fullpath, depth))
        yield from lst


if __name__ == '__main__':
    ff = FindFiles(
        pathlib.Path('/Users/yeko/Desktop/netflix_TD/self_study/qt_study'),
        ['.py'])
    # print(list(ff.get_files()))
    # print(ff.get_files_lst())

    res = ff.get_files_recursion('/Users/yeko/Desktop/netflix_TD/self_study/qt_study')
    # print(list(res))

    # print('#############3\n')
    for i in res:
        # print(type(i), type(res))
        assert isinstance(i, CheckWord)
        is_exist = CheckWord.is_check_word(i.fullpath, 'yoyoyoyoyo')
        print(
            f'{i.fullpath} - {i.depth}: {is_exist}')
