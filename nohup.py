import subprocess, signal
subprocess.Popen(['python3', 'docking.py'],
                 stdin=subprocess.DEVNULL,
                 stdout=open('nohup.log', 'w'),
                 stderr=subprocess.STDOUT,
                 start_new_session=True,
                 preexec_fn=(lambda: signal.signal(signal.SIGHUP, signal.SIG_IGN)))
