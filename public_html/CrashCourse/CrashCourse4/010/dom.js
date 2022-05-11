var form = document.getElementById('addForm');
var a = form[0].value; var b = form[0].value; var c = form[0].value; 
var itemList = document.getElementById('items');
var filter = document.getElementById('filter');

// Form submit event
form.addEventListener('submit', addItem);
// Delete event
itemList.addEventListener('click', removeItem);
// Filter event
filter.addEventListener('keyup', filterItems);

// Add item
function addItem(e){
  e.preventDefault();

  // Get input value
  var x = [1,2,3];
  //var newItem = document.getElementById('item').value;
  x[0] = document.getElementById('addForm')[0].value;
  x[1] = document.getElementById('addForm')[1].value;
  x[2]= document.getElementById('addForm')[2].value;
  console.log(x);


  // Create new li element
  var tr = document.createElement('tr');
  // Add class
  tr.className = 'list-group-item';
  console.log(tr)
  // Add text node with input value
  newItem = '<td>Larry the Bird</td>'
  tr.appendChild(document.createTextNode(newItem));
  
  //li.appendChild(document.createTextNode(newItem));
  var tr_str = '<td>Larry the Bird</td>';
  console.log(tr_str);
  tr.appendChild(document.createTextNode(tr_str));

  // Create del button element
  var deleteBtn = document.createElement('button');

  // Add classes to del button
  deleteBtn.className = 'btn btn-danger btn-sm float-right delete';

  // Append text node
  deleteBtn.appendChild(document.createTextNode('X'));

  // Append button to li
  tr.appendChild(deleteBtn);

  // Append li to list
  itemList.appendChild(tr);
}

// Remove item
function removeItem(e){
  if(e.target.classList.contains('delete')){
    if(confirm('Are You Sure?')){
      var li = e.target.parentElement;
      itemList.removeChild(li);
    }
  }
}

// Filter Items
function filterItems(e){
  // convert text to lowercase
  var text = e.target.value.toLowerCase();
  // Get lis
  var items = itemList.getElementsByTagName('li');
  // Convert to an array
  Array.from(items).forEach(function(item){
    var itemName = item.firstChild.textContent;
    if(itemName.toLowerCase().indexOf(text) != -1){
      item.style.display = 'block';
    } else {
      item.style.display = 'none';
    }
  });
}