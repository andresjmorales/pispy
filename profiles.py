from binascii import unhexlify
from pprint import pprint
from sflow import decode
import time

TOTAL_GENERATION_TIME = 1 * 10 ** 12




# plan:
# when new datagram is collected, check dictionary of profiles to see if it already exists in the master list of profiles

# if it does not, make a profile for it and add to the dictionary
# if it does exist, go to that profile and average all the values with the values of the current datagram to make the values more accurate

# then


def get_datagram(rawsflow_datagram):
    unhex_sflow = unhexlify(rawsflow_datagram)
    sflow_dict = decode(unhex_sflow)
    return sflow_dict


class Profile:
    def __init__(self, ip, raw_sflow ):
        datagram = get_datagram(raw_sflow)
        self.datagram = datagram
        self.ip = datagram['agent_address']
        
    def print_profile(self):
        pprint(self.datagram)


# python dict of all ip:profiles
all_datagrams = {}



start_time = time.time()
print("Starting profile generation with sFlow for time", TOTAL_GENERATION_TIME)
while (time.time() - start_time < TOTAL_GENERATION_TIME):
    
    sflow_sampling = 0 # sflow api here
    
    datagram_received = sflow_sampling
    
    if datagram_received:
        
        ip1 = "127.0.0.1"
        ip2 = "127.0.0.2"

        rawsflow_datagram = '0000000500000001ac15231100000001000001a6673f36a00000000100000002' +\
            '0000006c000021280000040c0000000100000001000000580000040c00000006' +\
            '0000000005f5e100000000010000000300000000018c6e9400009b9e00029062' +\
            '0001f6c400000000000000000000000000000000005380600000a0de0000218a' +\
            '000008d7000000000000000000000000'
        
        p1 = Profile(ip1, rawsflow_datagram)
        p2 = Profile(ip2, rawsflow_datagram)

        #newp.print_profile()

        all_datagrams[ip1] = p1
        all_datagrams[ip2] = p1

    # do nothing else


'''
def clean_sflow_data(jumbled):

    clean_sflow_dict = {}
    clean_sflow_dict = jumbled['samples'][0]['counters'][0]
    clean_sflow_dict['ip'] = jumbled['agent_address']
    clean_sflow_dict['seq'] = jumbled['sequence_number']

    for i in jumbled['samples'][0]['counters'][1:]:
        print(1)
        clean_sflow_dict.add(i)
    
    clean = 1
    return clean
'''

#pprint(clean_sflow_dict)
