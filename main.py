from class_bed import BED

# enter the full path to the bedgraph format file you want to convert to a wiggle file

filename = 'C:\\Users\\hpatterton\\Documents\\Students\\Jessica Reid\\NGS\\Galaxy570-[WT_6d_(Bedgraph_Treatment)].bedgraph'

bed = BED()
bed_matrix = bed.Readfile(filename)
chromosome_name = []
number_of_chromosomes = 0
for entry in bed_matrix:
	if(number_of_chromosomes == 0):
		chromosome_name.append(entry[0])
		number_of_chromosomes += 1
	else:
		if(entry[0] == chromosome_name[number_of_chromosomes-1] or entry[0] in chromosome_name):
			pass
		else:
			chromosome_name.append(entry[0])
			number_of_chromosomes += 1
print(number_of_chromosomes)
print(chromosome_name)
wiggle,total = bed.ConvertBEDtoWiggle(bed_matrix)
print('Total signal ='+str(total))
dot = filename.rfind('.')
outfile = filename[:dot]
handle = open(outfile+'_4.wig','w')
for line in wiggle:
	handle.write(line+'\n')
print('Written to '+outfile+'.wig')
print('done')

	

