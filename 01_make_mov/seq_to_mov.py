# standard library modules
import os
import pathlib
import re
import sys

# third-party library modules
import cv2
import imageio
from tqdm import tqdm
import pyseq

# local project modules
from PySide2 import QtGui, QtWidgets, QtCore
import importlib

# gui modules
import seq_to_mov_ui

importlib.reload(seq_to_mov_ui)

"""
이미지 시퀀스를 Gif로 만들자!
(mov로 하려니 codec error가 자꾸 나는 바람에 gif로 변경)

- 이미지 파일 경로 선택
- 이미지를 읽어와서 pyseq로 정리 및 리스트 나열
- 리스트 이미지를 누르면 이미지 preview
- convert mov 누르면 저장경로 선택 및 gif 생성됌 -> **mp4로 변경하도록 codec에 대해 더 공부하기

(추가하고 싶은 것)
- mov를 컨버트 성공하게 되면, gif는 pyseq 프리뷰처럼 뜨는 걸로 변경해보기
- OpenEXR도 시도

"""


class SeqToMov(QtWidgets.QMainWindow, seq_to_mov_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.filename = list()  # 이미지 파일들을 긁어와서 저장하기 위한 리스트
        self.sub_filename = list()  # 다른 이미지 그룹을 선택할 때, detail list가 초기화될 수 있도록 옮겨놓기 위한 용도

        self.file_gen = list()

        self.zip_f = None  # 이미지리스트를 pyseq.Sequence 하여 얻은 결과값 저장하기 위한 변수


        self.label__img_show.setScaledContents(True)  # 이미지 프리뷰와 레이블 사이즈 맞추기

        self.dpath = None  # 파일 오픈 경로
        self.signal_func()

    def signal_func(self):
        self.pushButton__open_dir.clicked.connect(self.open_dir)
        self.listWidget__seq_grp_lst.currentItemChanged.connect(self.show_lst)
        self.listWidget__seq_detail_lst.currentItemChanged.connect(self.show_preview)

    def show_lst(self, idx: QtWidgets.QListWidgetItem):
        text_idx = re.sub(r'_\d+-\d+\.[a-z]+', '', idx.text())
        print(text_idx)

        # TODO : self.filename이 addItems가 되는건 맞는데,
        #   seq_grp_lst의 item을 누를 때마다 self.filename의 리스트 내용이 바뀌어야 한단말이지?
        #

        self.listWidget__seq_detail_lst.addItems(self.filename)
        self.lineEdit__select_grp.setText(f'{text_idx}.gif')

    def show_preview(self, idx: QtWidgets.QListWidgetItem):
        ipath = f'{self.dpath}/{idx.text()}'
        self.label__img_show.setPixmap(QtGui.QPixmap(ipath))

    def open_dir(self):
        dpath = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Open Dir','/Users/yeko/Desktop/netflix_TD/self_study/qt_study/01_make_mov')
        self.lineEdit__dirpath.setText(dpath)
        self.read_dir()

    def read_dir(self):
        self.dpath = pathlib.Path(self.lineEdit__dirpath.text())
        # print(dpath.exists())

        # TODO: self.filename은 결국엔 dpath 즉, lineEdit에 적힌 text의 경로 영향을 받는이다.
        #  즉, 경로를 grp list에게 직접 저장해주지 않으면 detail list는 grp list의 영향을 절대 받지 못한다.

        # TODO: 아니면 선택을 해야해. open dir로 경로를 선택했을 때, 그 경로 안에있는 파일만 나오게 한다던가.
        #  그렇게 되면 경로가 바뀔 때 filename은 문제가 없어,
        #  ------대신 파일 안에 다양한 확장자를 분리할 함수를 구현해야 함.

        self.file_gen = self.dpath.glob('*.exr')
        self.file_gen = list(self.file_gen) + list(self.dpath.glob('*.png'))
        self.make_file_lst()
        self.make_file_zip()

    # TODO: seq grp lst가 dic-key가 되고, seq detail lst가 value가 되도록 하면,
    #  lst를 grp을 눌렀을 때 detail lst가 나올 수 잇을까?

    def make_file_lst(self):
        self.filename = list(map(lambda x: x.name, self.file_gen))
        self.filename = sorted(self.filename, reverse=False)
        # print(self.filename)

    def make_file_zip(self):
        self.zip_f = pyseq.Sequence(self.filename)
        # self.zip_f = self.zip_f.format("%l, %f")
        # HACK:
        # if not str(self.zip_f) in self.listWidget__seq_grp_lst.items():
        self.listWidget__seq_grp_lst.addItem(str(self.zip_f))
        # else:
        #     pass
        print(self.zip_f)
        self.pushButton__convert.clicked.connect(self.convert_png_to_mov)

    # re group 연습용 / 전체 코드에 영향을 미치고 있지 않음
    # TODO: 이거는 한 폴더 안에 다양한 형태의 확장자가 있어서 분리를 해야할 경우 필요할 것 같음
    def find_pattern(self):
        png_pattern = re.compile(r'(?P<name>[A-Za-z]+&[A-Z])_(?P<obj>[A-Za-z]{4})_(?P<frange>\d{4})\.png', re.DOTALL)
        for i in self.filename:
            match = png_pattern.search(i)
            a = match.group('obj')
            print(a)

    def convert_png_to_mov(self):  # mov -> gif
        spath = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Save Dir', '/Users/yeko/Desktop/netflix_TD/self_study/qt_study/')
        images = []
        for i, v in enumerate(self.filename):  # enumerate 는 (index, value) tuple 형식으로 반환
            images.append(f'{self.dpath}/{v}')
        print(images)
        frame = cv2.imread(os.path.join(self.dpath, images[0]))
        out = f'{spath}/{self.lineEdit__select_grp.text()}'
        height, width, layers = frame.shape  # shape => (height, width, channels(채널수: 색상채널)) tuple로 반환

        # video = cv2.VideoWriter(out, cv2.VideoWriter_fourcc(*'mp4v'), 24, (height, width))
        # for image in tqdm(images, desc="Creating Video", unit="image"):
        #     video.write(cv2.imread(os.path.join(self.dpath, image)))

        #
        frames = []
        for image in tqdm(images, desc="Creating GIF", unit="image"):
            frames.append(imageio.imread(os.path.join(self.dpath, image)))
        imageio.mimsave(out, frames, duration=1/24)
        # cv2.destroyAllWindows()
        # video.release()
        tqdm.write('Done')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    s = SeqToMov()
    s.show()  # 아예 _init_ 안에 self.show()로 써줘도 된다고 함.
    sys.exit(app.exec_())
