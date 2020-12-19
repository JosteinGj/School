num=[1.9/2 -1.9/2]
denom=[1 -0.9]
[h1,w1]=freqz(num,denom,10000,"whole")

plot(w1/pi,20*log10(abs(h1)))
ax = gca;
ax.YLim = [-20 1];

xlabel('Normalized Frequency (\times\pi rad/sample)')
ylabel('Magnitude (dB)')



num2=[0.1/2 -1.9/2]
denom2=[1 -0.9]
[h2,w2]=freqz(num2,denom2,10000,"whole")

plot(w2/pi,20*log10(abs(h2)))
ax=gca;

xlabel('Normalized Frequency (\times\pi rad/sample)')
ylabel('Magnitude (dB)')
