for ii in `seq 1 6`
do
  cat > PPINPUT << EOF
&INPUTPP
  outdir = './tmp'
  plot_num = 7
  lsign = .true.
  filplot = PSI2.dat
  kpoint = 1
  kband = $ii
/

&PLOT
  iflag = 3
  output_format = 5
  fileout = 'MO$ii.xsf'
/
EOF
  # Run pp.x
  ~/mysoftwares/qe-5.2.1/pp.x < PPINPUT
done

