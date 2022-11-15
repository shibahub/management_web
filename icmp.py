from pysnmp.hlapi import *

result=[]
errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           CommunityData('public'),
           UdpTransportTarget(('127.0.0.1', 161)),
           ContextData(),
           #icmpInEchos
           ObjectType(ObjectIdentity('1.3.6.1.2.1.5.8.0')),
           #icmpInEchosReps
           ObjectType(ObjectIdentity('1.3.6.1.2.1.5.9.0')),
           #icmpOutEchos
           ObjectType(ObjectIdentity('1.3.6.1.2.1.5.21.0')),
           #icmpOutEchosReps
           ObjectType(ObjectIdentity('1.3.6.1.2.1.5.22.0')))
)

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    for varBind in varBinds:
        #print(' = '.join([x.prettyPrint() for x in varBind]))
        #print(str(varBind))
        
        result.append(str(varBind))