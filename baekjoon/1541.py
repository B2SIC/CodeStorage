exp = input()
exp_list = list(exp)

clean_exp = ""
num_exp = ""
for item in exp_list:
    if item == "+" or item == "-":
        clean_exp += str(int(num_exp)) + item
        num_exp = ""
    else:
        num_exp += item

clean_exp += str(int(num_exp))

if '-' in clean_exp:
    clean_exp_list = clean_exp.split('-')

    exp = ""
    for item in clean_exp_list:
        exp += "(" + item + ")-"
    exp = exp[:-1]
    result = eval(exp)
else:
    result = eval(clean_exp)

print(result)
