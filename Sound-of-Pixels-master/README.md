Fork from https://github.com/Lihit/Sound-of-Pixels

Sound-of-Pixels
Codebase for ECCV18 "The Sound of Pixels".


New contents:
1. Add data preprocessing part and fix the bug when creating data dirname(downloading data part). The space existing in data dirname will bring an error when loading the data.
2. Fix the bug in extracting audio part. ffmpeg requires a mp3 encoder(such as libmp3lame) when transform a mp4 file into mp3.
3. Edit the parameters "scripts/train_MUSIC.sh" according to the local environment.
4. Add clear.sh to restart downloading data if bugs happen.


Prepare video dataset.
    Running prepare_data.sh in dir data.

    Steps:
    a. Download MUSIC dataset from: https://github.com/roudimit/MUSIC_dataset
    b. Download videos.
    c. Extract frames at 8fps and waveforms at 11025Hz from videos. We have following directory structure:
    d. Make training/validation index files. It will create index files train.csv/val.csv with the following format:
    ./data/audio/acoustic_guitar/M3dekVSwNjY.mp3,./data/frames/acoustic_guitar/M3dekVSwNjY.mp4,1580
    ./data/audio/trumpet/STKXyBGSGyE.mp3,./data/frames/trumpet/STKXyBGSGyE.mp4,493
    For each row, it stores the information: AUDIO_PATH,FRAMES_PATH,NUMBER_FRAMES


Train the default model.
    Running ./scripts/train_MUSIC.sh


Evaluation
    a. (Optional) Download our trained model weights for evaluation.
        ./scripts/download_trained_model.sh
    b. Evaluate the trained model performance.
        ./scripts/eval_MUSIC.sh


Reference
If you use the code or dataset from the project, please cite:

    @InProceedings{Zhao_2018_ECCV,
        author = {Zhao, Hang and Gan, Chuang and Rouditchenko, Andrew and Vondrick, Carl and McDermott, Josh and Torralba, Antonio},
        title = {The Sound of Pixels},
        booktitle = {The European Conference on Computer Vision (ECCV)},
        month = {September},
        year = {2018}
    }
