#!python
# for each cell on a grid, evaluate a expresion on all neighbors
# distance: distance in regular cells to consider neighbors

'''
usage: $0 data*vtk,csv distance=1,2,3 fields#field:data#operation=count,major,sum,mean,min,max output*vtk,csv
'''
import sys, os.path, re
import numpy as np
import pandas as pd

# import modules from a pyz (zip) file with same name as scripts
sys.path.insert(0, os.path.splitext(sys.argv[0])[0] + '.pyz')
from _gui import usage_gui, commalist, log

from pd_vtk import vtk_Voxel, pv_save, vtk_array_ijk, vtk_mesh_info, vtk_reshape_a3d

def major(_):
  return pd.Series.value_counts(_).idxmax()

def np_calc_neighbors(s, gcn, operation):
  r = None
  f = None
  if operation == 'major':
    f = major
    r = np.full(s.size, '', np.object_)
  else:
    r = np.zeros(s.size)
    if operation == 'count':
      f = np.size
    else:
      f = eval(f'np.nan{operation}')

  for i in range(s.size):
    r[i] = f(np.take(s, gcn[i]))

  return r

def vtk_cell_neighbors(data, distance, fields, output):  
  grid = vtk_Voxel.factory(data)
  fields = commalist(fields)
  if grid is None:
    print("data is not a schema or a grid")
    return 1
  gcn = grid.find_neighbors()
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
    log(field, operation, output_field)
    s = grid.get_array(field, 'cell')

    grid.cell_data[output_field] = np_calc_neighbors(s, gcn, operation)
    
    #for i in range(grid.n_cells):
      #print(i, *gcn[i])
      # print(*grid.cell_neighbors(i,'points'))
      # print(*grid.cell_neighbors(i,'faces'))
      # print(*grid.cell_neighbors(i,'edges'))
  print(vtk_mesh_info(grid))
  if output:
    pv_save(grid, output)
  log("# vtk_cell_neighbors finished")

main = vtk_cell_neighbors

if __name__=="__main__":
  usage_gui(__doc__)
