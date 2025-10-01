# kdot-mustard
Blown away by the 2025 Super Bowl Halftime Show? Wondering how you can get more sweet, pungent, yellowish condiment-based goodness?

# Quick Start
Simply fire up ```kdot-mustard```,
```
pip install kdot-mustard
```

load up one of our three curated commands,
```python
from kdot_mustard import kdot, kdot_simple, kdot_example

kdot(src_path, target_path, loop, frames, duration) # for total control over what goes on the beat
kdot_simple(src_path) # fast and easy results to turn his TV off
kdot_example() # if you need a demonstration of syrup sandwiches and crime allowances
```

and you have your very own mustardized Mr. Morales jumpscare:
![boo!](src\kdot_mustard\img\bossman.gif)

# Documentation
## ```kdot```
Passable parameters to control your ```.gif```

```python
kdot(src_path, target_path, loop, frames, duration)
```
- ```src_path```: ```str```, path to image file to mustardize
- ```target_path```: ```str```, path to save the ```.gif``` file to
- ```loop```: ```int | None```, number of times to loop the ```.gif```, if ```None```, does not loop
- ```frames```: ```int```, number of frames in the ```.gif```
- ```duration```: ```int```, number of ms per frame

## ```kdot_simple```
Simpler function with just the ```src_path```

```python
kdot_simple(src_path)
```
- ```src_path```: ```str```, path to image file to mustardize

## ```kdot_example```
Example function that takes a test image to mustardize for demo purposes

```python
kdot_example()
```
