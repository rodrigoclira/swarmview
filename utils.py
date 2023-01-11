import os
import glob
import shutil

import numpy as np
from PIL import Image

import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter


# utils.py is a module downloaded from https://towardsdatascience.com/particle-swarm-optimization-visually-explained-46289eeb2e14
# with some modifications


plt.rcParams['figure.figsize'] = [12, 6] # default = [6.0, 4.0]
plt.rcParams['figure.dpi']     = 100     # default = 72.0
plt.rcParams['font.size']      = 7.5     # default = 10.0

cmap = cm.colors.LinearSegmentedColormap.from_list('Custom',
                                                   [(0, '#2f9599'),
                                                    (0.45, '#eee'),
                                                    (1, '#8800ff')], N=256)


def make_gif_from_folder(folder, out_file_path, remove_folder=True):
    files = os.path.join(folder, '*.png')
    img, *imgs = [Image.open(f) for f in sorted(glob.glob(files))]
    img.save(fp=out_file_path, format='GIF', append_images=imgs,
             save_all=True, duration=200, loop=0)

    if remove_folder:
        shutil.rmtree(folder, ignore_errors=True)


def plot_2d_pso(grid, positions=None, velocity=None, normalize=True, color='#000', ax=None):

    # get coordinates and velocity arrays
    if positions is not None:
        X, Y = positions.swapaxes(0, 1)
        if velocity is not None:
            U, V = velocity.swapaxes(0, 1)
            if normalize:
                N = np.sqrt(U**2+V**2)
                U, V = U/N, V/N

    # create new ax if None
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1, projection='3d')

    # add contours and contours lines
    ax.contour(grid.X_grid, grid.Y_grid, grid.Z_grid, levels=30, linewidths=0.5, colors='#999')
    cntr = ax.contourf(grid.X_grid, grid.Y_grid, grid.Z_grid, levels=30, cmap='viridis', alpha=0.7)
    #plt.colorbar(cntr, ax=ax, shrink=0.9)
    if positions is not None:
        ax.scatter(X, Y, color=color)
        if velocity is not None:
            ax.quiver(X, Y, U, V, color=color, headwidth=2, headlength=2, width=5e-3)

    # add labels and set equal aspect ratio
    ax.set_xlabel('D0')
    ax.set_ylabel('D1')
    ax.set_xlim(grid.X_grid_min, grid.X_grid_max)
    ax.set_ylim(grid.Y_grid_min, grid.Y_grid_max)
    ax.set_aspect(aspect='equal')


def plot_3d_pso(grid, positions=None, velocity=None, normalize=True, color='#000', ax=None):
    # get coordinates and velocity arrays
    if positions is not None:
        X, Y = positions.swapaxes(0, 1)
        Z = grid.function(X, Y)
        if velocity is not None:
            U, V = velocity.swapaxes(0, 1)
            W = function(X + U, Y + V) - Z

    # create new ax if None
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1, projection='3d')

    # Plot the surface.
    surf = ax.plot_surface(grid.X_grid, grid.Y_grid, grid.Z_grid, cmap="viridis",
                           linewidth=0, antialiased=True, alpha=0.7)
    ax.contour(grid.X_grid, grid.Y_grid, grid.Z_grid, zdir='z', offset=0, levels=30, cmap="viridis")
    if positions is not None:
        ax.scatter(X, Y, Z, color=color, depthshade=True)
        if velocity is not None:
            ax.quiver(X, Y, Z, U, V, W, color=color, arrow_length_ratio=0., normalize=normalize)

    len_space = 10
    # Customize the axis
    max_z = (grid.Z_grid_max // len_space + 1).astype(int) * len_space
    ax.set_xlim3d(grid.X_grid_min, grid.X_grid_max)
    ax.set_ylim3d(grid.Y_grid_min, grid.Y_grid_max)
    ax.set_zlim3d(0, max_z)
    ax.zaxis.set_major_locator(LinearLocator(max_z // len_space + 1))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    # Rmove fills and set labels
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.set_xlabel('D0')
    ax.set_ylabel('D1')
    ax.set_zlabel('f(D0, D1)')

    # Add a color bar which maps values to colors.
    # fig.colorbar(surf)

if __name__ == '__main__':
    pass