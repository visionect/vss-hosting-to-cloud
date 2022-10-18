from vss_python_api import ApiDeclarations
import time 
import sys, getopt

def get_uuid_list(vss_api_instance):
	uuid_list = list()
	all_devices = vss_api_instance.get_all_devices()[1]

	
	for device in all_devices:
		uuid_list.append(device['Uuid'])
		
	return uuid_list
	
def success(tclv_send, tclv_type, url):
	if tclv_send != 200:
		print("Sending the TCLV command ID {0} to server URL {1} FAILED, please check the parameters-----".format(tclv_type, url))
	else:
		print("Command was successful")
		
def delete_device(vss_api_instance, status, uuid):
	if status != 200:
		print("The device could not be deleted from the server")
	else:
		vss_api_instance.delete_device(uuid)
		print("Device deleted from the server!")

def device_tclv(url, key, secret):

	# TCLV commands
	tclv_type = 166
	print("West Europe - we3.gw.getjoan.com \nEast US - eu3.gw.getjoan.com \nWest US - wu.gw.getjoan.com \nHong Kong - hongkong1.gw.getjoan.com\n")
	value = input("Enter the target server for change: ").strip() + ":11113"
	flash_save = {'Type': 53, 'Value': ''}
	reboot = {'Type': 91, 'Value': '0'}
	
	# VSS declaration
	vss_api_instance = ApiDeclarations(url, key, secret)
	uuid_list = get_uuid_list(vss_api_instance)
	
	# Sending TCLV commands
	for uuid in uuid_list:
		# Change server TCLV
		print("----Sending the TCLV command ID {0} to server URL {1}-----".format(tclv_type, url))
		tclv_send = vss_api_instance.update_device_config(uuid, tclv_type, value)
		success(tclv_send, tclv_type, url)
		
		delete_device(vss_api_instance, tclv_send, uuid)	
	
def main(argv):
	url = input("Enter the IP/URL of the server: ").strip()
	key = input("Enter the API key: ").strip()
	secret = input("Enter the API secret: ").strip()

	try:
		device_tclv(url, key, secret)
	except:
		print("Something went wrong, re-check if the URL, Api key, and Api secret are correct")
		
if __name__ == '__main__':
   main(sys.argv[1:])
