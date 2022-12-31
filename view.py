import os
import numpy as np
import matplotlib.pyplot as plt
from utils import plot_2d_pso, plot_3d_pso, make_gif_from_folder

ROOT = 'tmp/'
#filename = '_tmp.gif'
save = True

class SwarmView():
    def __init__(self, simuid, xmin, xmax, function):
        self.x = np.arange(xmin, xmax, 0.05)
        self.y = np.arange(xmin, xmax, 0.05)
        self.meshgrid = np.meshgrid(self.x, self.y)
        self.function = function
        self.root = ROOT + str(simuid) + os.sep
        self.filename_output = f"_tmp_{simuid}.gif"        
        self.tmp_dir = os.path.join(self.root, '_gifs')

    def plot_view(self, positions, iteration, title="", is_3d = False, save = True):
        fig = plt.figure()
        
        if save:
            if not os.path.exists(self.tmp_dir):
                os.makedirs(self.tmp_dir)

        if not is_3d:
            ax = fig.add_subplot(1, 1, 1)
            plot_2d_pso(self.meshgrid, self.function, positions, None, ax=ax)        
        else:
            ax = fig.add_subplot(1, 1, 1, projection='3d')  
            plot_3d_pso(self.meshgrid, self.function, positions, None, ax=ax)

        ax.set_title(f"it={iteration}  {title}")
        save_path = None if not save else os.path.join(self.tmp_dir, f'{iteration:05d}.png')
        
        if save_path is None:
            plt.show()
        else:
            plt.savefig(save_path)
            plt.close()

    def create_gif(self, remove_folder = False):
        make_gif_from_folder(self.tmp_dir, os.path.join(self.root, self.filename_output), remove_folder)

if __name__ == '__main__':

    sv = SwarmView("teste", -5, 5, lambda x, y: x**2 + y**2)

    sv.plot_view(np.array([[2, 2], [0, 0], [-1, 1]]), 0, is_3d=False, save = True)
    sv.create_gif()
