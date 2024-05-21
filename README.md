## 📌 Description
for each cell on a grid, evaluate a expression on all neighbors
## 📸 Screenshot
![screenshot1](https://github.com/pemn/assets/blob/main/vtk_cell_neighbors1.png?raw=true)
## 📝 Parameters
name|optional|description
---|---|------
data|❎|grid with original data
distance|❎|how many cells to walk away from center block
||0|immediate neighbors (max of 6)
||1|neighbors within a distance of 1 cells (max of 26)
||2|neighbors within a distance of 2 cells (max of 124)
||3|…
fields|☑️|path to save modified grid|
display||show results in a 3d voxel chart
## 📓 Notes
 - When distance is `== 0` the builtin function cell_neighbors() is used. otherwise a slower custom algorithm is used.
 - on distance `>= 1` the diagonal blocks will be included
## 📚 Examples
![screenshot2](https://github.com/pemn/assets/blob/main/vtk_cell_neighbors2.png?raw=true)  
## 🧊 Test Data
[grid_16_12_8_100.vtk](https://github.com/pemn/assets/raw/main/grid_16_12_8_100.vtk)  
[std_voxel_0.vtk](https://github.com/pemn/assets/raw/main/std_voxel_0.vtk)  
## 🧩 Compatibility
distribution|status
---|---
![winpython_icon](https://github.com/pemn/assets/blob/main/winpython_icon.png?raw=true)|✔
![vulcan_icon](https://github.com/pemn/assets/blob/main/vulcan_icon.png?raw=true)|❌
![anaconda_icon](https://github.com/pemn/assets/blob/main/anaconda_icon.png?raw=true)|✔
## 🙋 Support
Any question or problem contact:
 - paulo.ernesto
## 💎 License
Apache 2.0
Copyright ![vale_logo_only](https://github.com/pemn/assets/blob/main/vale_logo_only_r.svg?raw=true) Vale 2024
