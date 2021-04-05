var w, h;//idth = window.innerWidth;
var root = document.documentElement.style;
var css_style = document.querySelector('#css_style');

document.querySelector('.img__btn').addEventListener('click', function () {
    document.querySelector('.cont').classList.toggle('s--signup');
});
/*
var divs = document.querySelectorAll('div'), i;

for (i = 0; i < divs.length; ++i) {
  divs[i].style.color = "green";
}
 */
document.querySelector('#in_btn').addEventListener('click',
    function () {
        //document.body.style.background = 'red';
        var hid = document.querySelectorAll('.sign-up, .m--in');
        var app = document.querySelectorAll('.sign-in, .m--up');
        for (let i = 0; i < hid.length; i++) {
            hid[i].setAttribute('style', 'display:none');
        }
        for (let i = 0; i < app.length; i++) {
            app[i].setAttribute('style', 'display:block');
        }
        //document.querySelector('.sign-up').setAttribute('style', 'display:none');
        //document.querySelectorAll('.m--in').setAttribute('style', 'display:none');
        //document.querySelector('.sign-in').setAttribute('style', 'display:block');
        //document.querySelectorAll('.m--up').setAttribute('style', 'display:block');
    }
)
document.querySelector('#up_btn').addEventListener('click',
    function () {
        //document.body.style.background = 'yellow';
        var hid = document.querySelectorAll('.sign-in, .m--up');
        var app = document.querySelectorAll('.sign-up, .m--in');
        for (let i = 0; i < hid.length; i++) {
            hid[i].setAttribute('style', 'display:none');
        }
        for (let i = 0; i < app.length; i++) {
            app[i].setAttribute('style', 'display:block');
        }
        //document.querySelector('.sign-up').setAttribute('style', 'display:block');
        //document.querySelectorAll('.m--in').setAttribute('style', 'display:block');
        //document.querySelector('.sign-in').setAttribute('style', 'display:none');
        //document.querySelectorAll('.m--up').setAttribute('style', 'display:none');
    }
)


window.onload = function(){
    init();
}

function init() {
    set_var();
}

function reportWindowSize() {
    h = window.innerHeight;
    w = window.innerWidth;
}
function enableStylesheet(node) {
    node.setAttribute('rel', "stylesheet");
}
function disableStylesheet(node) {
    node.setAttribute('rel', "stylesheet alternate");
}
function set_var() {
    reportWindowSize();
    if (w < 625) {
        css_style.setAttribute('href', 'login2.css');
        //document.body.style.background = 'red';
        //alert('small');
        //disableStylesheet(css_for_large);
        //enableStylesheet(css_for_small);
    }
    else if (625 < w < 900) {
        //disableStylesheet(css_for_small);
        //enableStylesheet(css_for_large);
        css_style.setAttribute('href', 'login.css');
        var contw = w * 0.90;
        var contw_str = contw + 'px';
        var imgw = w * 0.28;
        var imgw_str = imgw + 'px';
        root.setProperty('--contW', contw_str);
        root.setProperty('--imgw', imgw_str);
    }
    //625<w<900
    else if (w > 900) {
        //disableStylesheet(css_for_small);
        //enableStylesheet(css_for_large);
        css_style.setAttribute('href', 'login.css');
        root.setProperty('--contW', '900px');
        root.setProperty('--imgw', '260px');
    }
    
}
window.addEventListener('resize', set_var);
/*--contW: 900px;
--imgW: 260px;*/