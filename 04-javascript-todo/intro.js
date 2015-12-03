console.log("JavaScript successfully loaded");

var addToTDL = function addToTDL(s){
    var tdl = document.getElementById("todolist");
    var n = document.createElement("li");
    n.innerHTML = s;
    tdl.appendChild(n);
    var tdlItems = todolist.children;
    var length = tdlItems.length;
    tdlItems[length-1].addEventListener("click",moveToDL(length-1));
};

var removeFromTDL = function removeFromTDL(n){
    var items = todolist.children;
    items[n].remove();
};

var moveToDL = function moveToDL(n){
    var tdlItem = document.getElementsByTagName("li")[n];
    var dl = document.getElementById("donelist");
    var doneItem = document.createElement("li");
    doneItem.innerHTML = tdlItem.innerHTML;
    dl.appendChild(doneItem);
    removeFromTDL(n);
    //var dlItems = donelist.children;
    //var length = dlItems.length;
    //dlItems[length-1].addEventListener("click",moveToTDL(length-1));
};

var removeFromDL = function removeFromDL(n){
    var items = donelist.children;
    items[n].remove();
};

var moveToTDL = function moveToTDL(n){
    var dlItem = document.getElementsByTagName("li")[n];
    var tdl = document.getElementById("todolist");
    var todoItem = document.createElement("li");
    todoItem.innerHTML = dlItem.innerHTML;
    tdl.appendChild(todoItem);
    removeFromDL(n);
    //var tdlItems = todolist.children;
    //var length = tdlItems.length;
    //tdlItems[length-1].addEventListener("click",moveToDL(length-1));
}

var addInput = function addInput(e){
    console.log(e);
    console.log(this);
    var input = document.getElementById("TDLinput");
    var text = input.value;
    e.stopImmediatePropagation();
    addToTDL(text);
};

var addButton = document.getElementById("addButton");
addButton.addEventListener("click",addInput);
