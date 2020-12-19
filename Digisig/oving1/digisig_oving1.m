t=4;
fs=8000;
n=0:1/fs:4;
f=6/8*fs;
sig=cos(2*pi*f*n);
%plot(n,sig)
soundsc(sig,fs)


% problem  5 a) and b)%
x=[1 2 3];
h1=[1 1 1];
n=[0:10];
h2=0.9.^n;
y1=conv(x,h1);
y2=conv(y1,h2);
%stem(h1)
%stem(h2)
%stem(y1)
%stem(y2)

y3=conv(x,h2);
y4=conv(y3,h1);
%stem(y4)


