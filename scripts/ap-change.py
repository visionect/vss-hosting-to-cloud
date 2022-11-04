from vss_python_api import ApiDeclarations
from getpass import getpass
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

def device_tclv(url, key, secret, ap_name, password):

	# TCLV commands
	ssid_set = 65
	psk_set = 67
	flash_save = {'Type': 53, 'Value': ''}
	reboot = {'Type': 91, 'Value': '0'}
	
	# VSS declaration
	vss_api_instance = ApiDeclarations(url, key, secret)
	uuid_list = get_uuid_list(vss_api_instance)
	
	# Sending TCLV commands
	for uuid in uuid_list:
		# Change SSID TCLV
		print("----Sending the TCLV command ID {0} to server URL {1}-----".format(ssid_set, url))
		tclv_send = vss_api_instance.update_device_config(uuid, ssid_set, ap_name)
		success(tclv_send, ssid_set, url)

		# Change password TCLV
		print("----Sending the TCLV command ID {0} to server URL {1}-----".format(psk_set, url))
		tclv_send = vss_api_instance.update_device_config(uuid, psk_set, password)
		success(tclv_send, psk_set, url)
			
		# Flash save TCLV
		print("----Sending the TCLV command ID {0} to server URL {1}-----".format(flash_save['Type'], url))
		tclv_send = vss_api_instance.update_device_config(uuid, flash_save['Type'], flash_save['Value'])
		success(tclv_send, flash_save['Type'], url)
		
		# Reboot TCLV
		print("----Sending the TCLV command ID {0} to server URL {1}-----".format(reboot['Type'], url))
		tclv_send = vss_api_instance.update_device_config(uuid, reboot['Type'], reboot['Value'])
		success(tclv_send, reboot['Type'], url)	
	
def main(argv):
	url = input("Enter the IP/URL of the server: ").strip()
	key = input("Enter the API key: ").strip()
	secret = input("Enter the API secret: ").strip()

	ap_name = input("Enter the SSID: ").strip()
	password = getpass()

	try:
		device_tclv(url, key, secret, ap_name, password)
	except:
		print("Something went wrong, re-check if the URL, Api key, and Api secret are correct")
		
if __name__ == '__main__':
   main(sys.argv[1:])