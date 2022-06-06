clc;
clear all;
close all;


[x,fs]=audioread('tu_falta.wav');
[y,fs]=audioread('tu_falta_frase_4.wav');
y_r=x(:,2);

x_r=y(:,2);





%%%%%%%%%%%%%%%%%%%
figure(2);

subplot(3,1,1);
m=sum(x_r.^2);
N=length(x_r)+length(y_r);
R_xy = abs(ifft(fft(y_r,2^24).*conj(fft(x_r,2^24))))./m;
[or,or]=max((R_xy(:)))
plot(R_xy);

subplot(3,1,2);
n_x=norm(x_r)
n_y=norm(y_r)
R_xy = abs(fftshift(ifft(fft(x_r,N).*conj(fft(y_r,N)))./(n_x*n_y)));
[Mr,Ir]=max((R_xy(:)))
plot(R_xy);

subplot(3,1,3);


x2 = y_r - mean(y_r);
y2 = x_r - mean(x_r);
phi_xy = abs((ifft(fftshift(fft(x2,N)).*conj(fftshift(fft(y2,N)))))./(norm(x2).*norm(y2)));
[Mj,Ij]=max((phi_xy(:)))

plot(phi_xy);