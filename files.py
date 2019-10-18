import os, sys

class FileCreator:

    py = '.py'
    c = '.c'
    cpp = '.cpp'
    txt = '.txt'
    json = '.json'


    file_extensions = {
            '.py' : py,
            'python' : py,
            'py' : py,
            'pyy' : py,
            'pyyy' : py,
            'ppy' : py,
            '.c' : c,
            'c' : c,
            '.txt' : txt,
            'txt' : txt,
            'text' : txt,
            'teext' : txt,
            'ttxt' : txt,
            'txtt' : txt,
            '.cpp' : cpp,
            'cpp' : cpp,
            'cplusplus' : cpp,
            'cplus' : cpp,
            'c++' : cpp,
            'c+' : cpp,
            '.json' : json,
            'json' : json,
            'jason': json,
            'dict' : json,
            'jon' : json,
            'jsn': json
    }

    file_name = ''
    folder_name = ''
    file_extension = ''
    found_file_extension = ''
    path = os.getcwd()

    def get_args(self, ext_id, fold_id):
        """Get arguments 3 and 4, set folder and extension names """
        try:
            self.file_extension = str(sys.argv[ext_id]).lower()
            self.file_extension = self.file_extensions[self.file_extension]
        except Exception:
            self.file_extension = '.txt'

        try:
            self.folder_name = str(sys.argv[fold_id])
        except Exception:
            self.folder_name = 'Default'

        try:
            self.file_name = str(sys.argv[2])
        except Exception:
            print("Files need a name")
            sys.exit()

    def make_file_and_fold(self):
        os.chdir('./root_files')

        self.file_name = self.file_name + self.file_extension
        if os.path.isdir('./' + self.folder_name):
            os.chdir('./' + self.folder_name)
        else:
            os.mkdir(self.folder_name)
            os.chdir('./' + self.folder_name)

        if not os.path.isfile('./' + self.file_name):
            open(self.file_name, 'a').close()

        os.system('vim ' + self.file_name)

    def find_file_in_fold(self, folder):
        if os.path.isdir(self.path + '/' + folder):
            self.path = self.path + '/' + folder
            self.find_file(self.file_name, '', self.path)
        else:
            self.path = self.find_file(folder, '', self.path)
            self.find_file(self.file_name, '', self.path)

        os.system('vim ' + self.path)


    def find_file(self, file_to_find, fold_to_search, path_):
        path_to_fold = ''
        file_exists = False

        for subdir, dirs, files in os.walk(path_ + fold_to_search):
            for d in dirs:
                if d.lower() == self.folder_name.lower():
                    path_to_fold = ''
                    path_to_fold = subdir + '/' + self.folder_name

            for f in files:
                f_name = ''
                for i in range(len(str(f))):
                    if len(str(self.file_name)) > i:
                        if str(f).lower()[i] == str(self.file_name).lower()[i]:
                            f_name = f_name + str(f)[i]
                            if len(f_name) > len(self.file_name) * 0.8:
                                self.path = os.path.join(subdir, f)
                                file_exists = True
                                break

        if not file_exists:
            self.path = os.path.join(path_to_fold, self.file_name + self.file_extension)
            open(self.path, 'a').close()



if __name__ == '__main__':
    files = FileCreator()
    cmd = str(sys.argv[1])
    if cmd == 'ffe':
        files.get_args(4, 3)
        files.make_file_and_fold()
    if cmd == 'of':
        files.get_args(4, 3)
        try:
            files.find_file_in_fold(str(sys.argv[3]))
        except Exception:
            files.find_file_in_fold('')
    if cmd == 'fe':
        files.get_args(3, 444)
        files.find_file_in_fold('')

