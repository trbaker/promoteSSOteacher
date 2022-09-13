from arcgis.gis import GIS
gis = GIS("home")

gis_users = gis.users.search(query='', max_users=5000, outside_org=0)

for user in gis_users:
    if (user.role == 'org_user') or (user.role == 'org_publisher'):
        print(user.username, user.role)
