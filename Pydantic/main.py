from pydantic_models import Employee
from uuid import uuid4
from datetime import timedelta, date

employee = Employee(
    employee_id=uuid4(),
    name='Ahliddin',
    email='ahliddin@example.com',
    birth_date=date.today() - timedelta(365 * 17),
    compensation=1235,
    department='IT',
    elected_benefits=True
)
a = employee.model_dump()
b = employee.model_dump_json()
print(type(a), a)
print(type(b), b)
print(employee.model_json_schema())