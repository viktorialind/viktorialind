folk=307357870
#set inn gildi sem synir hversu margar sek eru i ari
ar_sek=365*24*60*60
ar_sek_float=float(ar_sek)

faeding=ar_sek_float/7
daudi=ar_sek_float/13
nyr_innflytjandi=ar_sek/35
#bid notenda um ar
arsfjoldi_str=input("Years:")
arsfjoldi_float=float(arsfjoldi_str)
arsfjoldi_int=int(arsfjoldi_str)
if arsfjoldi_float<0: #set inn bool ef inn kemur neikvaed tala
   print('Invalid input!')
else:
  folksfjoldi=folk+arsfjoldi_float*(faeding-daudi+nyr_innflytjandi)
  folksfjoldi_int=int(folksfjoldi)
  print('eftir', arsfjoldi_int,'ar verdur folksfjoldi i USA', folksfjoldi_int)


