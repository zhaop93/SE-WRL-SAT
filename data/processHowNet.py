import jieba

bound = [':', '}']
r = open('HowNet.txt', 'r')
word_sememe_dict = {}

def readItem():
    while True:
        line = r.readline()
        if line == '':
            break

        while line[:2] != 'NO':
            line = r.readline()
            if line == '':
                break
            pass
        if line == '':
            break
        #print(line)

        word = r.readline()[:-1].split('=')[1]
        while r.readline()[:3] != 'S_C':
            pass

        EXAMPLE = r.readline()[:-1].split('=')[1]
        EXAMPLE = EXAMPLE.replace('~', word).split('，')
        examples = []
        for item in EXAMPLE:
            examples.extend([x for x in jieba.cut(item)])
        
        while r.readline()[:3] != 'E_E':
        	pass
        DEF = r.readline()[:-1].split('=')[1]
        sememes = []
        sememe = ''
        begin = False
        for x in DEF:
            if x == '|':
                begin = True
                continue
            if x in bound:
                begin = False
                sememes.append(sememe)
                sememe = ''
                continue
            if begin:
                sememe += x
        sememes = sorted(sememes)
        #if word_sememe_dict.has_key(word):
        if word in word_sememe_dict:
            word_sememe_dict[word].append((sememes, examples))
        	#word_sememe_dict[word].append(sememes)
        else:
    	    word_sememe_dict[word] = [(sememes, examples)]
        	#word_sememe_dict[word] = [sememes]

readItem()

#for key, value in word_sememe_dict.items():
    #semems_list = []
    #example_list = []
    #print(value)
    #sem_exam = list(set(tuple(value)))
    #print(sem_exam)

    #word_sememe_dict[key] = list(set(tuple()))
    #word_sememe_dict[key] = list(set(value))

w = open('Word_Sense_Sememe.txt', 'w')
for key, values in word_sememe_dict.items():
    w.write(key)
    w.write(' ')
    w.write(str(len(values)))
    w.write(' ')
    for value in values:
        #print(value)
        semems_list = value[0]
        example_list = value[1]
        w.write(str(len(semems_list)))
        w.write(' ')
        for i, sememe in enumerate(semems_list):
            w.write(sememe)
            w.write(' ')
        if len(example_list) <= 0:
            w.write('0')
        else:
            w.write('1 ')
            w.write(' '.join(example_list))
        w.write(' ')

    w.write('\n')
w.close()
