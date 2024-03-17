import os
import sys
import subprocess

# Disabling output buffering so that the status window can be updated in real time
os.environ['PYTHONUNBUFFERED'] = '1'

print('Starting WhisperWriter...')

# ko: multiple processes launched
# subprocess.run([sys.executable, os.path.join('src', 'main.py')])

# ok: but needs python in env:
#subprocess.run(['python', os.path.join('src', 'main.py'), os.environ['PARAM']])

# ko: [49856] Cannot create temporary directory!
# if compile with the following --runtime-tmpdir option, loop again:
# pyinstaller -F run.py --runtime-tmpdir .
si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
subprocess.run([sys.executable,os.path.join('src','main.py'),os.environ['PYTHONUNBUFFERED']],env={'PYTHONUNBUFFERED':os.environ['PYTHONUNBUFFERED']},stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,startupinfo=si)
