#
# routes/main.py
#
import system
import ip
import icmp
routes = {
  "/":"Web Application for SMTP manage",                        # http route make it happend by 
  "/system" : system.result ,       # Python Dictionary:- map path to resource
  "/ip" : ip.result,
  "/icmp": icmp.result
  
}


