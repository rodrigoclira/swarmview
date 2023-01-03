# Swarm View

The simplest way to use it is adding as a submodule in your repository

```
git submodule add https://github.com/rodrigoclira/swarmview/ swarmview
```

After that you can import and create a view.SwarmView object doing: 

```python
from swarmview.view import SwarmView
# Rastrigin 
func = lambda x, y: x ** 2 - 10 * np.cos(2 * math.pi * x) + y ** 2 - 10 * np.cos(2 * math.pi * y)

swarm_view = SwarmView(simuid = simulation_id, xmin = -5.12, xmax = 5.12, is_3d = False, function = func )
```

finally, you can use the swarmview object calling the plot_view

```python
 sv.plot_view(positions= np.array(array), title=f"{self.best_fit} - IT=({self.best_fit_it}) W={self.curr_ai_pack}", iteration=f"{iteration}")
```

if you want to create a gif, you can use the create_gif method from SwarmView object

```
swarm_view.create_gif()
```

