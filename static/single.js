var editBuyer = document.getElementById("edit-buyer");
var extraDiv = document.getElementById("extra");
editBuyer.onclick = ()=>{
    extraDiv.innerHTML = "";
    var newInput = document.createElement('input');
    newInput.id = "new-buyer"
    newInput.name = "new_buyer"
    var submit = document.createElement('button');
    submit.innerHTML = "SUBMIT"
    submit.type = "submit";
    
    extraDiv.appendChild(newInput);
    extraDiv.appendChild(submit)

}

