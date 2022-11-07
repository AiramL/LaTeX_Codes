def show_double_entries(file):
    with open(file,'rb') as bibtex:
        refs = []
        entry =  ''
        encoding = 'utf-8'
        for line in bibtex:
            #print(line.decode(encoding))
            if '@' in line.decode(encoding):
                entry = line.decode(encoding)
            elif line.decode(encoding)[0]  == '}':
                entry += line.decode(encoding)
                refs.append(entry)
            elif line.decode(encoding)[0] == '\n':
                pass
            else:
                entry += line.decode(encoding)

    title_list = []
    double =  []
    for i in range(len(refs)):
        itens = refs[i].split(',')
        for k in itens:
            if ('booktitle' in k) or ('shorttitle' in k):
                pass
            elif 'title' in k:
                key = k.replace('{','').replace('}','').replace('\r\n','').replace('title','').replace('=','').lower().replace(' ','')
                if key in title_list:
                    double.append(k.replace('{','').replace('}','').replace('\r\n','').replace('title','').replace('=',''))
                else:
                    title_list.append(key)

    return double


if __name__ == "__main__":
    print(show_double_entries('ref.txt'))
