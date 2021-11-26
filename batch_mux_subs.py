import os

video_path = input("Insert full path of Videos Folder: ")
subs_path = input("Insert full puth of Subtitles Folder: ")

video_files = os.listdir(video_path)
subs_files = os.listdir(subs_path)
output_path = input("Insert full path of Output Folder: ")

for index in range(len(video_files)):
    current_video_abs_path = video_path + "\\" + video_files[index]
    current_subs_abs_path = subs_path + "\\" + subs_files[index]
    output_file_abs_path = output_path + "\\" + \
        os.path.basename(video_files[index])
    outp = 'ffmpeg -i ' + f'"{current_video_abs_path}"' + ' -i ' + f'"{current_subs_abs_path}"' + \
        ' -map 0 -map 1 -c copy -disposition:s:0 default ' + \
        f'"{output_file_abs_path}"'
    os.system(outp)
