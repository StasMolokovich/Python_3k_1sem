'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
a = input('Enter ip address in format 10.0.1.1:')

ip = int(a.split('.')[0])
if ip > 0 and ip <=127:
    print(('ip address {} class A,this unicast').format(a))
elif ip > 127 and ip <= 191:
    print(('ip address {} class B,this unicast').format(a))
elif ip > 191 and ip <= 223:
     print(('ip address {} class C,this unicast').format(a))
elif ip > 223 and ip <= 239:
    print(('ip address{} class D,this multicast').format(a))
elif a == '255.255.255.255':
    print(('local broadcast').format(a))
elif a == '0.0.0.0':
    print(('unassigned').format(a))
else:
    print ('unused')