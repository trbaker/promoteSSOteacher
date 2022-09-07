from arcgis.gis import GIS

gis = GIS("home")
roles=gis.users.roles.all(max_roles=50)
for role in roles:
    print(role.name, ' ::: ', role.role_id)
