from subprocess import PIPE, Popen
import os
from threading import Thread

p_install = Popen(['bash', 'install.sh'], stdout=PIPE, stderr=PIPE)
stdout = p_install.stdout.read()
stderr = p_install.stderr.read()
print(stdout.decode('utf8'))


def run_browser_stream():
	p_browser_stream = Popen(['bash', 'browser_stream.sh'], stdout=PIPE, stderr=PIPE)
	p_browser_stream.wait()


def run_stream():
	process = Popen(['bash', 'stream.sh'], stdout=PIPE, stderr=PIPE)
	while True:
		output = process.stdout.readline().decode('utf8')
		if output == '' and process.poll() is not None:
			break
		if output:
			print(output.strip())
	rc = process.poll()
	return rc


if not stderr:
	thread = Thread(target=run_browser_stream)
	thread.start()
	print('installed')
	ready = False
	print('wating for browser recording')
	while not ready:
		if os.path.exists('output.wav'):
			ready = True
	print('start streaming into browser output')
	run_stream()
			
	

