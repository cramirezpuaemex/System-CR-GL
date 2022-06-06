import os

a=[
 'codex_061_2006.25959.tar.mseed',
 'codex_062_2006.158831.tar.mseed',
 'codex_063_2006.346797.tar.mseed',
 'codex_064_2006.148796.tar.mseed',
 'codex_065_2006.225607.tar.mseed', 
 'codex_066_2006.100083.tar.mseed',
 'codex_067_2006.463007.tar.mseed',  
 'codex_068_2006.505042.tar.mseed',
 'codex_069_2006.537840.tar.mseed',
 'codex_070_2006.420036.tar.mseed',
 'codex_071_2006.197581.tar.mseed',
 'codex_072_2006.928890.tar.mseed',
 'codex_073_2006.939130.tar.mseed',
 'codex_074_2006.124572.tar.mseed',
 'codex_075_2006.50025.tar.mseed',
 'codex_076_2006.855994.tar.mseed',
 'codex_077_2006.55040.tar.mseed',
 'codex_078_2006.341102.tar.mseed',
 'codex_079_2006.697746.tar.mseed',
 'codex_080_2006.526150.tar.mseed',
 'codex_081_2006.842247.tar.mseed',
 'codex_082_2006.636711.tar.mseed',
 'codex_083_2006.619538.tar.mseed',
 'codex_084_2006.526053.tar.mseed',
 'codex_085_2006.886247.tar.mseed',
 'codex_086_2006.905478.tar.mseed',
 'codex_087_2006.740365.tar.mseed',
 'codex_088_2006.290799.tar.mseed',
 'codex_089_2006.496779.tar.mseed',
 'codex_090_2006.127981.tar.mseed',
 'codex_091_2006.169147.tar.mseed',
 'codex_092_2006.521738.tar.mseed',
 'codex_093_2006.251321.tar.mseed',
 'codex_094_2006.966814.tar.mseed',
 'codex_095_2006.189125.tar.mseed',
 'codex_096_2006.816250.tar.mseed',
 'codex_097_2006.975651.tar.mseed',
 'codex_098_2006.236919.tar.mseed',
 'codex_099_2006.402351.tar.mseed',
 'codex_0100_2006.861960.tar.mseed',
 ]

path='/media/carlos/Disk_CRP/'
cont=61
for i in a:
	ruta=''
	ruta=path+i
	os.system('tar -xvf '+ ruta+' -C /media/carlos/Disk_CRP/')
	os.system('cd  '+path+'codex_0'+str(cont)+'_2006')
	os.system('/media/carlos/Disk_CRP/ mseed2sac *.mseed *.SAC')
	#os.system('cd ..')
	os.system('mkdir '+path+'0'+str(cont))
	cont+=1