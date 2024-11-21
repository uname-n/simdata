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

print(sim.int.create(values=[1, 2, 2, 3, 3, 3, 4, 4, 4, 4])) 
# func='int' mean=3.0 std=1.0 min=1.0 max=4.0 precision=3
```

Create from existing data. Ex. [Loan Approval Prediction](https://www.kaggle.com/competitions/playground-series-s4e10/data?select=test.csv)
```python
from simdata import simd, sim
from polars import read_csv

data = read_csv("sample.csv")
s = simd(
    person_age=sim.int.create(values=data["person_age"].to_list()),
    person_income=sim.int.create(values=data["person_income"].to_list()),
    person_home_ownership=sim.choice.create(values=data["person_home_ownership"].to_list()),
    person_emp_length=sim.float.create(values=data["person_emp_length"].to_list(), precision=1),
    loan_intent=sim.choice.create(values=data["loan_intent"].to_list()),
    loan_grade=sim.choice.create(values=data["loan_grade"].to_list()),
    loan_amnt=sim.int.create(values=data["loan_amnt"].to_list()),
    loan_int_rate=sim.float.create(values=data["loan_int_rate"].to_list(), precision=2),
    loan_percent_income=sim.float.create(values=data["loan_percent_income"].to_list(), precision=2),
    cb_person_default_on_file=sim.choice.create(values=data["cb_person_default_on_file"].to_list()),
    cb_person_cred_hist_length=sim.int.create(values=data["cb_person_cred_hist_length"].to_list()),
)
print(s.simulate())
# {
#     "cb_person_cred_hist_length": 7,
#     "cb_person_default_on_file": "N",
#     "loan_amnt": 9150,
#     "loan_grade": "C",
#     "loan_int_rate": 8.45,
#     "loan_intent": "VENTURE",
#     "loan_percent_income": 0.23,
#     "person_age": 30,
#     "person_emp_length": 1.0,
#     "person_home_ownership": "RENT",
#     "person_income": 51526
# }
```

## Pydantic
Built with pydantic, easily load and dump sims.
```python
model = s.model_dump_json(indent=4)
model = simd.model_validate_json(model)

model.simulate()
```