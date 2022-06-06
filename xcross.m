clear all;
close all;
%clc;

[x,fs]=audioread('tu_falta_frase_5.wav');
[y,fs]=audioread('tu_falta.wav');
x=x(:,2);

y=y(:,2);

winvec_y = hamming(length(y));
winvec_x = hamming(length(x));

xdft = (x.*winvec_x);
ydft = (y.*winvec_y);


Wp = 250/(fs/2); Ws = 3000/(fs/2);
Rp = 3; Rs = 40;
%[n,Wn] = buttord(Wp,Ws,Rp,Rs);
%[b,a] = butter(n,Wn);




fNorm = 2000/ (fs/2);

[b,a] = butter(10, fNorm, 'high');


x_Lw = filtfilt(b, a, xdft);
y_Lw=filtfilt(b, a, ydft);
audiowrite('z_frase_1.wav', y_Lw, fs);


f0=(fft(y, 2^23));
f1=(fft(x, 2^23));

c=conj(f1).*f0;

figure(1);

subplot(5,1,1);
plot(x_Lw)
subplot(5,1,2);
plot(abs(f1));
subplot(5,1,3);
plot(y);
subplot(5,1,4);
plot(abs(f0));
subplot(5,1,5);
plot(abs((ifft(c))));

%%%%%%%%%%%%%%%%%%%
figure(2);
x_r=x;
y_r=y;
subplot(3,1,1);
N=length(x_r)+length(y_r);
R_xy = abs(ifft(fft(y_r,2^24).*conj(fft(x_r,2^24))));
[or,or]=max((R_xy(:)))
plot(R_xy);

subplot(3,1,2);
n_x=norm(x_r)
n_y=norm(y_r)
R_xy = abs(ifft(fft(x_r,N).*conj(fft(y_r,N)))./(n_x*n_y));
[Mr,Ir]=max((R_xy(:)))
plot(R_xy);

subplot(3,1,3);


x2 = y_r - mean(y_r);
y2 = x_r - mean(x_r);
phi_xy = abs((ifft(fftshift(fft(x2,N)).*conj(fftshift(fft(y2,N)))))./(norm(x2).*norm(y2)));
[Mj,Ij]=max((phi_xy(:)))

plot(phi_xy);