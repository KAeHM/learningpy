# vars
cmd = True
salaries = []
allowances = []
contributors = 0
minallowance = 0

#main

while cmd:
    salary = float(input('Type your salary: '))
    if salary <= 0:
        cmd = False
    else:
        salaries.append(salary)
        allowance = salary * 20 // 100
        if allowance <= 100:
            allowances.append(100)
            contributors += 1
            minallowance += 1
        else:
            allowances.append(allowance)
            contributors += 1
contributors = 0

# Contibutors Output 
print('-' * 30)
for c in salaries:
    for b in range(1):
        print(f'Contributiner: {contributors+1}')
        print(f'Salary: {salaries[contributors]}')
        print(f'Allowance: {allowances[contributors]}')
    print('-' * 30)
    contributors += 1

# Geral Output 
print(f'Have been processed {contributors} contributors.')
print(f'Amount spend with allowances: ${sum(allowances)}.')
print(f'Minimum pay for {minallowance} contributors.')
print(f'The most allowance pay: {max(allowances)}')
print()
