import os,sys

def write_tex(csvfn, log=sys.stdout) :
  assert os.path.exists(csvfn)
  s = '''\\section{Filtered Top8000 PDB Chains and Residue Counts}

\\begin{longtable}{|c|c|c| a|a|a| c|c|c| a|a|a| c|c|c|}
PDB & Cn & N & PDB & Cn & N & PDB & Cn & N & PDB & Cn & N & PDB & Cn & N \\\\
\\hline
\\endfirsthead

PDB & Cn & N & PDB & Cn & N & PDB & Cn & N & PDB & Cn & N & PDB & Cn & N \\\\
\\hline
\\endhead

\\multicolumn{15}{r}{Continued on next page} \\\\
\\endfoot

\\hline \hline
\\endlastfoot
\\fontfamily{courier}
'''
  print >> log, s.strip()
  fle = open(csvfn,'r')
  head = fle.readline()
  i = 0
  eof = False
  while 1 :
    i= i + 1
    if i > 8000 : raise RuntimeError("More than 8000 lines in %s" % csvfn)
    tl = []
    for i in range(5) :
      line = fle.readline()
      tl = tl + line.strip().split(',')
      if line == '' : eof = True
    print >> log, " & ".join(tl) + "\\\\"#;break
    if eof : break
  fle.close()
  s = '''\\bottomrule
\\end{longtable}
\\fontfamily{\\familydefault}'''
  print >> log, s

def run(args) :
  csvfn = "8000_filtered_pdb_chains.csv"
  write_tex(csvfn)

if __name__ == "__main__" :
  run(args=sys.argv[1:])
