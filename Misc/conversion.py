import subprocess
import os

def convert_hd_to_sd(input_file, output_file):
    # ffmpeg command to resize video to SD resolution (640x480)
    ffmpeg_command = [
        'ffmpeg',
        '-i', input_file,
        '-vf', 'scale=640:480',
        '-c:a', 'copy',  # Copy audio codec without re-encoding
        '-c:v', 'libx264',
        '-crf', '23',  #
        '-preset', 'medium',
        '-movflags', 'faststart',
        output_file 
    ]

    # Execute ffmpeg command
    subprocess.run(ffmpeg_command)


hd_video_dir = r'/hd.mp4'

sd_video_dir = r'/video1.mp4'

os.makedirs(sd_video_dir, exist_ok=True)

# List HD video files in the input directory
hd_video_files = [f for f in os.listdir(hd_video_dir) if os.path.isfile(os.path.join(hd_video_dir, f))]

# Convert each HD video file to SD resolution
for hd_video_file in hd_video_files:
    input_file = os.path.join(hd_video_dir, hd_video_file)
    output_file = os.path.join(sd_video_dir, hd_video_file)
    convert_hd_to_sd(input_file, output_file)

print("Conversion completed successfully!")
