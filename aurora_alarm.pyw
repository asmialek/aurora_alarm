from win10toast import ToastNotifier
import urllib.request
import urllib.error
import threading
import pystray
from PIL import Image


toaster = ToastNotifier()
duration = 20
time_period = 15
exit_call = False
timer_object = None


def aurora_lookup():
    if not exit_call:
        global timer_object
        timer_object = threading.Timer(time_period * 60.0, aurora_lookup)
        timer_object.start()

    try:
        page = urllib.request.urlopen('http://www2.irf.se/maggraphs/'
                                      'preliminary_real_time_k'
                                      '_index_15_minutes')
        index = int(page.read())
    except urllib.error.URLError:
        index = 0

    if index not in list(range(0, 10)):
        pass
    elif index >= 7:
        toaster.show_toast('Holy Sh*t',
                           f'There should be amazing aurora outside!'
                           f'Get your ass up! The Kp index is: {index}',
                           duration=duration,
                           icon_path='aurora_alarm.ico',
                           threaded=True)
    elif index >= 3:
        toaster.show_toast('Aurora Alarm',
                           f'There could be an aurora over your head!'
                           f'Get out and look up. The Kp index is: {index}',
                           duration=duration,
                           icon_path='aurora_alarm.ico',
                           threaded=True)
    else:
        # toaster.show_toast('Aurora Alarm',
        #                    f'There is nothing to see here.\n'
        #                    f'The Kp index is: {index}',
        #                    duration=duration,
        #                    icon_path='aurora_alarm.ico',
        #                    threaded=True)
        pass


if __name__ == '__main__':
    toaster.show_toast('Aurora Alarm',
                       f'Hi! The notification will pop every {time_period} '
                       f'minutes if Kp index is over 3.',
                       duration=duration,
                       icon_path='aurora_alarm.ico',
                       threaded=True)
    aurora_lookup()

    def kill_app():
        global exit_call
        global timer_object

        icon.stop()
        exit_call = True
        timer_object.cancel()

    image = Image.open('aurora_alarm.ico')

    menu = pystray.Menu(pystray.MenuItem('Exit', kill_app))

    icon = pystray.Icon('Aurora Alarm', image, 'Aurora Alarm', menu=menu)

    icon.visible = True
    icon.run()
