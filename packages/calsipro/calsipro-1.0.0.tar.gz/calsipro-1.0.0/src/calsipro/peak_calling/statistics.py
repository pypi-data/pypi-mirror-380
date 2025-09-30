import numpy as np

def call_peaks(s, sigma=1.5):
    std = np.std(s)
    peaks_detected = s / std >= sigma
    peaks = _find_peak_edges(peaks_detected)
    peaks_detected = _join_close_peaks(s, peaks_detected, peaks)
    peaks = _find_peak_edges(peaks_detected)

    peaks = [push_peak(peak, s) for peak in peaks]

    return peaks

def push_peak(peak, signal):
    start, end = peak
    m = len(signal)
    while start > 0 and signal[start-1] < signal[start]:
        start -= 1
    while end < m-1 and signal[end+1] < signal[end]:
        end += 1
    return start, end

def _find_peak_edges(peak_detected):
    i = 0
    peaks = []
    while i < len(peak_detected):
        idx_start = np.argmax(peak_detected[i:])
        if (idx_start == 0) and not peak_detected[i]:
            break
        idx_end = np.argmin(peak_detected[i+idx_start:])
        if idx_end == 0:
            idx_end = len(peak_detected[i+idx_start:])
        peaks.append((i+idx_start, min(i+idx_start+idx_end, len(peak_detected))))
        i = i + idx_start+idx_end+1
    return peaks

def _join_close_peaks(signal, peak_detected, peaks, N=1):
    peak_detected = peak_detected.copy()
    for p1, p2 in zip(peaks, peaks[1:]):
        p1_start, p1_end = p1
        p2_start, p2_end = p2

        if p2_start - p1_end <= N:
            peak_detected[p1_end:p2_start] = True
    return peak_detected


