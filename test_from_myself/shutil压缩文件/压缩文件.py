import shutil

# help(shutil.make_archive)

# 打包后的文件名，文件格式，要打包的文件夹名称
shutil.make_archive("诗歌打包", "zip", "诗歌")

print("ok")