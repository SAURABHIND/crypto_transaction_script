import urllib.request, json 
import csv

owner = '3QPB5BQNeUcksTt1sZXZM5BFnFSyzrDRht'
#owner = '1PDHdVA4Ft1iDr8ruwYs7zheWBSdewriAw'
path = '/home/bsetec/Desktop/final_amount.txt'

txHash_output=['TxHash']
amount_output=['Amount']
date=['Date']
Type=['Type']

with urllib.request.urlopen("https://api.blockcypher.com/v1/btc/main/addrs/3QPB5BQNeUcksTt1sZXZM5BFnFSyzrDRht") as url:
  data = json.loads(url.read().decode())
  for item in data["txrefs"]:
    txHash = item["tx_hash"]
    with urllib.request.urlopen("https://api.blockcypher.com/v1/btc/main/txs/"+txHash) as urlInner:
      dataInner = json.loads(urlInner.read().decode())
      final_amount = 0;
      temp=""
      for input_address in dataInner["inputs"]:
        for address1 in input_address["addresses"]:
          if address1 == owner:
            final_amount = final_amount - input_address["output_value"]
            print (address1)
            print (final_amount)
            temp="SENT"
          else:
            pass
      for output_address in dataInner["outputs"]:
        for address2 in output_address["addresses"]:
          if address2 == owner:
            final_amount = final_amount + output_address["value"]
            print (address2)
            print (final_amount)
            temp="RECEIVE"
          else:
            pass

      date.append(dataInner['confirmed'])
      txHash_output.append(txHash)
      Type.append(temp)
      final = final_amount / 100000000
      amount_output.append(final)

      

      
        
  
  with open("/home/bsetec/Desktop/outputnew.csv","w") as out_file:
    for i in range(len(amount_output)):
      out_string = ""
      out_string = str(date[i])
      out_string += ", " + str(txHash_output[i])
      out_string += ", " + str(Type[i])
      out_string += ", " + str(amount_output[i]) + "\n"
      out_file.write(out_string)
