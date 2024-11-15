# simdata

**simdata** is a data simulation tool.

## Installation
To install **simdata**, run the following command:
```bash
pip install simdata
```

## Quick Start
```python
from simdata import simd, sim

# sim.seed(42)

s = simd(
    a=sim.int(mean=50, std=10, min=0, max=100),
    b=sim.float(mean=0.5, std=0.1, min=0, max=1, precision=2),
    c=sim.int(mean=75, std=10, min=0, max=100),
    d=sim.choice(choices=["A","B","C","D"], weights=[25,25,25,25]),
    e=sim.literal(value="edward"),
)

print(s.simulate())
# {'a': 59, 'b': 0.46, 'c': 86, 'd': 'A', 'e': 'edward'}
```

## Pydantic
Built with pydantic, easily load and dump sims.
```python
s = s.model_dump_json(indent=4)
s = simd.model_validate_json(model)

s.simulate()
```