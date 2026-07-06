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
1. Signal Generator
>High-fidelity simulation of digital modulations (BPSK, QPSK, QAM) and controlled channel degradation (AWGN, fading).

2. Signal Processor
>Real-time feature extraction using Short-Time Fourier Transform (STFT) to convert complex I/Q data into time-frequency representations.

3. Anomaly Detector
>Deep learning-based unsupervised engine (Autoencoder) that learns the "normal" spectral footprint and identifies deviations based on reconstruction error (MSE).

4. Evaluation Engine
>Metrics-focused suite measuring Probability of Detection (Pd) vs. False Alarm Rate (Pfa) under varying SNR scenarios.


## Key Differentiators
>Defense-Oriented Metrics: Focus on robust performance under low-SNR conditions.
>Modular Pipeline: Easily swappable models and signal generators.
>Edge-Ready Design: Architected for potential deployment on embedded hardware (FPGA/SoC) for real-time tactical surveillance.


## Performance Analysis
he system evaluates performance using:
1. ROC-AUC Curves
>Visualizing detection capability across different noise floors.
2. Reconstruction MSE
>Using the Mean Squared Error of the autoencoder to define the anomaly threshold.


## Technologies
>Python (NumPy, SciPy, scikit-learn, PyTorch)
>Digital Signal Processing (DSP)
>Mathematical modeling of digital modulation schemes
>Modular and reproducible ML architecture design
