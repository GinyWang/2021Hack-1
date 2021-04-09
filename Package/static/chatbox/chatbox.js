const send = document.getElementById("send")
const typing = document.getElementById("typing")
const chats = document.getElementById("chats")

var new_input = document.createElement("div")
new_input.setAttribute('class' , "my-chat")

chats.scrollTop = chats.scrollHeight

send.addEventListener('click',function(){

    if(typing.value != ''){
        new_input.innerHTML = typing.value
        chats.appendChild(new_input.cloneNode(true))
        chats.scrollTop = chats.scrollHeight
    }
})