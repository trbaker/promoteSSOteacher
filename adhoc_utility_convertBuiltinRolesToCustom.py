#script should convert ALL members of an org with builtin user or publisher roles to a custom roleid

from arcgis.gis import GIS
gis = GIS("home")

gis_users = gis.users.search(query='', max_users=5000, outside_org=0)

for user in gis_users:
    if (user.role == 'org_user') or (user.role == 'org_publisher'):
        print('Converting ' + user.username, user.role + " to the custom role")
        # update the roleid below with your target cutom role id
        user.update_role(role='npqoaTX2gNx8MYZC1')
