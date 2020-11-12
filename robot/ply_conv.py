import numpy as np
from plyfile import PlyData, PlyElement
plydata = PlyData.read('model1.ply')
el = PlyData([plydata.elements[0],plydata.elements[1]],text=True)
#PlyData([el], text=True).write('some_ascii.ply')
test_file = './some_ascii.ply'
with open(test_file,'wb') as f:
    el.write(f)