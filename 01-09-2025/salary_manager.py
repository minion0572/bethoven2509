salaries = [1000,5000,6000]
search = 5000
print(salaries)
index = -1
I = 0
for salary in salaries:
    if salary == search:
        index = I
        break
    I +=  1
print(index)
salaries.remove(search)
print(salaries)