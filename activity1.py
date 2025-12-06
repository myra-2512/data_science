import numpy as np

data_type=[('name','S15',),('class',int),('height',float)]
students_details=[('Jacob',5,134.8),('Emma',5,140.3),('Michael',6,152.7),('Sofia',5,146.2)]

students=np.array(students_details,dtype=data_type)

print("Original array:")
print(students)
print("Sort by height:")
print(np.sort(students,order='height'))