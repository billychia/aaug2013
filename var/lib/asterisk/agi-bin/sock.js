socket= new WebSocket('ws://www.example.com:8000/somesocket');
socket.onopen= function() {
    socket.send('hello');
};
socket.onmessage= function(s) {
    alert('got reply '+s);
};
