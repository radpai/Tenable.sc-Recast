# Recast Risk Rules/Vulnerabilities in Tenable.sc Security Center

This script allows to recast vulnerabilities in Tenable Security Centers by taking a csv file with fields - `repositories`, `plugin`, `newSeverity`, `hostType`, `port`, `protocol`, comments

## Executing the script

Login to the Security Center Server.

```bash
git clone https://github.com/radpai/Tenable.sc-Recast
```

Modify the `RecastTenableSC.py` to add the values for `SC IP address` , `username`, `password` for your Security Center.

Modify the `recast.csv` to add the following:  
`repositories` - repository ids in Security Center  
`plugin` - comma separated list of plugins to recast  
`newSeverity` - the severity to recast your vulnerability to:  
   `0`: informational  
   `1`: low   
   `2`: medium  
   `3`: high  
   `4`: critical  
`hostType` - all   
`port` - any or specific port  
`protocol` - all or specific protocol  
`comments` - reason for recasting the risk rule.

## Usage

```python
$ ls
$ RecastTenableSC.py recast.csv

# Execution
$ python3 RecastTenableSC.py recast.csv

```
Post execution, you should see the vulnerabilities/plugins with new severity in the Security Center.
