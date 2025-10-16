+------------------+        +------------------+
|    Teacher       |        |    Student       |
|------------------|        |------------------|
| - id: int        |        | - id: int        |
| - full_name: str |        | - full_name: str |
| - email: str     |        | - grade: int     |
|------------------|        |------------------|
| +assign_course() |        | +enroll(course)  |
+--------+---------+        +--------+---------+
         |                           |
         | 1                        *|
         |                           |
         v                           v
+------------------+        +------------------+
|    Course        |<------>|   Enrollment     |
|------------------|        |------------------|
| - code: str      |        | - course: Course |
| - title: str     |        | - student:Student|
| - capacity: int  |        +------------------+
| - teacher:Teacher|        
| - students: list |
|------------------|
| +add_student()   |
| +remove_student()|
| +is_full()       |
+------------------+
