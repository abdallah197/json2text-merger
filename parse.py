import json, os, sys, glob
 directory = "change to you directory"
for path, dirnames, file_list in os.walk(directory): 

    with open('directory of the text file','a') as bert:
        for file in file_list:
            fullpath = os.path.join(path, file)

            with open(fullpath,'r', encoding = 'utf8') as json_file:
                text_file = json.load(json_file)
                # text_list = [text['postText'] for text in text_file['replies']]
                for text in text_file['text']:
                    bert.write(text['text_data'])





