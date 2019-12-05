'''
用for循环计算1-100的和，偶数和，奇数和
'''
evenTotal = 0
oddTotal = 0
total = 0
for x in range(1,101):
    total = total + x
    if x%2 == 0:
        evenTotal += x
    else:
        oddTotal += x
result = '结果：总和={0},奇数和={1},偶数和={2}'
print(result.format(total,oddTotal,evenTotal))
