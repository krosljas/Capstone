clear; clc; close all; % Clear terminal and figures

[y, Fs] = audioread("micCheck.m4a"); % Load mace recording audio (m4a)
[y_, Fs_] = audioread("micCheck.wav"); % Load onboard mic audio (wav)
%sound(y, Fs);                % Play the audio. NOTE: wavplay is depracated.
stem(y);                     % Plot the signal as a function of discrete time.
xlabel('time (samples)');    % Label x axis
ylabel('magnitude');         % Label y axis
title('Mic Check 1 - Mac Recording Wavelet');

figure; stem(y_);
xlabel('time (samples)');    % Label x axis
ylabel('magnitude');         % Label y axis
title('Mic Check 1 - Microphone Wavelet');

dt = 1/Fs;                     % seconds per sample
dt_ = 1/Fs_;
StopTime = 2;                  % seconds
t = (0:dt:StopTime-dt)';
t_ = (0:dt_:StopTime-dt_)';
N = size(t,1);
N_ = size(t_, 1);
dF = Fs/N;                      % hertz
dF_ = Fs_/N_;
f = -Fs/2:dF:Fs/2-dF;           % hertz
f_ = -Fs_/2:dF_:Fs_/2-dF_;
%Plot the spectrum:
Y = fftshift(fft(y(1:StopTime*Fs)));
figure; plot(f,abs(Y)/N);
xlabel('Frequency (Hz)');    % Label x axis
ylabel('Magnitude');         % Label y axis
title('Mic Check 1 - Mac Recording Spectrogram');

Y_ =fftshift(fft(y_(1:StopTime*Fs_)));
figure; plot(f_, abs(Y_)/N_);
xlabel('Frequency (Hz)');    % Label x axis
ylabel('Magnitude');         % Label y axis
title('Mic Check 1 - Microphone Spectrogram');



