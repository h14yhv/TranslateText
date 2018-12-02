import sys, getopt, re, string


def write_file(path_file, content):
    file_translate = open(path_file, 'w+')
    try:
        print 'write content to file'
        file_translate.write(content)
    except:
        print "Error", sys.exc_info()[0]
    file_translate.flush()
    file_translate.close()


def read_file(path_file):
    file_core = open(path_file, 'r+')
    if file_core.mode == 'r+':
        content = file_core.read()
        file_core.close()
    return content


def replace_algo(content, old, new):
    # generate regular expression ignore case sentitive to search
    try:
        re_item_find = re.compile(old, re.IGNORECASE)
        content, number = re_item_find.subn(new, content)
    except:
        print 'compile error'
        content = string.replace(content, old, new)
        return content
    if number > 0:
        print 'Success replace ', number, old, 'to', new
    return content


def replace_str(content, old, new):
    StrOld = old.split(' ')
    if len(StrOld) > 1:
        content = replace_algo(content, old, StrOld[0] + 'hv8 ' + StrOld[1] + 'hv8')
        return content
    content = replace_algo(content, old + '', new + 'hv8')
#    content = replace_algo(content, old + 's ', new + 'shv8 ')
#    content = replace_algo(content, old + 'es ', new + 'eshv8 ')
#    content = replace_algo(content, old + 'ed ', new + 'edhv8 ')
#    content = replace_algo(content, old + ',', new + 'hv8,')
#    content = replace_algo(content, old + '.', new + 'hv8.')
#    content = replace_algo(content, old + ':', new + 'hv8:')
#    content = replace_algo(content, old + ';', new + 'hv8;')
    return content


def convert_replace_str(content, old, new):
	content = replace_algo(content, 'hv8', '')
	return content
#    StrOld = old.split(' ')
#    if len(StrOld) > 1:
#        content = replace_algo(content, StrOld[0] + 'hv8 ' + StrOld[1] + 'hv8', old)
#        return content
#    content = replace_algo(content, new + 'hv8', old + '')
#    content = replace_algo(content, new + 'shv8 ', old + 's ')
#    content = replace_algo(content, new + 'eshv8 ', old + 'es ')
#    content = replace_algo(content, new + 'edhv8 ', old + 'ed ')
#    content = replace_algo(content, new + 'hv8, ', old + ', ')
#    content = replace_algo(content, new + 'hv8. ', old + '. ')
#    content = replace_algo(content, new + 'hv8: ', old + ': ')
#    content = replace_algo(content, new + 'hv8; ', old + '; ')



def eng1_to_eng():
    #    FileCore = open(sys.argv[1], 'a+')
    #    FileTranslate = open(sys.argv[2], 'r+')

    # open file source
    Core = read_file(core_path)
    content = read_file(dest_path)
    CoreOriginal = Core.splitlines()
    # print(contentCore)
    i = 0
    while len(CoreOriginal) != i:
        # print CoreOriginal
        content = convert_replace_str(content, CoreOriginal[i], CoreOriginal[i])  # Replace word
        i = i + 1

    # print(content)
    write_file(dest_path, content)


def vn_to_eng():
    content = read_file(dest_path)
    core = read_file(core_path)
    content_core = core.splitlines()
    # print(contentCore)
    i = 0
    while len(content_core) != i:
        find_item = content_core[i].split(':')
        #            print(find_item)
        # generate regular expression ignore case sentitive to search
        try:
            re_item_find = re.compile(find_item[0], re.IGNORECASE)
            content, number = re_item_find.subn(find_item[1], content)
        except:
            print 'compile error'
            content = string.replace(find_item[0], find_item[1])
        if number > 0:
            print 'Success replace ', number, find_item[0], 'to', find_item[1]
        i = i + 1
    write_file(dest_path, content)


def eng_to_eng1():
    #    FileCore = open(sys.argv[1], 'a+')
    #    FileTranslate = open(sys.argv[2], 'r+')

    # open file source
    Core = read_file(core_path)
    content = read_file(dest_path)
    CoreOriginal = Core.splitlines()
    # print(contentCore)
    i = 0
    while len(CoreOriginal) != i:
        # print CoreOriginal
        content = replace_str(content, CoreOriginal[i], CoreOriginal[i])  # Replace word
        i = i + 1

    # print(content)
    write_file(dest_path, content)


def main():
    print 'So tham so:', len(sys.argv), 'tham so.'
    print 'Danh sach tham so:', str(sys.argv)

    type_set = sys.argv[3]
#    type_set = '1'
    if type_set == '1':
        print 'Eng To Eng1'
        eng_to_eng1()
    elif type_set == '2':
        print 'Eng1 To Eng'
        eng1_to_eng()
    elif type_set == '3':
        print 'Vn To Eng'
        vn_to_eng()
    else:
        print 'Error'


print 'Usage: File_Core File_Translate Type'
print "Type:  1:EngToEng hv8, 2:Eng hv8 ToEng 2: VnToEng,"
core_path = sys.argv[1]
dest_path = sys.argv[2]
#core_path = "E:\\Auto\\TranslateTool\\Translate\\Translate\\test\\Core_eng.txt"
#dest_path = "E:\\Auto\\TranslateTool\\Translate\\Translate\\test\\Dest_eng.txt"

main()
