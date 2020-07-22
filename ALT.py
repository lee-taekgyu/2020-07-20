cnt = 0
with open("070.vcf", 'r') as handle:
    for line in handle:
        if line.startswith("#"):
            continue

        splitted = line.strip().split("\t")
        alts = splitted[4].split(",")
        for alt in alts:
            cnt += 1 

print(cnt)
