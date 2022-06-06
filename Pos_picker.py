import subprocess
import glob

class Pos_picker():
	def main(self, path):
		p = subprocess.Popen(['sac'],
						stdout = subprocess.PIPE,
    					stdin  = subprocess.PIPE,
    					stderr = subprocess.STDOUT)
		s=''
		
		#print path1
		#pathE='/home/carlos/Escritorio/CODEX_2006/'+dia[j]+'/ZA.'+estaciones[i]+'..HHE.M.2006.027.000000.SAC'
		#pathN='/home/carlos/Escritorio/CODEX_2006/'+dia[j]+'/ZA.'+estaciones[i]+'..HHN.M.2006.027.000000.SAC'
		s = "echo on\n"
		line1='read '+path+'\n'
		line2='apk\n'
		s+=line1
		s+=line2
		s += "quit()\n"

		#print '========================================'
		#print s
		#print '========================================'

		
		out = p.communicate(s)
		a=out[0]


		return a