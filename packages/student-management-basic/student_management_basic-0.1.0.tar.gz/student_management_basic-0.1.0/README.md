# student_management

Tiny example package exposing simple student classes:
- `UndergraduateStudent`
- `GraduateStudent`
- `PhDStudent`

## Install
```bash
pip install student-management
```

## Usage

from student_management import UndergraduateStudent, GraduateStudent, PhDStudent

u = UndergraduateStudent("Alice", "U123")
g = GraduateStudent("Bob", "G456")
p = PhDStudent("Carol", "P789")

print(u.get_student_type())  # "Undergraduate Student"
print(g.get_student_type())  # "Graduate Student"
print(p.get_student_type())  # "PhD Student"