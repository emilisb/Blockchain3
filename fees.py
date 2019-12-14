from bitcoin.rpc import RawProxy

p = RawProxy()

txid = str(raw_input("Enter transaction ID: "))

decoded_tx = p.decoderawtransaction(p.getrawtransaction(txid))

total_out = 0
for output in decoded_tx['vout']:
    total_out += output['value']
    
total_in = 0
for input in decoded_tx['vin']:
    out_index = input['vout']
    input_tx = p.getrawtransaction(input['txid'])
    decoded_input_tx = p.decoderawtransaction(input_tx)
    total_in += decoded_input_tx['vout'][out_index]['value']
    
print("Total input: %f" % total_in)
print("Total output: %f" % total_out)

fee = total_in - total_out
print("Fee: %f" % fee)

