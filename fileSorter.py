import os
import shutil


class FileSorter:
    def __init__(self, path, dest, prefix):
        self.origin = path
        self.destination = dest
        self.prefix = prefix if prefix != "" else dest.split("/")[-1]
        self.files = self.getFiles()
        self.count = len(self.files)

    def getFileExtension(self, file):
        return os.path.splitext(file)[1][1::]

    def getFiles(self):
        files = os.scandir(self.origin)
        fileNames = []
        for file in files:
            if (file.is_file()):
                fileNames.append(file.name)
        return fileNames

    def createDirs(self):
        dirPath = self.destination + f"/{self.prefix}"
        for file in self.files:
            if (not os.path.exists(dirPath+f"-{self.getFileExtension(file)}")):
                os.makedirs(dirPath+f"-{self.getFileExtension(file)}")

    def moveFiles(self):
        dirPath = self.destination+f"/{self.prefix}"
        for file in self.files:
            shutil.move(self.origin+f"/{file}", dirPath +
                        f"-{self.getFileExtension(file)}")

    def start(self):
        self.createDirs()
        self.moveFiles()
