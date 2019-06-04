import sys, getopt, re, string
from docx import Document
import docx2txt

document = Document()
from googletrans import Translator

proxy = {
    'http': 'http://username:password@1.1.1.1:1234',
    'https': 'http://username:password@1.1.1.1:1234',
}
translator = Translator()


def write_file(path_file, content):
    if path_file.endswith('.docx'):
        document.add_paragraph(content)
        document.save(path_file+"_translated.docx")
        return
    file_translate = open(path_file+"_translated.txt", 'w+', encoding='utf8')
    try:
        print('write content to file')
        file_translate.write(content)
    except:
        print('Error')
    # file_translate.flush()
    file_translate.close()


def read_file(path_file):
    if path_file.endswith('.docx'):
        text = docx2txt.process(path_file)
        return text
    # text = textract.process(path_file)
    file_core = open(path_file, 'r+', encoding="utf8")

    if file_core.mode == 'r+':
        content = file_core.read()
        file_core.close()

    return content


def replace_algo_addhv8(content, old, new):
    # generate regular expression ignore case sentitive to search

    try:
        count_item = 0
        re_item_find = re.compile(old, re.IGNORECASE)
        content_temp = re.compile(content, re.IGNORECASE)
        int_find = content.find(re_item_find.pattern)
        while int_find > -1:
            content, number = re_item_find.subn(content[int_find:int_find + len(old)] + 'HV8', content, count=1)
            int_find = content_temp.find(re_item_find.pattern, int_find + len(old) + 4)
            count_item = count_item + 1
    except:
        print('compile error')
        content = string.replace(content, old, new)
        return content
    if count_item > 0:
        print('Success replace ', count_item, old, 'to', new)
    return content


def replace_algo(content, old, new):
    # generate regular expression ignore case sentitive to search
    try:
        re_item_find = re.compile(old, re.IGNORECASE)
        content, number = re_item_find.subn(new, content)
    except:
        print('compile error')
        content = string.replace(content, old, new)
        return content
    if number > 0:
        print('Success replace ', number, old, 'to', new)
    return content


def replace_str(content, old, new):
    old = old.strip()
    StrOld = old.split(' ')
    if len(StrOld) > 1:
        content = replace_algo(content, old, 'hv8' + StrOld[0] + 'hv8 ' + 'hv8' + StrOld[1] + 'hv8')
        return content
    content = replace_algo(content, old, 'hv8' + new + 'hv8')
    return content


def convert_replace_str(content, old, new):
    content = replace_algo(content, 'hv8', '')
    return content


def vn_to_eng():
    content = read_file(source_path)
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
            print('compile error')
            content = string.replace(find_item[0], find_item[1])
        if number > 0:
            print('Success replace ', number, find_item[0], 'to', find_item[1])
        i = i + 1
    write_file(source_path, content)


def eng1_to_eng():
    # open file source
    Core = read_file(core_path)
    content = read_file(source_path)
    CoreOriginal = Core.splitlines()
    # print(contentCore)
    i = 0
    while len(CoreOriginal) != i:
        # print CoreOriginal
        content = convert_replace_str(content, CoreOriginal[i], CoreOriginal[i])  # Replace word
        i = i + 1

    # print(content)
    write_file(source_path, content)


def eng_to_eng1():
    #    FileCore = open(sys.argv[1], 'a+')
    #    FileTranslate = open(sys.argv[2], 'r+')

    # open file source
    Core = read_file(core_path)
    content_all = read_file(source_path)
    CoreOriginal = Core.splitlines()
    # print(contentCore)
    temp = 0
    for x in range(0, len(content_all) // 4000 + 2):
        print('one times')
        content = content_all[temp:temp + 4000]
        i = 0
        while len(CoreOriginal) != i:
            # print CoreOriginal
            content = replace_str(content, CoreOriginal[i], CoreOriginal[i])  # Replace word
            i = i + 1

        # print(content)
        translation = translator.translate(content, dest='vi')
        content = translation.text

        i = 0
        while len(CoreOriginal) != i:
            # print CoreOriginal
            content = convert_replace_str(content, CoreOriginal[i], CoreOriginal[i])  # Replace word
            i = i + 1

        """if (temp + 4000 ) > len(content_all):
            content_all[temp:len(content_all) - temp] = content
        else:
            #content_all[temp:temp + 4000] = content """

        if temp == 0:
            content_translated = content
        else:
            content_translated = content_translated + content

        # content_all[temp: temp+4000] = content
        temp = temp + 4000

    write_file(source_path, content_translated)


def main():
    print('So tham so:', len(sys.argv), 'tham so.')
    print('Danh sach tham so:', str(sys.argv))

    eng_to_eng1()


#   eng1_to_eng()

#    if type_set == '1':
#       print 'Eng To Eng1'
#        eng_to_eng1()
#    elif type_set == '2':
#        print 'Eng1 To Eng'
#        eng1_to_eng()
#    elif type_set == '3':
#        print 'Vn To Eng'
#        vn_to_eng()
#    else:
#        print 'Error'


print('Usage: File_Core File_Translate Type')
print("Type:  1:Eng To Enghv8, 2:Eng hv8 ToEng 3: VnToEng,")
# core_path = sys.argv[1]
# source_path = sys.argv[2]
# dest_path = sys.argv[3]
# type_set = sys.argv[4]

# type_set = '2'

core_path = "C:\\Users\\HuyHV\\Desktop\\Auto\\core_eng.txt"
source_path = "C:\\Users\\HuyHV\\Desktop\\Auto\\eng_goc.docx"


main()
