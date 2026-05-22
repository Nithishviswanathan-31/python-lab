## Exp 05 — Set and dictionary operations

Programs demonstrating Python set and dictionary operations on real-world models.

| File | Description |
|------|-------------|
| 05a_automobile_subset_components.py | Set operations on automobile components — union, intersection, difference, subset check |
| 05b_civil_structure_directory.py | Dictionary operations on civil structure elements — add, update, delete, display |

## Concepts used
- Set creation and operations: union (|), intersection (&), difference (-), issubset()
- Dictionary creation, key-value access, update(), pop(), items(), keys(), values()
- Iterating over sets and dictionaries

## Sample output

**05a — Automobile subsets**
```
Set A (Car)    : {'Engine', 'Tyres', 'Brakes', 'Battery'}
Set B (Truck)  : {'Engine', 'Tyres', 'Axle', 'Chassis'}
Union          : {'Engine', 'Tyres', 'Brakes', 'Battery', 'Axle', 'Chassis'}
Intersection   : {'Engine', 'Tyres'}
Difference A-B : {'Brakes', 'Battery'}
```

**05b — Civil structure directory**
```
Structure  : {'Foundation': 'RCC', 'Walls': 'Brick', 'Roof': 'Concrete'}
After add  : {'Foundation': 'RCC', 'Walls': 'Brick', 'Roof': 'Concrete', 'Doors': 'Teak'}
After update: {'Foundation': 'RCC', 'Walls': 'AAC Block', 'Roof': 'Concrete', 'Doors': 'Teak'}
```