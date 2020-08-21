function output = echo_gen(input, fs, delay, amp)
delay_sample_n = round(delay * fs);
vect_and_echo = zeros(delay_sample_n + length(input), 1);
vect_no_echo = vect_and_echo;

for i = 1:length(input)
    vect_and_echo(i + delay_sample_n) = input(i) * amp;
    vect_no_echo(i) = input(i);
end

full_sound = vect_no_echo + vect_and_echo;
range = abs(full_sound);
maxrange = max(range)

if maxrange > 1
    full_sound = full_sound/maxrange;
end

output = full_sound;
end

% Load splat which adds y and Fs to the workspace
load splat
% Call echo_gen to create the new audio data
output = echo_gen(y, Fs, 0.25, 0.6);
% The time between points is 1/Fs;
dt = 1/Fs;
% Plot the original sound
plot(0:dt:dt*(length(y)-1), y)
% Plot the new data to see visualize the echo
figure
plot(0:dt:dt*(length(output)-1), output)

% sound(output, Fs) % Uncomment in MATLAB to listen to the new sound data