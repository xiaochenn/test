

# a = list()
# for i in range(1,100):
#     flag = 0
#     for j in range(2,i):
#         if (i % j == 0):
#             flag = 1
#     if (flag == 0):
#         a.append(i)
# print(a)

# j = sum(X[0] + X[i] + 3 * X[i+1] for i in range(10) if i % 2 == 1)
# for y in range(10):
#     if ((y + j) % 10 == 0):
#         X.append(y)

code_table = {"S":"...", "O":"---"}
S = "SOS"
p = " "
for i in S:
    p = p + code_table[i] + " "
print(p)
            

