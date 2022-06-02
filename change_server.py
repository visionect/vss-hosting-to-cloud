from vss_python_api import ApiDeclarations
import time 
import sys, getopt

def get_uuid_list(vss_api_instance):
	uuid_list = list()
	all_devices = vss_api_instance.get_all_devices()[1]

	
	for device in all_devices:
		uuid_list.append(device['Uuid'])
		
	return uuid_list

def device_tclv(url, key, secret, tclv_type, value):

	# TCLV commands
	tclv_type = 166
	print("West Europe - we3.gw.getjoan.com \nEast US - eu3.gw.getjoan.com \nWest US - wu.gw.getjoan.com \nHong Kong - hongkong1.gw.getjoan.com")
	value = input("Enter target server: ").strip()
	flash_save = {'Type': 53, 'Value': ''}
	reboot = {'Type': 91, 'Value': '1'}
	
	# VSS declaration
	vss_api_instance = ApiDeclarations(url, key, secret)
	uuid_list = get_uuid_list(vss_api_instance)
	
	# Sending TCLV commands
	for uuid in uuid_list:
		# Change server TCLV
		print("----Sending the TCLV command ID {0} to server URL {1}-----".format(tclv_type, url))
		tclv_send = vss_api_instance.update_device_config(uuid, tclv_type, value)
		if tclv_send != 200:
			print("Sending the TCLV command ID {0} to server URL {1} FAILED, please check the parameters-----".format(tclv_type, url))
		else:
			print("Command was successful")
			
		# Flash save TCLV
		print("----Sending the TCLV command ID {0} to server URL {1}-----".format(flash_save['Type'], url))
		tclv_send = vss_api_instance.update_device_config(uuid, flash_save['Type'], flash_save['Value'])
		if tclv_send != 200:
			print("Sending the TCLV command ID {0} to server URL {1} FAILED, please check the parameters-----".format(flash_save['Value'], url))
		else:
			print("Command was successful")
		
		# Reboot TCLV
		print("----Sending the TCLV command ID {0} to server URL {1}-----".format(reboot['Type'], url))
		tclv_send = vss_api_instance.update_device_config(uuid, reboot['Type'], reboot['Value'])
		if tclv_send != 200:
			print("Sending the TCLV command ID {0} to server URL {1} FAILED, please check the parameters-----".format(reboot['Type'], url))
		else:
			print("Command was successful")	
	
def main(argv):
	key = "dbd2226a755f0848"
	secret = "TpwLJd3aR+0L0gs6FMhEiYgBD2FQ4ozg7/pQigH+TFg"
	url = "http://192.168.64.118:8081/"

	try:
		device_tclv(url, key, secret)
	except:
		print("Something went wrong, re-check if the URL, Api key, and Api secret are correct)
		
if __name__ == '__main__':
   main(sys.argv[1:])
