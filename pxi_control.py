import nidaqmx
import time

class pxi_chasis:
	def __init__(self):
		self.device_list = self.check_sys_devices()

	def check_sys_devices(self):
		system = nidaqmx.system.System.local()
		system.driver_version
		device_list = []
		for device in system.devices:
			device_list.append(device)
			print(device)
		return device_list

	def daq_switch(self,dev,port,mux_en,mux_sel0,mux_sel1,enb_buf1,enb_buf2,enb_buf3):
		self.do_channel_gen(dev,port,'line0',mux_en)
		self.do_channel_gen(dev,port,'line1',mux_sel1)
		self.do_channel_gen(dev,port,'line3',mux_sel0)
		self.do_channel_gen(dev,port,'line4',enb_buf3)
		self.do_channel_gen(dev,port,'line5',enb_buf2)
		self.do_channel_gen(dev,port,'line6',enb_buf1)

	def do_channel_gen(self,dev,port,line,value):
		with nidaqmx.Task() as task:
			task.do_channels.add_do_chan(dev+'/'+port+'/'+line)
			try:
				if value == 0:
					task.write([False],auto_start=True)
				else:
					task.write([True],auto_start=True)
			except nidaqmx.DaqError as e:
				print(e)

