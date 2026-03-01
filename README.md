# Aegis-RF
Development of a modular anomaly detection system for complex RF (I/Q) signals, oriented toward spectrum surveillance and electronic warfare scenarios. The project includes advanced synthetic signal generation, interference and jamming modeling, spectral feature extraction, and unsupervised machine learning models for real-time anomaly detection.

## Overview

This project implements a complete simulation and anomaly detection framework for radio-frequency (RF) signals, with a focus on defense-oriented applications such as:

>Spectrum surveillance
>Intentional interference (jamming) detection
>Tactical communication link monitoring
>RF intrusion detection

The system operates on complex baseband I/Q signals generated under realistic mathematical models of digital modulation and channel effects.

## Technical Objectives

1. Design a synthetic RF signal generator supporting digital modulations (BPSK, QPSK, QAM).

2. Simulate realistic channel effects including AWGN and controlled degradations.

3. Model representative RF anomalies:
>Broadband jamming
>Narrowband interference bursts
>Unexpected carrier injection
>Abrupt modulation changes
>Frequency drift (oscillator instability simulation)

4. Build a signal processing pipeline:
>Windowing and segmentation
>Short-Time Fourier Transform (STFT)
>Spectral and statistical feature extraction

5.Implement unsupervised anomaly detection models:
>Isolation Forest
>One-Class SVM
>Autoencoders (dense and convolutional variants)

6.Evaluate performance using defense-relevant metrics:
>False Alarm Rate (FAR)
>ROC-AUC
>Detection delay
>Sensitivity to SNR variations


## System Architecture
The system is structured into modular layers:
1. Signal Simulation Layer
>Digital modulation generation
>Channel modeling
>Controlled anomaly injection

2. Preprocessing Layer
>Signal normalization
>Temporal segmentation
>Time-frequency transformation (STFT)

3. Feature & Modeling Layer
>Spectral and statistical feature extraction
>Unsupervised model training
>Anomaly scoring

4. Evaluation Layer
>Statistical performance analysis
>Robustness testing under varying SNR
>Model comparison and benchmarking


## Key Differentiators
>Explicit mathematical modeling of complex RF signals.
>Fully parameterizable and reproducible synthetic dataset generation.
>Clear separation between physical signal simulation and anomaly detection modeling.
>Emphasis on metrics critical for defense systems (minimizing false alarms).
>Designed with potential edge/embedded deployment in mind.


## Technologies
>Python (NumPy, SciPy, scikit-learn, PyTorch)
>Digital Signal Processing (DSP)
>Mathematical modeling of digital modulation schemes
>Modular and reproducible ML architecture design
