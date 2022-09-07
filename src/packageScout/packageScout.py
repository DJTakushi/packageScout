class packageScout():
    def testAlive(self):
        ### Debugging function ###
        print("packageScout testAlive()")

    def getPackageDictList(self):
        ### gets list of dictionaries of pacakges from file
        filename = "/var/lib/dpkg/status"
        readString = ""
        with open(filename,"r", encoding="UTF-8") as f:
            readString = f.read()

        ### squash encoding - problems occured with unencodable chars
        readString = readString.encode("ascii", 'ignore')
        readString = readString.decode("ascii")
        textBlock_l = readString.split("\n\n")

        dictList = []
        for i in textBlock_l:
            # replace block items with a single line
            # TODO fix this to get the whole description.  Not necessary for now, but very sad
            i.replace("\n ", " ")
            i.replace("\r ", " ")
            i.replace("\r\n ", " ")
            i.replace("\n\t", " ")

            #split up blocks by lines
            keyValLines = i.split("\n")

            dict_t = {}
            for j in keyValLines:
                try:
                    # split by colon
                    keyVal_t = j.split(": ")

                    # key is first val; value is second
                    dict_t[keyVal_t[0]] = keyVal_t[1]
                except:
                    pass
            dictList.append(dict_t)
        return dictList

    def getUserInstalledPackages(self, dictList):
        ### return thinned list the excludes packages with a "Source" key and have a priority "optional"
        chosenList = []
        for i in dictList:
            keys = i.keys()
            if "Source" not in keys:
                try:
                    if i["Priority"] == "optional":
                        chosenList.append(i)
                except:
                    pass
        return chosenList

    def displayPackagesInstalledByUser(self):
        # print the identified packages
        packageDictList = self.getPackageDictList()
        chosenList = self.getUserInstalledPackages(packageDictList)
        for i in chosenList:
            print(i['Package'])


if __name__ == "__main__":
    ps = packageScout()
    ps.displayPackagesInstalledByUser()
