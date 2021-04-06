var ac_list = document.getElementsByClassName("ac_sel")[0];
var tk_list = document.getElementsByClassName("tk_sel")[0];
var fd_list = document.getElementsByClassName("fd_sel")[0];
var sign = document.getElementsByClassName("show_sign");

function ac_list_display () {
  if (ac_list.style.display !== "flex"){
    ac_list.style.display = "flex";
    sign[0].innerHTML = "▾";
  } else {
    ac_list.style.display = "none";
    sign[0].innerHTML = "◂";
  }
}

function tk_list_display () {
  if (tk_list.style.display !== "flex"){
    tk_list.style.display = "flex";
    sign[1].innerHTML = "▾";
  } else {
    tk_list.style.display = "none";
    sign[1].innerHTML = "◂";
  }
}

function fd_list_display () {
  if (fd_list.style.display !== "flex"){
    fd_list.style.display = "flex";
    sign[2].innerHTML = "▾";
  } else {
    fd_list.style.display = "none";
    sign[2].innerHTML = "◂";
  }
}
