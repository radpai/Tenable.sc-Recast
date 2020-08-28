# Recast-Script
# For execution of script please use : 
Steps Common to all Security centers 
Once you have successfully logged into the security center server follow the below steps to execute the script.
$ ls
$ recast.py
You should see a file by name recast.py, if not create a file using the following command.
$ vi recast.py
Hit "i" to edit the file and copy the below contents to the file and save [ ESP followed by :wq] 
pluginList → list of plugins that need to be recast. 
newSeverity.id → 0 : informational, 1: low, 2: medium, 3: high, 4: critical
repositories.id → each 'id' is repository.id which is numerical value associated to the repository.name.

Basic vi commands :
vi filename → create a a new file or already existing file.
"i" → insert contents/edit a file , ESP → get out of edit mode, :wq → save changes , :q → quit or close w/o saving.

Create a file by name recast.csv with list of repo's , plugin IDs and required severity the plugins need to be recast to: example of csv to be used is provided as recast.csv
Ensure to use the file path based on the location of the csv created - using pwd and add the path where your csv resides in place of "x/home/radpai/recast.csv" in the script.
