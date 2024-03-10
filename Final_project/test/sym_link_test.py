import os
import pathlib

src = pathlib.Path('/Users/yeko/Desktop/netflix_TD/Final_project/test/db_test.py')
dst = pathlib.Path('/Users/yeko/Desktop/netflix_TD/Final_project/test/dst(sym).py')

os.symlink(src, dst)
