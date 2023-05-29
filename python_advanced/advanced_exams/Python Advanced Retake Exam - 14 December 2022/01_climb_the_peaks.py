from collections import deque

supplies = deque([int(x) for x in input().split(", ")])
stamina = deque([int(x) for x in input().split(", ")])

conquered_peaks = []

peaks_info = {
    80: "Vihren",
    90: "Kutelo",
    100: "Banski Suhodol",
    60: "Polezhan",
    70: "Kamenitza",
}

for difficulty_level, peak_name in peaks_info.items():

    while supplies:

        daily_supplies = supplies.pop()
        daily_stamina = stamina.popleft()

        daily_power = daily_stamina + daily_supplies

        if daily_power >= difficulty_level:
            conquered_peaks.append(peak_name)
            break


if len(conquered_peaks) == len(peaks_info):
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")

else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print(f"Conquered peaks: ")
    print('\n'.join(conquered_peaks))
