# https://www.activestate.com/resources/quick-reads/how-to-install-python-packages-using-a-script/
import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'<packagename>'])