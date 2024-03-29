import os
import numpy as np
import matplotlib.pyplot as plt
from .utils import plot_2d_pso, plot_3d_pso, make_gif_from_folder

ROOT = 'tmp/'
#filename = '_tmp.gif'
save = True

class Grid():
    def __init__(self, xmin, xmax, interval, function):
        self.function = function
        self.x = np.arange(xmin, xmax, interval)
        self.y = np.arange(xmin, xmax, interval)
        self.meshgrid = np.meshgrid(self.x, self.y, copy = False)
        self.X_grid, self.Y_grid = self.meshgrid
        self.Z_grid = function(self.X_grid, self.Y_grid)
        self.X_grid_max = np.max(self.X_grid)
        self.Y_grid_max = np.max(self.Y_grid)
        self.X_grid_min = np.min(self.X_grid)
        self.Y_grid_min = np.min(self.Y_grid)
        self.Z_grid_max = np.max(self.Z_grid)

class SwarmView():
    def __init__(self, simuid, xmin, xmax, function, is_3d = False, enable = True):
        
        interval = 0.05 
        if abs(xmin) + abs(xmax) > 30:
            interval = 1 # decreasing meshgrid in high search spaces

        #self.function = function
        self.grid = Grid(xmin, xmax, interval, function)        
        self.root = ROOT + str(simuid) + os.sep
        self.filename_output = f"_tmp_{simuid}.gif"        
        self.tmp_dir = os.path.join(self.root, '_gifs')
        self.is_3d = is_3d
        self.projection = None
        
        if self.is_3d:
            self.projection = '3d'
        
        self.enable = enable

    def plot_view(self, positions, iteration, title="", save = True):

        if not self.enable:
            return None

        fig = plt.figure()
        
        if save:
            if not os.path.exists(self.tmp_dir):
                os.makedirs(self.tmp_dir)
        
        ax = fig.add_subplot(1, 1, 1, projection=self.projection)  

        if not self.is_3d:
            plot_2d_pso(self.grid, positions, None, ax=ax)        
        else:            
            plot_3d_pso(self.grid, positions, None, ax=ax)

        ax.set_title(f"it={iteration}  {title}")
        save_path = None if not save else os.path.join(self.tmp_dir, f'{iteration:05d}.png')
        
        if save_path is None:
            plt.show()
        else:
            plt.savefig(save_path)
            plt.close()

    def create_gif(self, remove_folder = False):
        if self.enable:
            make_gif_from_folder(self.tmp_dir, os.path.join(self.root, self.filename_output), remove_folder)

if __name__ == '__main__':

    sv = SwarmView(simuid = "test", xmin = -5, xmax = 5, function = lambda x, y: x**2 + y**2, is_3d = True)

    sv.plot_view(positions = np.array([[2, 2], [2, 0], [-1, 1]]), iteration = 0, save = True)
    sv.plot_view(positions = np.array([[1, 0], [1.2, 1], [-2, 1.5]]), iteration = 1, save = True)
    sv.plot_view(positions = np.array([[0, 0], [1, 0], [1, 2]]), iteration = 2, save = True)
    
    sv.create_gif()
