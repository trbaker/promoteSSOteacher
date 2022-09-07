# Python uses pound signs to indicate comments.  There are three actions required below, indicated in comments leading with 1,2, or 3.
# In Python, spaces and/or tabs are very important. Be careful to not lose tabs.
# Create a new standard Notebook in ArcGIS Online and add this entire script to a single code block. Customize as above. Save it. Run it.
# ArcGIS Online Notebooks can also be scheduled to run.  The script below expects to be run once a week.


# import libs and set vars
from arcgis.gis import GIS
import re
import time

# 1. Add your org name, an admin username, an admin password
gis = GIS("http://cobbk12.maps.arcgis.com", "<your_username>", "<your_password>")
gis_users = gis.users.search(query="", max_users=5000, outside_org=0)

for user in gis_users:
    # filter for SSO extension automatically added to usernames (e.g. janeSmith_KansasUniv)
    # 2. change to your organization prefix, replacing cobbk12
    if user.username.find('_cobbk12') >=0: 
        now = time.time()
        createSec=user.created/1000  # var holds lastlogin in seconds (rather than milliseconds)
        diffCreateSec = now-createSec # var holds difference between now and lastlogin in seconds.
        diffCreateDays = diffCreateSec/(24*60*60)    #Last login in days (rounded)
        # filter for  new users from the past week.
        print(user.username + ": " + str(round(diffCreateDays,2)) + " days")
        if round(diffCreateDays,2) < 7:
            m=re.search('student', user.username)
            # filter for 'student' in username
            if not m:  #if username doesn't contain 'students', then run below
                # 3. Pick an option below, removing the pound sign before one of the user.update_role() lines below.
                #Pick one of the two update lines below (standard publisher or to a custom role. Get your own custom role id and insert it below.)
                #user.update_role(role='org_publisher')  # This is a built-in role type and available in all ArcGIS Online organizations.
                #user.update_role(role='npqoaTX2gNx8MYZC')  # This is the hashed id of a custom role. It will be different for your organization and role.
                print(user.username + " updated to: " + user.role)

print("complete.")
