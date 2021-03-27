const subject_input = document.getElementById("subject-input")
const submit_button = document.getElementById("button")
const name_textbox = document.getElementById("name")
const ID_textbox = document.getElementById("ID")
result = document.getElementById("result")

submit_button.addEventListener('click' , function(){
    var name_input = document.createElement("div")
    name_input.textContent = name_textbox.value;
    var ID_input = document.createElement("div")
    ID_input.textContent = ID_textbox.value;
    var sub = document.createElement("div")
    sub.textContent = subject_input.value;
    result.appendChild(name_input)
    result.appendChild(ID_input)
    result.appendChild(sub)
})