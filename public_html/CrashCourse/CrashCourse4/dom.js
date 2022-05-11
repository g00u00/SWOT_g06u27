var form = document.getElementById('addForm');
//var a = form[0].value; var b = form[1].value; var c = form[3].value; 
var tboby = document.getElementById('tbody')
var itemList = document.getElementById('items');
var filter = document.getElementById('filter');

// Form submit event
form.addEventListener('submit', addItem);
// Delete event
tbody.addEventListener('click', removeItem);
// Filter event
filter.addEventListener('keyup', filterItems);

// Add item
function addItem(e){
  e.preventDefault();
  
  // Get input value
  var x = [1,2,3];
  //var newItem = document.getElementById('items').outerHTML;
  x[0] = document.getElementById('addForm')[0].value;
  x[1] = document.getElementById('addForm')[1].value;
  x[2]= document.getElementById('addForm')[2].value;
  x[3]= document.getElementById('addForm')[3].value;
  console.log(x);


  // Create new li element
  var tr = document.createElement('tr');
  // Add class
  tr.className = '';
   tr.innerHTML = `
  <tr>
  <td>${x[0]}<input type="hidden" name="v1" value=${x[0]}></td>
  <td>${x[1]}<input type="hidden" name="v2" value=${x[1]}></td>
  <td>${x[2]}<input type="hidden" name="v3" value=${x[2]}></td>
  <td>${x[3]}<input type="hidden" name="v4" value=${x[3]}></td>
  `;

  // Add text node with input value
  tbody.appendChild(tr);
 //tr.appendChild(document.createTextNode(newItem));
  //tr.appendChild(document.createTextNode(x));
  //tr.appendChild(document.createTextNode(x));
  var td = document.createElement('td');
  td.innerHTML="<td></td>"
  tr.appendChild(td);  
  var deleteBtn = document.createElement('button');
  deleteBtn.className = 'btn btn-danger btn-sm float-right delete';
  deleteBtn.innerHTML = `
  X
  `;
   td.appendChild(deleteBtn);

  // Append li to list
  //itemList.appendChild(tr);
}

// Remove item
function removeItem(e){
  if(e.target.classList.contains('delete')){
    if(confirm('Are You Sure?')){
      var li = e.target.parentElement.parentElement;
      tbody.removeChild(li)
    }
  }
}

