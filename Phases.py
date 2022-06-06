import subprocess
import glob


class Phases():
	def main(self, path):

			
			p = subprocess.Popen(['sac'],
                     					stdout = subprocess.PIPE,
                     					stdin  = subprocess.PIPE,
                     					stderr = subprocess.STDOUT )

			s = "echo on\n"
			line1='read '+path+'\n'
			line2='apk\n'
			s+=line1
			s+=line2
			s += "quit()\n"
			out = p.communicate( s )
			
			return out[0]