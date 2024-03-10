import os
import pathlib
import hou


final_dpath = '/Users/yeko/workspace/final'
hou.parm('/stage/cube_2/lopoutput').set(f"`$HIP`/geo/`$HIPNAME`/`$OS`/`$OS`_v002.usdnc")

src_path = pathlib.Path(hou.parm('/stage/cube_2/lopoutput').eval())
dst_final = pathlib.Path(final_dpath) / pathlib.Path('cube_2')

try:
    os.symlink(src_path, dst_final)
    print('link created successfully')
except FileExistsError:
    print('Destination already exists. No symbolic link created.')



