cnt = 0
with open("070.vcf", 'r') as handle:
    for line in handle:
        if line.startswith("##"):
            continue
        if line.startswith("#"):
            header = line.strip().split("\t")
            filt_idx = header.index("ID")

        splitted = line.strip().split("\t")
        chrom = splitted[0]
        pos = splitted[1]
        id_ = splitted[2]
        ref = splitted[3]
        alt = splitted[4]
        
        if splitted[filt_idx] != ".":
            print(f"{chrom} \t, {pos} \t, {alt} \t, {ref} \t, {id_} \t")

