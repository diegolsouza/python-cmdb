#!/usr/bin/python3
import distro,platform,os,subprocess


#print('Processor: {}'.format(os.system('cat /proc/cpuinfo | grep "model name" | cut -d ":" -f 2')))
print('OS: {0} - {1} | Version: {2}'.format(platform.system(), distro.id(), distro.version()))
#print('Users sessions: {}'.format(os.system(who | awk "{print $1 ':' $2 ':' $3}")))
getcpu = "cat /proc/cpuinfo | grep 'model name' | cut -d ':' -f 2 | sed 's/^ *//'"
cpu = os.system(getcpu)
print('CPU',cpu)
