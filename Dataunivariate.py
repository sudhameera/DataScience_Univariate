class dtypes():
    def quanqual(data):
        quan=[]
        qual=[]

        for columnname in data.columns:
            #print(columnname)
            if(data[columnname].dtypes=='O'):
                qual.append(columnname)
                #print("Qual")
            else:
                quan.append(columnname)
                #print("quan")
        return quan,qual