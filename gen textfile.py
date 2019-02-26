import os 
import zipfile

def oat(pathed):
    print(pathed)
    if not os.path.exists(pathed):
        dirname = os.makedirs(pathed)
        print(dirname)
        kowoat = input("what you name \n")
        file = open("C:/Users/Anuchit/Desktop/kowoatkowoatz/oat.txt", "w")
        file.write(kowoat)
        file.close()
        print ("Generated !!")
    else:
        print("Directory already exists")

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))
            zipf.printdir()
    zipf.close()

if __name__ == '__main__':
    oat("C:/Users/Anuchit/Desktop/kowoatkowoatz")
    zipf = zipfile.ZipFile('C:/Users/Anuchit/Desktop/kowoatz.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('C:/Users/Anuchit/Desktop/kowoatkowoatz', zipf)
