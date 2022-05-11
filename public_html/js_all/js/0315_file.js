/*
function print_object(obj){
    var res= "<ul>"
    for(i in obj)
        res += '<li>' + i + ': ' + obj[i] + '</li>';
    res += '</ul>';
    document.write(res);
}
var object = document.getElementById("my_p")
print_object(object)
*/

var var_variable = 10
let let_variable = 10

console.log("var_variable: " + var_variable)
console.log("let_variable: " + let_variable)

setTimeout(function(){alert("Оповещение, через 10 сек");},10000)

setTimeout(function(){
    var string1 = "Задержка 6 сек"
    console.log(string1)
    var object = document.getElementById("my_p")
    var string0 = object.innerHTML
    var string1 = "Задержка 4 сек"
    var string2 = "object.innerHTML"
    object.innerHTML=(string0 + "<br>" + string1 + "<br>" + string2)
    },4000)

setTimeout(function(){console.log("Задержка 2 сек");},2000)


console.log("!. В JS вывод асинхронный ..")

//var answer = confirm ("Да?")
//console.log(answer);
