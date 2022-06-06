import os


class File_hyp():
	def file_main(self, model, name_salve_file, path_estaciones, path_del, path_crh):
		

		fo = open(name_salve_file+'/codex.hyp', 'w')
		fo.write("RMS 4 .10 2 3				/Residual weighting\n")
		fo.write("POS 1.78\n")
		fo.write("ZTR 5\n")
		fo.write("DIS 4 15 3.5 7\n")



		fo.write("* OUTPUT FORMAT\n")
		fo.write("ERF T					/Send error messages to terminal\n")
		fo.write("TOP F					/No page ejects\n")
		fo.write("LST 2 0 1				/station list or models in printfile\n")
		fo.write("KPR 2					/Medium print output each event\n")
		fo.write("H71 2 1 3				/Use hypo71 summary format for this test\n")

		fo.write("CRH 1 '"+ path_crh+"'\n")
		fo.write("STA '"+path_estaciones+"'\n")
		fo.write("DEL '"+path_del+"'\n")
		fo.write("PRT '"+name_salve_file+"/File_hyp/rcodex.prt'\n")
		fo.write("PHS '"+name_salve_file+"/File_hyp/codex.phs'\n")
		fo.write("SUM '"+name_salve_file+"/File_hyp/codex.sum'\n")
		fo.write("ARC '"+name_salve_file+"/File_hyp/codex.arc'\n")
		fo.write("FIL\n")
		fo.write("LOC\n")
		fo.write("STO\n")
		fo.close()