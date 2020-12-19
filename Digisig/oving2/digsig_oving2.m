t=1;
fs=4000;
n=0:1/fs:t;
f=1/4*fs;
sig=cos(2*pi*f*n);
%plot(n,sig)
soundsc(sig,fs)

t=1;
fs=1500;
n=0:1/fs:t;
f=1/6*fs;
sig=cos(2*pi*f*n);
%plot(n,sig)
soundsc(sig,fs)