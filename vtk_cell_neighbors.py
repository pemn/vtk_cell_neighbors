#!python
# for each cell on a grid, evaluate a expresion on all neighbors
# distance: distance in regular cells to consider neighbors
# 0 mean immediate neighbors (max of 6 neighbors)
# 1 means a distance of 1 cell (max of 26 neighbors)

'''
usage: $0 data*vtk,csv distance=0,1,2,3 fields#field:data#operation=count,major,sum,mean,min,max output*vtk,csv display@
'''
import sys, os.path, re
import numpy as np
import pandas as pd

# import modules from a pyz (zip) file with same name as scripts
sys.path.insert(0, os.path.splitext(sys.argv[0])[0] + '.pyz')
from _gui import usage_gui, commalist, log

from pd_vtk import vtk_Voxel, pv_save, vtk_array_ijk, vtk_mesh_info, vtk_reshape_a3d, vtk_plot_grid_vars

def major(_):
  return 

def np_calc_neighbors(s, gcn, operation):
  r = None
  if operation == 'major':
    r = np.full(s.size, '', np.object_)
    for i in range(s.size):
      r[i] = pd.Series.value_counts(np.take(s, gcn[i])).idxmax()
  elif operation == 'count':
    r = np.fromiter(map(len, gcn), np.int_)
  else:
    r = np.zeros(s.size)
    f = eval(f'np.nan{operation}')

    for i in range(s.size):
      r[i] = f(np.take(s, gcn[i]))

  return r

def vtk_cell_neighbors(data, distance, fields, output, display):  
  grid = vtk_Voxel.factory(data)
  fields = commalist(fields)
  if grid is None:
    print("data is not a schema or a grid")
    return 1
  if not distance:
    distance = 1
  else:
    distance = int(distance)

  gcn = grid.find_neighbors(distance)
  vl = []
  for field, operation in fields:
    if not field:
      field = 'neighbor'
      operation = 'count'
    elif field not in grid.array_names:
      log('field not found:',field)
      continue
    elif not operation:
      operation = 'count'

    output_field = field + '_' + operation
    if field not in vl:
      vl.append(field)
    vl.append(output_field)
    log(field, operation, output_field)
    grid.cell_data[output_field] = np_calc_neighbors(grid.get_array(field, 'cell'), gcn, operation)

  print(vtk_mesh_info(grid))
  if output:
    pv_save(grid, output)
  if int(display):
    vtk_plot_grid_vars(grid, vl)
  log("# vtk_cell_neighbors finished")

main = vtk_cell_neighbors

if __name__=="__main__":
  usage_gui(__doc__)
