# Swarm View

A simple class to print swarm agents in 2D search space. 
It is based in [https://github.com/AxelThevenot/Particle_Swarm_Optimization](https://github.com/AxelThevenot/Particle_Swarm_Optimization)

## How to use ?
The simplest way to use it is adding as a submodule in your repository

```
git submodule add https://github.com/rodrigoclira/swarmview/ swarmview
```

After that you can import and create a _view.SwarmView_ object doing: 

```python
from swarmview.view import SwarmView
# Rastrigin 
func = lambda x, y: x ** 2 - 10 * np.cos(2 * math.pi * x) + y ** 2 - 10 * np.cos(2 * math.pi * y)

swarm_view = SwarmView(simuid = simulation_id, xmin = -5.12, xmax = 5.12, is_3d = False, function = func )
```

finally, you can use the _view.SwarmView_ object calling the _plot_view_

```python
 sv.plot_view(positions= np.array(array), title=f"{self.best_fit} - IT=({self.best_fit_it}) W={self.curr_ai_pack}", iteration=f"{iteration}")
```

if you want to create a gif, you can use the _create_gif_ method from _SwarmView_ object

```python
swarm_view.create_gif()
```

## Example

There is a example in view.py 

```python
sv = SwarmView(simuid = "teste", xmin = -5, xmax = 5, function = lambda x, y: x**2 + y**2, is_3d=False)

sv.plot_view(np.array([[2, 2], [0, 0], [-1, 1]]), 0, save = True)
sv.plot_view(np.array([[2, 0], [1, 1], [-1, 2]]), 1, save = True)

sv.create_gif()

```

