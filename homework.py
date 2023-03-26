import re

def read_file(filepath):                           #读文件模块
    with open(filepath,'r',encoding="utf-8") as f:
        lines = f.readlines()
        return lines

def code_analyze(lines):                            #代码分析模块
    total_lines = 0                 #总行数
    comment_lines = 0               #评论行数
    blank_lines = 0                 #空白行数
    code_lines  = 0                 #代码行数
    code_length = 0                 #代码长度
    if_num = 0                      #if数
    for_num = 0                     #for数
    while_num = 0                   #while数
    try_num = 0                     #try数
    max_indent_level = 0            #最大代码缩进层级
    func_lines_num = []             #函数代码数量
    func_num = 0                    #函数数量
    var_name = []                   #变量名列表

    for line in lines:          
        total_lines += 1            #获取总行数
        line.strip()                #删掉多余空格
        if re.search('^$',line):                #累计空行
            blank_lines += 1
            continue
        if re.search('^#',line):    #累计注释行
            comment_lines += 1
            continue
        
        code_lines += 1             #累计代码行
        code_length += len(line)    #累计代码长度

        indent_level = line.count('    ')
        if indent_level > max_indent_level:
            max_indent_level = indent_level
        
        if re.search('^for',line):
            for_num += 1
        elif re.search('^if',line):
            if_num += 1
        elif re.search('^while',line):
            while_num += 1
        elif re.search('^try',line):
            try_num += 1

        if re.search('^def.*:$',line):
            func_lines_num.append(0)
            func_num += 1
        if func_num > 0:
            func_lines_num[-1] += 1
        
        var_name = re.findall('\\b[a-zA-Z]\\w*\\b',line)
        var_name.remove('for','while','if','try','elif','else','in')
    if func_num > 0:
        avg_func_line_num = sum(func_lines_num) / func_num
    else:
        avg_func_line_num = 0
    if code_lines > 0:
        avg_code_length = code_length / code_lines
        var_name_length = sum([len(var) for var in var_name]) / len(var_name)
    result = {
    'total_lines': total_lines,
    'comment_lines': comment_lines,
    'blank_lines': blank_lines,
    'code_lines': code_lines,
    'avg_code_length': avg_code_length,
    'max_indent_level': max_indent_level,
    'if_num': if_num,
    'for_num': for_num,
    'while_num': while_num,
    'try_num': try_num,
    'func_num': func_num,
    'avg_func_line_num': avg_func_line_num,
    'var_name': var_name,
    'var_name_length': var_name_length,
    }

    return result
    

if __name__ == '__main__':
    lines = read_file('leeson2.py')
    result = code_analyze('lines')
    for key in result:
        print(result[key])
