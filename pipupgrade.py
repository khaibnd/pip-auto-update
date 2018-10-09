import sys
import shlex
import pkg_resources
from subprocess import call

#run(shlex.split('ls -l'))
#call([sys.executable, '-m','pip','install', '--upgrade', 'pip'])

packages = [dist.project_name for dist in pkg_resources.working_set]
packages.sort()

for pkg in packages:
    print('check package: %s' %pkg)
    call([sys.executable, '-m','pip','install','--upgrade', '%s' %pkg,'--user'])

print('Finished')
