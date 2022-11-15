from pysnmp.entity.rfc3413.oneliner import cmdgen  
errorIndication, errorStatus, errorIndex, \
varBindTable = cmdgen.CommandGenerator().bulkCmd(  
            cmdgen.CommunityData('test-agent', 'public'),  
            cmdgen.UdpTransportTarget(('127.0.0.1', 161)),  
            0, 
            25, 
            #(1,3,6,1,2,1,4,20), # ipAddrTable OID . This works fine.
            (1,3,6,1,2,1,4,21) # ipRouteTable
            #(1,3,6,1,2,1,4,22), # ipNetToMediaTable
        )

if errorIndication:
   print('1')
else:
    if errorStatus:
        print ('2')
            
    else:
        for varBindTableRow in varBindTable:
            for name, val in varBindTableRow:
                print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
                #print(f'{name}, {val}')