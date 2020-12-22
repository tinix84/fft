clear all
close all
clc

addpath('../mfiles/')

vpk=40;
t=linspace(0,1,10000);
s=vpk*square(2 * pi * 5 * t);
plot(t,s)

[f, c] = calc_fourier_coefficients(t, s);
figure
loglog(f, abs(c), 'DisplayName', "calc fourier coefficients")
legend
