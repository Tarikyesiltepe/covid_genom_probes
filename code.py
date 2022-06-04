import time

#all of the sequences
general_set = set()

#probes their count
max_dict = {}

#max probes
max_list = []

#counts of probes
max_count = 0

def find_probes(string,k):
        
    #probes of one sequence
    probes=set()
    
    global max_count
    
    for i in range(len(string)-1):
        probe = string[i:i+k]
        if(len(probe) == k):            
            probes.add(probe)
    
    for i in probes:
        #checking probes is in probe dictionary
        if i in max_dict.keys():
            #increase count of probe
            max_dict[i] += 1
            if max_dict[i] > max_count:
                max_list.clear()
                max_list.append(i)
                max_count = max_dict[i]
                
            elif max_dict[i] == max_count:
                max_list.append(i)
        else:
            max_dict[i] = 1
            
            
def probes(fileName, probeLen):
    
    
    with open(fileName,"r") as f:
        data = f.readline()   
        while data:
            if "N" not in data and len(data) >= 27000:  
                general_set.add(data[:27000])
            data = f.readline()

    for i in general_set:
        find_probes(i,probeLen)
    
    num_of_valid_seq = len(general_set)
    len_of_list = len(max_list)
    
    
    with open("tarikYesiltepe.txt","w") as f:
        f.write(str(num_of_valid_seq) + " " + str(max_count))
        f.write("\n")
        f.write(str(len_of_list))
        f.write("\n")
        for i in max_list:
            f.write(str(i) + "\n")
    
    
         
        
start_time = time.time()
probes("turkey.txt",5)
end_time = time.time()
print("Time:",(end_time-start_time))
print("Max list:",max_list)
print("Max count",max_count)
print("Valid",len(general_set))









