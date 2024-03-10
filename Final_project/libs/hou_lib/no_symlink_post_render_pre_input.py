import os
import pathlib
import hou


final_dpath = '/Users/yeko/workspace/final'
hou.parm('/stage/input/lopoutput').set(f"`$HIP`/geo/`$HIPNAME`/`$OS`/`$OS`_version.usdnc")

src_path = pathlib.Path(hou.parm('/stage/input/lopoutput').eval())
dst_final = pathlib.Path(final_dpath) / pathlib.Path('input')

try:
    os.symlink(src_path, dst_final)
    print('link created successfully')
except FileExistsError:
    print('Destination already exists. No symbolic link created.')



