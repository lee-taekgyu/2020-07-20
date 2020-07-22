
d = {"ins":0, "del":0, "SNP":0}
with open("070.vcf", 'r') as handle:
    for line in handle:
        if line.startswith("#"):
            continue

        splitted = line.strip().split("\t")
        alts = splitted[4].split(",")
        ref = splitted[3]
        for alt in alts:
            if len(ref) < len(alt):
                d['ins'] += 1
            elif len(ref) > len(alt):
                d['del'] += 1
            elif len(ref) == len(alt):
                d['SNP'] += 1
            else:
                raise
print(d)
        
