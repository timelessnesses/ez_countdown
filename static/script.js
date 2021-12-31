var tz = Intl.DateTimeFormat().resolvedOptions().timeZone

function Countdown() {
    const request = new XMLHttpRequest();
    request.open("GET", `/time?tz=${tz}`);
    request.send();
    request.onreadystatechange = (e) => {
        try{
            data = JSON.parse(request.responseText)
        }catch(e){
            ; // SHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
        }
        document.getElementById('days').innerHTML = data.day;
        document.getElementById('hours').innerHTML = data.hour;
        document.getElementById('minutes').innerHTML = data.min;
        document.getElementById('secs').innerHTML = data.sec;
    };
};
window.onload = function() {
    setInterval(Countdown, 100);
};