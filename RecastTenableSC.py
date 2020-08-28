from tenable.sc import TenableSC
import csv
import os
import time

sc = TenableSC('SC IP address')
sc.login('username','password')


def callRecastFunction(recast_payload,pluginList):
        for x in range(0,len(pluginList)):
                recast_payload["plugin"]["id"]=pluginList[x]
                print(recast_payload)
                sc.post('recastRiskRule', json=recast_payload)

def load_RecastFile():
        flag=0
        recast_payload={}
        #repositories=[]
        pluginList=[]
        newSeverity={}
        hostType=""
        port=""
        protocol=""
        comments=""

        if os.path.exists('x/home/radpai/recast.csv'):
                with open('x/home/radpai/recast.csv') as RecastFile:
                        reader = csv.reader(RecastFile)
                        for row in reader:
                                        repositories=[]
                                        if flag==0:
                                                flag=1
                                        else:
                                                repos=row[0]
                                                repos=repos.split(",")
                                                for repo in repos:
                                                        repositories.append({"id":repo})

                                                pluginList=row[1]
                                                pluginList=pluginList.split(",")

                                                newSeverity={"id":row[2]}
                                                hostType=row[3]
                                                port=row[4]
                                                protocol=row[5]
                                                comments=row[6]

                                                recast_payload={"repositories":repositories, "plugin":{"id":""}, "newSeverity":newSeverity, "hostType":hostType, "port":port, "protocol":protocol, "comments":comments}
                                                callRecastFunction(recast_payload,pluginList)


                RecastFile.close()
        else:
                logger.error("ERROR: Recast File does not exists" )


load_RecastFile()
sc.logout()
