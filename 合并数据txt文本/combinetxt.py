import os

def combineTxt(path:str)->bool:
    """合并txt文本
    """
    count = 0
    files = os.listdir(path)
    with open("combine.txt", "w") as fwrite:
        for file in files:
            f = os.path.join(path, file)
            with open(f, "r") as fopen:
                data = fopen.read()
                fwrite.write(data)
            count += 1

    return count


def main():
    path = "cmp"
    ret = combineTxt(path)
    print(ret)

if __name__ == '__main__':
    main()