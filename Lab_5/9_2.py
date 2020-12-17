'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def return_match(file_name, reg):
    input_file = open(file_name, "r")
    file_lines = input_file.readlines()
    result_lines = []
    for line in file_lines:
        match = re.search(reg, line)
        if match:
            result_lines.append(match[0])


return_match("sh_ip_int_br.txt", "d+\.d+\.d+\.d+\")