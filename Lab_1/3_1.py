'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
print(NAT.replace('Fast', 'Gigabit'))

MAC = 'AAAA:BBBB:CCCC'
print(MAC.replace(':', '.'))

CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
commands = CONFIG.strip().split()
vlans = commands[-1].split(',')
print(vlans)

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
commands1 = command1.strip().split()
commands2 = command2.strip().split()
vlan1 = set(commands1[-1].split(','))
vlan2 = set(commands2[-1].split(','))
print(vlan1.intersection(vlan2))

VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
print(sorted(set(VLANS)))

ospf_route = 'OSPF 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
route = ospf_route.strip().split()
ospf_route['Protocol'] = 'OSPF'
ospf_route['Prefix'] = '10.0.24.0/24'
ospf_route['AD/Metric'] = '[110/41]'
ospf_route['Next-Hop'] = '10.0.13.3'
ospf_route['Last update'] = '3d18h'
ospf_route['Outbound Interface'] = 'FastEthernet0/0'