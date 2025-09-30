[![Tests](https://github.com/google/zimtohrli/workflows/Test%20Zimtohrli/badge.svg)](https://github.com/google/zimtohrli/actions)

# Zimtohrli: A New Psychoacoustic Perceptual Metric for Audio Compression

Zimtohrli is a psychoacoustic perceptual metric that quantifies the human
observable difference in two audio signals in the proximity of
just-noticeable-differences.

In this project we study the psychological and physiological responses
associated with sound, to create a new more accurate model for measuring
human-subjective similarity between sounds.
The main focus will be on just-noticeable-difference to get most significant
benefits in high quality audio compression.
The main goals of the project is to further both existing and new practical
audio (and video containing audio) compression, and also be able to plug in the
resulting psychoacoustic similarity measure into audio related machine learning
models.

## Install
`pip install zimtohrli`
## Usage
Please note that the sampling frequency MUST be 48kHz. 
See code below for reference.
```
import librosa
from zimtohrli import mos_from_signals

signal_a, sr_a = librosa.load("audio_a.wav", sr=48000, mono=True)
signal_b, sr_b = librosa.load("audio_b.wav", sr=48000, mono=True)
mos = mos_from_signals(signal_a, signal_b)
```

## Design

Zimtohrli implements a perceptually-motivated audio similarity metric that
models the human auditory system through a multi-stage signal processing
pipeline. The metric operates on audio signals sampled at 48 kHz and produces a
scalar distance value that correlates with human perception of audio quality
differences.

### Signal Processing Pipeline

The algorithm consists of four main stages:

1. **Auditory Filterbank Analysis**: The input signal is processed through a
   bank of 128 filters with center frequencies logarithmically spaced from
   17.858 Hz to 20,352.7 Hz. These filters are implemented using a
   computationally efficient rotating phasor algorithm that computes spectral
   energy at each frequency band. The filterbank incorporates
   bandwidth-dependent exponential windowing to model frequency selectivity of
   the basilar membrane.

2. **Physiological Modeling**: The filtered signals undergo several transformations 
   inspired by auditory physiology:
   - A resonator model simulating the mechanical response of the ear drum and
     middle ear structures, implemented as a second-order IIR filter with
     physiologically-motivated coefficients
   - Energy computation through a cascade of three leaky integrators, modeling
     temporal integration in the auditory system
   - Loudness transformation using a logarithmic function with
     frequency-dependent gains calibrated to equal-loudness contours

3. **Temporal Alignment**: To handle temporal misalignments between reference
   and test signals, the algorithm employs Dynamic Time Warping (DTW) with a
   perceptually-motivated cost function. The warping path minimizes a weighted
   combination of spectral distance (raised to power 0.233) and temporal
   distortion penalties.

4. **Perceptual Similarity Computation**: The aligned spectrograms are compared
   using a modified Neurogram Similarity Index Measure (NSIM). This metric
   computes windowed statistics (mean, variance, covariance) over 6 temporal
   frames and 5 frequency channels, combining intensity and structure components
   through empirically-optimized non-linear functions inspired by SSIM.

### Key Parameters

- **Perceptual sampling rate**: 84 Hz (derived from [high gamma band](https://doi.org/10.1523/JNEUROSCI.5297-10.2011) frequency)
- **NSIM temporal window**: 6 frames (~71 ms)
- **NSIM frequency window**: 5 channels
- **Reference level**: 78.3 dB SPL for unity amplitude sine wave

The final distance metric is computed as 1 - NSIM, providing a value between 0
(identical) and 1 (maximally different) that correlates with subjective quality
assessments.
