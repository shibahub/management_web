from pysnmp.entity.rfc3413.oneliner import cmdgen
result=[]
errorIndication, errorStatus, errorIndex, varBindTable = cmdgen.CommandGenerator().nextCmd(
    cmdgen.CommunityData('test-agent', 'public'),
    cmdgen.UdpTransportTarget(('localhost', 161)),
    (1,3,6,1,2,1,1)
    )

if errorIndication:
    print('1')
else:
    if errorStatus:
        print ("2")
    else:
        for varBindTableRow in varBindTable:
            for name, val in varBindTableRow:
                tmp = name.prettyPrint()+' = '+val.prettyPrint()
                #print(tmp)
                result.append(tmp)
                #print (f"{name.prettyPrint()} = {val.prettyPrint() or 'Unknown'}")

#print(result)