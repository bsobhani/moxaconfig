from telnetlib import Telnet
import time

class NPort5150A:
	def send_cmd(self, cmd):
		cmd = cmd + "\r\n"
		cmd = bytes(cmd, encoding="ascii")
		self.tn.write(cmd)
		time.sleep(.1)
	def login(self):
		self.send_cmd("admin")
		self.send_cmd("moxa")

	def main_menu_screen(self):
		self.send_cmd("m")
	def serial_settings_screen(self):
		self.main_menu_screen()
		self.send_cmd("3")
		self.send_cmd("1")
	def operating_settings_screen(self):
		self.main_menu_screen()
		self.send_cmd("4")
		self.send_cmd("1")

	def network_settings_screen(self):
		self.main_menu_screen()
		self.send_cmd("2")

	def port_alias_screen(self):
		self.serial_settings_screen()
		self.send_cmd("1")
	def baud_rate_screen(self):
		self.serial_settings_screen()
		self.send_cmd("2")
	def data_bits_screen(self):
		self.serial_settings_screen()
		self.send_cmd("3")
	def stop_bits_screen(self):
		self.serial_settings_screen()
		self.send_cmd("4")
	def parity_screen(self):
		self.serial_settings_screen()
		self.send_cmd("5")
	def flow_control_screen(self):
		self.serial_settings_screen()
		self.send_cmd("6")
	def interface_standard_screen(self):
		self.serial_settings_screen()
		self.send_cmd("8")


	def ip_screen(self):
		self.network_settings_screen()
		self.send_cmd("1")
	def netmask_screen(self):
		self.network_settings_screen()
		self.send_cmd("2")
	def gateway_screen(self):
		self.network_settings_screen()
		self.send_cmd("3")

	def operating_mode_screen(self):
		self.operating_settings_screen()
		self.send_cmd("1")
	def tcp_port_screen(self):
		self.operating_settings_screen()
		self.send_cmd("a")

	def clear_field(self):
		for i in range(50):
			self.tn.write(b"\b")

	def set_port_alias(self, alias):
		self.port_alias_screen()
		self.clear_field()
		self.send_cmd(alias)
		self.send_cmd("")
	def set_baud_rate(self, key):
		self.baud_rate_screen()
		self.send_cmd(key)
	def set_data_bits(self, key):
		self.data_bits_screen()
		self.send_cmd(key)
	def set_stop_bits(self, key):
		self.stop_bits_screen()
		self.send_cmd(key)
	def set_parity(self, key):
		self.parity_screen()
		self.send_cmd(key)
	def set_flow_control(self, key):
		self.flow_control_screen()
		self.send_cmd(key)
	def set_interface_standard(self, key):
		self.interface_standard_screen()
		self.send_cmd(key)


	def set_operating_mode(self, key):
		self.operating_mode_screen()
		self.send_cmd(key)
	def set_tcp_port(self, port):
		self.tcp_port_screen()
		self.clear_field()
		self.send_cmd(port)
		self.send_cmd("")


	def set_ip(self, ip):
		self.ip_screen()
		self.clear_field()
		self.send_cmd(ip)
		self.send_cmd("")
	def set_netmask(self, netmask):
		self.netmask_screen()
		self.clear_field()
		self.send_cmd(netmask)
		self.send_cmd("")
	def set_gateway(self, gateway):
		self.gateway_screen()
		self.clear_field()
		self.send_cmd(gateway)
		self.send_cmd("")


	def __init__(self, ip, port=23):
		self.tn = Telnet(ip, port)
		time.sleep(1)
	

