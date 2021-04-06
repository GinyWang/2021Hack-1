var nowDate;
var EvDate = document.getElementById('EvDate');
var EvTime = document.getElementById('EvTime');
var warn = document.querySelector('.warn');
EvDate.addEventListener('input', setTimeRange);
EvTime.addEventListener('invalid', function () {
    EvTime.value = '';
   
   }
)

window.onload = function () {
    init();
    
};
function init(){
    setDateMin();
}

function setDateMin(){
    var today = new Date();
    var yyyy = today.getFullYear();
    var mon = today.getMonth() + 1; //January is 0!
    if (mon < 10) { mon = '0' + mon; }
    var dd = today.getDate(); 
    if (dd < 10) { dd = '0' + dd; }
    nowDate = yyyy + '-' + mon + '-' + dd;
    EvDate.setAttribute("min", nowDate)
}

function setTimeRange() {
    if (EvDate.value === EvDate.min) {
        //alert('today!');
        setTimeMin();
    }
    else {
        EvTime.removeAttribute("min");
        EvTime.removeAttribute("max")
    }

}
function setTimeMin() {
    var today = new Date();
    var hh = today.getHours();
    if (hh < 10) { hh = '0' + hh; }
    var min = today.getMinutes();
    if (min < 10) { min = '0' + min; }
    var nowTime = hh + ':' + min;
    EvTime.setAttribute("min", nowTime);
    EvTime.setAttribute("max", "23:59")
}

 