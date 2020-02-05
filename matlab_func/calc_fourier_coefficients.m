function [f,c] = calc_fourier_coefficients(t,s)

c_fft = fft(s)./length(s);
len = floor(length(s)/2+1);
c = c_fft(1:len);

if mod(length(s),2) == 1    
    % odd signal length
    c(2:end) = 2.*c(2:end);
else
    % even signal length
    c(2:end-1) = 2.*c(2:end-1);
end

f = 1/(t(end)-t(1))/(length(s)/(length(s)-1)).*(0:len-1);

end