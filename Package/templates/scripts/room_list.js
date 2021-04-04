window.onload = function(){
    set_events()
}


var amount = 5;
function set_events(){
const container = document.getElementById("container")

    var coupon_room = document.createElement('div')
    coupon_room.setAttribute("class" , "grid-item") 
    
    var bg = document.createElement('div')
    bg.setAttribute("class" , "bg")
    bg.innerHTML = "Subway"

    var title = document.createElement('div')
    title.setAttribute("class" , "title")
    title.innerHTML = "Let's have some fun in subway"

    var info = document.createElement('div')
    info.setAttribute("class" , "info")
        
    var date = document.createElement('div')
    date.setAttribute("class" , "date")
    date.innerHTML = "2021 April 23 16:00"

    var host = document.createElement('div')
    host.setAttribute("class" , "host")
    host.innerHTML = "Host: Philip Lai"

    var rate = document.createElement('div')
    rate.setAttribute("class" , "rate")
    rate.innerHTML = "Rate: 1 star"

    var join = document.createElement('button')
    join.setAttribute("type" , "button")
    join.setAttribute("class" , "join btn-primary")
    join.innerHTML = "Join"

    info.appendChild(date)
    info.appendChild(host)
    info.appendChild(rate)

    coupon_room.appendChild(bg)
    coupon_room.appendChild(title)
    coupon_room.appendChild(info)
    coupon_room.appendChild(join)

    for(i =0 ; i<amount ; i++){
        container.appendChild(coupon_room.cloneNode(true))
    }

}

