a = []
with open("070.vcf", 'r') as handle:
    for i in handle:
        if i.startswith("#"):
            continue
        i = i.strip().split("\t")
        a.append(i)
print(len(a))
cnt = 0
with open("070.vcf", 'r') as handle:
    for i in handle:
        if i.startswith("#"):
            continue
        cnt += 1
        
print(cnt)
