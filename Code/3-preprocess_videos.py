from moviepy.editor import VideoFileClip
import os


# Function to convert MP4 files to WAV files
def convert_mp4_to_wav(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through files in the input folder
    for file_name in os.listdir(input_folder):
        # convert mp4 files only
        if file_name.endswith(".mp4"):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(
                output_folder, os.path.splitext(file_name)[0] + ".wav"
            )

            # Load MP4 file and extract audio
            video = VideoFileClip(input_path)
            audio = video.audio

            # Write audio to WAV file
            audio.write_audiofile(
                output_path,
                codec="pcm_s16le",
                bitrate="320k",
                ffmpeg_params=["-ar", "44100"],
            )


# Convert MP4 files in each folder to WAV files
input_folders = ["train_raw/", "test_raw/", "dev_raw/"]
output_folders = ["train_wav", "test_wav", "dev_wav"]

for i in range(len(input_folders)):
    # convert_mp4_to_wav(input_folders[i], output_folders[i])
    print("Uncomment line above to run code")
