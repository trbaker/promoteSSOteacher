# Python uses pound signs to indicate comments.  There are four actions required below, indicated in comments leading with 1,2, or 3.
# In Python, spaces and/or tabs are very important. Be careful to not lose tabs.
# Create a new standard Notebook in ArcGIS Online and add this entire script to a single code block. Customize as above. Save it. Run it.
# ArcGIS Online Notebooks can also be scheduled to run.  The script below expects to be run once a week.


# import libs and set vars
from arcgis.gis import GIS
import re
import time

# 1. Add your org name, an admin username, an admin password
gis = GIS("home")
gis_users = gis.users.search(query='', max_users=5000, outside_org=0)

for user in gis_users:
    # filter for SSO extension automatically added to usernames (e.g. janeSmith_KansasUniv)
    # 2. change to your organization prefix, replacing cobbk12
    if user.username.find('_EsriEduDemo') >=0: 
        now = time.time()
        createSec=user.created/1000  # var holds lastlogin in seconds (rather than milliseconds)
        diffCreateSec = now-createSec # var holds difference between now and lastlogin in seconds.
        diffCreateDays = diffCreateSec/(24*60*60)    #Last login in days (rounded)
        # filter for  new users from the past week.
        print(user.username + ": " + str(round(diffCreateDays,2)) + " days")
        if round(diffCreateDays,2) < 365:
            # 3. Change the word 'student' below to the part of the username that is unique to students (e.g. USDstudent02034).
            # 3. (cont.) If teachers have the unique string, add the unique string where 'student' is AND change 'if not m' to 'if m'
            regex = r"([A-Z])"
            m=re.search(regex, user.username[:1]) # this check is redundant given the original search query string
            #print('m: ' + str(m))
            if NOT m:  
                # 4. Pick an option below, removing the pound sign before one of the user.update_role() lines below.
                #Pick one of the two update lines below (standard publisher or to a custom role. Get your own custom role id and insert it below.)
                #user.update_role(role='org_publisher')  # This is a built-in role type and available in all ArcGIS Online organizations.
                #user.update_role(role='wbzDiy6nktZtW6xF')  # This is the hashed id of a custom role. It will be different for your organization and role.
                roles=gis.users.roles.all(max_roles=50)
                if hasattr(user,'roleId'):
                  for role in roles:
                    if(user.roleId == role.role_id):
                        #print(user.username,user.role,role.name)
                        print(user.username + " current role: " + role.name)

print("script complete.")
