var editBuyer = document.getElementById("edit-buyer");
var editAmount = document.getElementById("edit-amount");
var editProduct = document.getElementById("edit-product");
var editPrice = document.getElementById("edit-price");
var extraDiv = document.getElementById("extra");
console.log(extraDiv)
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

editAmount.onclick = ()=>{
    extraDiv.innerHTML = "";
    var newInput = document.createElement('input');
    newInput.id = "new-amount"
    newInput.name = "new_amount"
    var submit = document.createElement('button');
    submit.innerHTML = "SUBMIT"
    submit.type = "submit";
    
    extraDiv.appendChild(newInput);
    extraDiv.appendChild(submit)

}

editProduct.onclick = ()=>{
    extraDiv.innerHTML = "";
    var newInput = document.createElement('input');
    newInput.id = "new-product"
    newInput.name = "new_product"
    var submit = document.createElement('button');
    submit.innerHTML = "SUBMIT"
    submit.type = "submit";
    
    extraDiv.appendChild(newInput);
    extraDiv.appendChild(submit)

}

editPrice.onclick = ()=>{
    extraDiv.innerHTML = "";
    var newInput = document.createElement('input');
    newInput.id = "new-price"
    newInput.name = "new_price"
    var submit = document.createElement('button');
    submit.innerHTML = "SUBMIT"
    submit.type = "submit";
    
    extraDiv.appendChild(newInput);
    extraDiv.appendChild(submit)

}

document.getElementById("del-order").onclick = ()=>{
    fetch('/seller/'+seller+'/table/'+order_id,  {
        method: 'DELETE'
    })
    window.location.href = "/seller/"+seller+"/table"
}