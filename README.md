# Swarm View

A simple way to print swarm agents' positions in 2D search space. 


![_tmp_teste](https://user-images.githubusercontent.com/276077/210286948-f9d0c028-1b42-4f6c-9453-b7258b860ca1.gif)
![_tmp_gsa_site](https://user-images.githubusercontent.com/276077/211828018-0a78257f-2681-4c1b-b441-1bf0394c25b8.gif)

Enabling 3d (is_3d = True) 
![_tmp_test](https://user-images.githubusercontent.com/276077/210287110-0f3423f1-3568-4afe-9e03-ba7d81cc572a.gif)


The project is based in [https://github.com/AxelThevenot/Particle_Swarm_Optimization](https://github.com/AxelThevenot/Particle_Swarm_Optimization)

## How to use ?
The simplest way to use it is adding as a submodule in your repository

```
git submodule add https://github.com/rodrigoclira/swarmview/ swarmview
```

After that you can import and create a _view.SwarmView_ object doing: 

```python
from swarmview.view import SwarmView
import math
import numpy as np

# Rastrigin 
func = lambda x, y: x ** 2 - 10 * np.cos(2 * math.pi * x) + y ** 2 - 10 * np.cos(2 * math.pi * y)

swarm_view = SwarmView(simuid = simulation_id, xmin = -5.12, xmax = 5.12, is_3d = False, function = func )
```

Lastly, you can use the _view.SwarmView_ object calling the _plot_view_ . The method will create a image using the current swarm state, based in _positions_ array. 

```python
 swarm_view.plot_view(positions = np.array(array), title = f"{self.best_fit} - IT =({self.best_fit_it}) W={self.curr_ai_pack}", iteration=iteration)
```

if you want to create a gif, you must use the _create_gif_ method from _SwarmView_ object. It will get all images and create a gif animation.

```python
swarm_view.create_gif()
```

All the files are created in "_./tmp_" folder.

## Example

There is a example in view.py 

```python
sv = SwarmView(simuid = "test", xmin = -5, xmax = 5, function = lambda x, y: x**2 + y**2, is_3d = False)

# call the method in a loop
sv.plot_view(positions = np.array([[2, 2], [2, 0], [-1, 1]]), iteration = 0, save = True)
sv.plot_view(positions = np.array([[1, 0], [1.2, 1], [-2, 1.5]]), iteration = 1, save = True)
sv.plot_view(positions = np.array([[0, 0], [1, 0], [1, 2]]), iteration = 2, save = True)


# if you want, create a gif with each iteration
sv.create_gif()

```

