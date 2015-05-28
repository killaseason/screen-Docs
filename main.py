import urllib

def getMaster(year, month, day):
       """Retrieves the master index for a given date, strips crap from header, and saves it."""
       filePath='edgar/daily-index/'
       fileName='master.'+year+month+day+'.idx'
       urllib.urlretrieve('ftp://ftp.sec.gov/'+filePath+fileName, filePath+'temp.txt')

#Strip first 7 lines of crap so only data remains
#Code should locate beginning of data
        with open(filePath+'/temp.txt','r') as fin:
            data = fin.read().splitlines(True)
        with open(filePath+fileName, 'w') as fout:
            fout.writelines(data[7:])
