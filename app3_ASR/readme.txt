This folder contains the implementations of ASR system, following the demo session of book: Speech Recognition A-Z with Hands-On, by Learnkart Technology Private Limited.

[Chap1: Speech and Its Types]
1. Audio Data Analysis and Visualization  
   -> librosa: play audio, plot waveform & spectrogram
2. Digitizing and Recording of Speech Signal
   -> SpeechRecognition: speech to text
3. Human Speech Production
   -> gtts: text to speech
   
[Chap2: Automated Speech Recognition]
1. Sampling Theorem
   -> numpy: calculation of sampling time and wave function
   -> matplotlib: plot
2. Feature Extraction
   -> librosa: spectrogram, zero crossing, spectral centroid, spectral roll-off, MFCC
3. Force Alignment Expectation
   -> numpy: generate arrays of numbers
   -> scipy.stats: simulate the data distributions
   -> matplotlib: plot data distributions
4. Spectrum Analysis
   -> numpy: generate arrays of numbers
   -> pylab: plot
   -> scipy: time to frequency domain transformation
5. Speech to Text Model
   -> librosa, scipy, numpy, matplotlib: read, visualize & preprocess speech data (resample, select)
   -> sklearn: further process data to better fit trainign (encode, split train and test)
   -> keras: build & train model
