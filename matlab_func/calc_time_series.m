function [t,s] = calc_time_series(f,c)

% build dft format

if imag(c(end)) == 0
    % even signal length
    c_fft = [c(1) 0.5.*c(2:end-1) c(end) 0.5.*conj(flip(c(2:end-1)))];
else
    % uneven signal length
    c_fft = [c(1) 0.5.*c(2:end) 0.5.*conj(flip(c(2:end)))];
end
len = length(c_fft);

% inverse fft
s = ifft(c_fft.*len);

% time points
t = linspace(0,1/f(2)*(len-1)/len,len);

end