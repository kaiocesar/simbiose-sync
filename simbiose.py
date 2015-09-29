import sys, time
import os.path
from daemon import Daemon

class MyDaemon(Daemon):
    def run(self):
        while True:
            print("Loading ...")
            time.sleep(1)

if __name__ == "__main__":
    pidfile = '/tmp/daemon-example123.pid'

    if not os.path.exists(pidfile):
        id = os.getpid()
        file = open(pidfile, 'a')
        file.write(str(id))
        file.close()


    daemon = MyDaemon(pidfile)
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print("Unknow command")
            sys.exit(2)
    else:
        print("Usage: %s start|stop|restart" % sys.argv[0])
        sys.exit(2)