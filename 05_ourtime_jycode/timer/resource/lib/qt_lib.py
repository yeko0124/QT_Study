import os
import typing
import pathlib

# 부모 디렉토리
# 특정 확장자만 찾을 수 있는 옵션


class System:
    @staticmethod
    def get_files(parent_dir:pathlib.Path, pattern:typing.List[str])-> typing.List[pathlib.Path]:
        for f in parent_dir.glob('**/*'):
            if not f.is_file():
                continue
            if '*' in pattern:
                yield f
            else:
                if f.suffix in pattern:
                    yield f
    @staticmethod
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

    @staticmethod
    def get_files_recursion(dpath:str, pattern:typing.List[str], depth=0):
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
                lst += System.get_files_recursion(fullpath, pattern, depth + 1)
            else:
                if os.path.isfile(fullpath):
                    if '*' in pattern:
                        lst.append(fullpath)
                    else:
                        ext = f'.{fullpath.split(".")[-1]}'
                        if ext in pattern:
                            lst.append(fullpath)
        yield from lst


import logging
from PySide2 import QtGui
class LogHandler(logging.Handler):
    def __init__(self, out_stream=None):
        super(LogHandler, self).__init__()
        # log text msg format
        self.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] : %(message)s'))
        logging.getLogger().addHandler(self)
        # logging level
        logging.getLogger().setLevel(logging.DEBUG)
        self.__out_stream = out_stream
    def emit(self, record):
        msg = self.format(record)

        self.__out_stream.setPlainText(self.__out_stream.toPlainText() + msg + '\n')
        self.__out_stream.moveCursor(QtGui.QTextCursor.End)
    @staticmethod
    def log_msg(method=None, msg=''):
        if method is None:
            return
        if method.__name__ == 'info':
            new_msg = '<font color=#dddddd>{msg}</font>'.format(msg=msg)
        elif method.__name__ == 'debug':
            new_msg = '<font color=#23bcde>{msg}</font>'.format(msg=msg)
        elif method.__name__ == 'warning':
            new_msg = '<font color=#cc9900>{msg}</font>'.format(msg=msg)
        elif method.__name__ == 'error':
            new_msg = '<font color=#e32474>{msg}</font>'.format(msg=msg)
        elif method.__name__ == 'critical':
            new_msg = '<font color=#ff0000>{msg}</font>'.format(msg=msg)
        else:
            raise TypeError('[log method] unknown type')
        method(new_msg)
if __name__ == '__main__':
    pass

