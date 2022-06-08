import pxi_control
pxi_chasis1 = pxi_control.pxi_chasis()
print(pxi_chasis1.device_list)
pxi_chasis1.daq_switch('Dev22','port4',1,0,1,1,1,0)

# mux_en,mux_sel0,mux_sel1,enb_buf1,enb_buf2,enb_buf3