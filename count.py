#! /usr/bin/env python
 
#import sys
#f = sys.argv[1]

#A,T,C,G = 0,0,0,0

#with open(f, 'r') as handle:
#    for i in handle:
#        if i.startswith('>'):
#            header = i.strip()
#        else:
#            seq = i.strip()
#            A += seq.count('A')
#            T += seq.count('T')
#            C += seq.count('C')
#            G += seq.count('G')

#print(f"A : {A}")
#print(f"T : {T}")
#print(f"C : {C}")
#print(f"G : {G}")

import sys

class FASTA:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.count = {}
        self.length = 0

    def count_base(self):
        with open(self.file_name, 'r') as handle:
            for i in handle:
                if  i.startswith('>'):
                    continue
                i = i.strip()
                for s in i:
                    if s in self.count:
                        self.count[s] += 1
                    else:
                        self.count[s] = 1

    def get_length(self):
        length = 0
        for k,v in self.count.items():
            self.length +=v
    
    def __len__(self):
        for k,v in self.count.items():
            self.length +=v
        return self.length

if __name__=="__main__":
    if len(sys.argv) != 2:
        print(f"usage: python{sys.argv[0]} [fasta]")
        sys.exit()
    file_name = sys.argv[1]
    t = FASTA(file_name)
    t.count_base()
    print(t.count)
    t.get_length()
    print(t.length)

