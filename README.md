# Aurora Alarm
**Note:** Aurora Alarm works only on Windows 10.

## How does it work
I didn't want to miss a good aurora sighting when gawking at computer screen. Aurora Alarm takes the Kp-index value from 15-minute feed from [IRF page](http://www2.irf.se/maggraphs/preliminary_real_time_k_index.php) and, when it is over 3, pushes a toast notification every 15 minutes. On the same page you can find how to interpret the given Kp-index.

To launch the app, just open `aurora_alarm.exe`. You can do same with `aurora_alarm.pyw`, but you have to do `pip install win10toast pystray` first. I know I'd be too lazy for that tho.

To exit Aurora Alarm right click on system tray icon and choose the only option.

## Aurora Alarm on Windows autostart
- Make a shortcut of  `aurora_alarm.exe`;
- Press `Win + R`;
- Type `shell:autostart` and press `OK`;
- Paste or move `aurora_alarm.exe` shortcut to this directory.