import nidaqmx
import time
### check system
system = nidaqmx.system.System.local()
system.driver_version
for device in system.devices:
    print(device)
freq = 10 ## in Hz
t_sleep = 1/freq
### open task


# with nidaqmx.Task() as task:
#     task.do_channels.add_do_chan(
#         'Dev5/port4/line0')
#     # try:
#     #     print('N Lines 1 Sample Boolean Write (Error Expected): ')
#     #     print(task.write([True, False, True, False],auto_start=True))
#     # except nidaqmx.DaqError as e:
#     #     print(e)
#     while(1):
#         task.write([True],auto_start=True)
#         time.sleep(t_sleep/2)
#         task.write([False],auto_start=True)
#         time.sleep(t_sleep/2)
