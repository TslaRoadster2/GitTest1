import random
import time
runCode = "null"
while not runCode == "y":
  runCode = input("Confirm initiation: ")
ipAddress = input("Target IP Address: ")

slines = ["system check -- passed", "launch protocol tcp_8005", "attempt winver check -- passed", "reorder required packets -- complete", "intcheck passed", "waiting for response from 192.168.0.102", "host shell32 error", "prepare program found at C:\hpswsetup\sp115284\setup.exe", "perform handshake with target host"]

flines = ["cmd_check1","cmd_check2", "cmd_check42", "cmd_check9", "cmd_check13", "cmd_check5", "cmd_check44", "cmd_check33", "cmd_check15", "cmd_check63", "cmd_check0", "mac_address_error -- autoresolve", "prompt readout void", "error at C:\ProgramData\regid.1991-06.com.microsoft\regid.1991-06.com.microsoft_Windows-10-Home.swidtag", "intel process test validated", "varied response length timeout", "firewall bypassed"]

print("\n")
for i in range(42):
  print(slines[random.randint(0,(len(slines)-1))])
  i=i+1
  time.sleep(random.random())
  for i in range(random.randint(0,15)):
    print(flines[random.randint(0,(len(flines)-1))])
    i=i+1
    time.sleep(0.01)

print("\n")
runCode = input("Install required files? ")
print("Installing...")
for i in range(101):
  print(str(i) + "% complete")
  time.sleep(random.uniform(0,0.3))
print("Installation Complete")
print("\n")
time.sleep(0.5)

for i in range(30):
  print(slines[random.randint(0,(len(slines)-1))])
  i=i+1
  time.sleep(random.random())
  for i in range(random.randint(0,15)):
    print(flines[random.randint(0,(len(flines)-1))])
    i=i+1
    time.sleep(0.01)

print("\n")
runCode = input("Required server is unresponsive due to geofence domain restrictions. Redirect via VPN? ")
print("Redirecting...")
print("\n")
for i in range(42):
  print(slines[random.randint(0,(len(slines)-1))])
  i=i+1
  time.sleep(random.random())
  for i in range(random.randint(0,15)):
    print(flines[random.randint(0,(len(flines)-1))])
    i=i+1
    time.sleep(0.01)

print("final_test_0: Passed")
print("final_test_1: Passed")
print("final_test_2: Passed")
print("final_test_3: Passed")
print("final_test_4: Passed")
print("final_test_5: Passed")
print("final_test_6: Passed")
print("final_test_7: Passed")
print("final_test_8: Passed")
print("final_test_9: Passed")
input("Complete. Press enter key to exit. ")