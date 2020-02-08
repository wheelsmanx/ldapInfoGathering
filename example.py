import ldap3
from ldap3 import Server, Connection, ALL
server = Server('192.168.1.45', get_info=ALL)
conn = Connection(server, 'cn=admin,dc=hagerty,dc=local', '<password>', auto_bind=True)
conn.search('dc=hagerty,dc=local', '(objectclass=person)')
print(conn.entries)



# define the server
s = Server('192.168.1.45', get_info=ALL)  # define an unsecure LDAP server, requesting info on DSE and schema

# define the connection
c = Connection(s, user='cn=walrus,cn=firstGroup,dc=hagerty,dc=local', password='walrus')

# perform the Bind operation
if not c.bind():
    print('error in bind', c.result)
else:
    print("Success.")
