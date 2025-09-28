import numpy as np


def play_sound(
    frequency: float | list[float] = 440.0,
    duration_s: float = 0.5,
    blend_duration_s: float = 0.025,
    sample_rate: int = 44100,
    volume: float = 1.0,
):
    """
    Generate and plays a sound on the server's audio output.

    Can play a single frequency or a sequence of frequencies laid out
    evenly across the total duration.

    Args:
        frequency: A single frequency (Hz) or a list of frequencies.
                   If a list, each frequency will be played in sequence.
        duration_s: Total duration of the sound in seconds.
        sample_rate: The sample rate for audio generation.
        volume: The volume, from 0.0 (silent) to 1.0 (full).
    """
    import simpleaudio as sa

    if isinstance(frequency, int | float):
        frequencies = [float(frequency)]
    else:
        frequencies = [float(f) for f in frequency]

    if not frequencies:
        return

    volume = np.clip(volume, 0.0, 1.0)
    total_samples = int(duration_s * sample_rate)

    duration_per_note = duration_s / len(frequencies)
    samples_per_note = int(duration_per_note * sample_rate)

    blend_samples = min(int(blend_duration_s * sample_rate), samples_per_note)

    instantaneous_freq_array = np.zeros(total_samples)

    current_sample_pos = 0
    prev_freq = frequencies[0]  # Start with the first frequency

    for i, current_freq in enumerate(frequencies):
        # The number of samples for this specific segment
        # Use min to handle the last segment precisely
        num_samples_for_this_segment = min(samples_per_note, total_samples - current_sample_pos)
        if num_samples_for_this_segment <= 0:
            break

        segment_end_pos = current_sample_pos + num_samples_for_this_segment

        # Create the blend ramp
        if i > 0 and blend_samples > 0:
            blend_ramp = np.linspace(prev_freq, current_freq, blend_samples)
            blend_end_pos = current_sample_pos + blend_samples
            instantaneous_freq_array[current_sample_pos:blend_end_pos] = blend_ramp
            # Fill the rest of the segment with the target frequency
            instantaneous_freq_array[blend_end_pos:segment_end_pos] = current_freq
        else:
            # No blend for the first note or if blend is disabled
            instantaneous_freq_array[current_sample_pos:segment_end_pos] = current_freq

        prev_freq = current_freq
        current_sample_pos = segment_end_pos

    # --- 3. Generate Waveform from Frequency Array ---
    # The core of the smooth transition:
    # 1. Calculate the phase change for each sample: `d(phase) = 2 * pi * f(t) * dt`
    #    where dt = 1 / sample_rate
    # 2. Integrate (cumsum) to get the continuous phase over time.
    # 3. Apply sin() to the continuous phase array.
    phase_increment = (2 * np.pi / sample_rate) * instantaneous_freq_array
    continuous_phase = np.cumsum(phase_increment)

    full_tone = np.sin(continuous_phase)

    # --- 4. Normalize and Play ---
    max_abs_val = np.max(np.abs(full_tone))
    if max_abs_val > 0:
        audio_data = (full_tone / max_abs_val * volume * 32767).astype(np.int16)
    else:
        audio_data = full_tone.astype(np.int16)

    if audio_data.size == 0:
        return

    sa.play_buffer(audio_data, 1, 2, sample_rate)
