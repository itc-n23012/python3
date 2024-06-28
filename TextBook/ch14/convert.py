import sys
import ezsheets

if len(sys.argv) < 2:
    sys.exit()

ss = ezsheets.upload(sys.argv[1])
ss.title = ss.title + '.conv'
ss.downloadAsExcel()
ss.downloadAsODS()
ss.downloadAsPDF()
