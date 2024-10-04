#несущ файл.
#Нетекст
#без .txt
def open_l(filename:str) -> list[str]:
    """функция открывает файл и возвращает список строк или пустой список если произошла ошибка

    Args:
        filename (str): название файла который нужно открыть

    Returns:
        list[str] | []: список строк или пустой список
    """    
    try:
        if isinstance(filename, str) and filename[-4:]==".txt":
            list = open(filename)
            res = list.readlines()
            list.close()
            return res
        else:
            print("Введенные данные не являются тектом.")
            return []
    except FileNotFoundError:
        print("Файл не найден")
        return []


def split1(line:str) -> list[str]:
    """Функция делит список

    Args:
        line (str): строка в формате: 1234:Jozef:Miloslav:Hurban:Legal

    Returns:
        list[str] | []: список элементов строки: [1234, Jozef, Miloslav, Hurban, Legal] или ["x","x","x","x","x"] или []
    """    
    if isinstance(line,str):
        line1 = line.split(":")
        if len(line1)==5:
            return line1
        else:
            return ["x","x","x","x","x"]
    else:
        return []
#1234:Jozef:Miloslav:Hurban:Legal


def gen(line:str) -> str:
    """Функция генерирует юзернейм

    Args:
        line (str): строка в формате: 1234:Jozef:Miloslav:Hurban:Legal

    Returns:
        str: полученый юзернейм
    """    
    global users
    res = split1(line)
    if res != []:
        n1 = res[1]
        n2 = res[2]
        n3 = res[3]
        username= (n1[0]+n2[:1]+n3).lower()[:8]
        if username in users:
            dublicate = str(users[username])
            users[username]+=1
            username+=dublicate
        else:
            users[username]=1
        return username
    else:
        return "incorrectusername"



def allfunc(input_list:list[str],output:str):
    """Запускает все функции

    Args:
        input_list (list[str]): список названий инпут файлов
        output (str): файл куда записывается результат
    """
    lines = []
    for i in input_list:
        lines += open_l(i)
    result = []
    for i in lines:
        str2 = gen(i)
        res = i.index(":")
        str3 = i[0:res]
        str4 = i[res:]
        res1 = str3+":"+str2+str4
        result.append(res1)

        file=open(output, 'w')
        file.writelines(result)
        file.close()


# str1 = '1234:Jozef:Miloslav:Hurban:Legal'
# str2 = "jmhurban"
# res = str1.index(":")
# str3 = str1[0:res]
# str4 = str1[res:]
# print(str3+":"+str2+str4)
#print(gen("1234:Jozef:Miloslav:Hurbanqw223:Legal"))
#line1 = "1234:Jozef:Miloslav:Hurban:Legal

users = {}
if __name__ == "__main__":

    #print(allfunc(["input_file1.txt","input_file2.txt","input_file3.txt"],"output_file.txt"))

    import argparse

    parser = argparse.ArgumentParser(
                        prog='TestProg',
                        description='What the program does',
                        epilog='Text at the bottom of help')

    parser.add_argument('inputfiles', nargs="+")
    parser.add_argument('-o', '--output')

    args = parser.parse_args()
    allfunc(args.inputfiles,args.output)
