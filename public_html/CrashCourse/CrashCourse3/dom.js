var itemInput = document.querySelector('input[type="text"]');
var select = document.querySelector('select');
var form = document.querySelector('form');

//itemInput.addEventListener('keyup', runEvent);
itemInput.addEventListener('input', runEvent);
select.addEventListener('change', runEvent);

form.addEventListener('submit', runEventSubmit);

function runEvent(e){
    //e.preventDefault();//submit
    console.log('EVENT TYPE: '+e.type);
    console.log(e.target);
    console.log(e.target.value);
}

function runEventSubmit(e){
    e.preventDefault();//submit
    console.log('EVENT TYPE: '+e.type);
    console.log(e.target);
    console.log(e.target.value);
    console.log(e.target[0].value);
    console.log(e.target[1].value);
}

