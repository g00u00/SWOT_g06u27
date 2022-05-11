var doAnalizeMy, doAnalizeNew, doCalculate, doSubmit 
var myVariable, newVariable 
var myVariableCalc, newVariableCalc, MyVariablesCalcSum = 0,  myVariablesCalc = []

doAnalizeMy = function(myVariable){
    console.log(myVariable)
    myVariableCalc = myVariable
    return(myVariable)
}    

doAnalizeNew = function(newVariable){
    console.log(newVariable)
    newVariableCalc = newVariable
    return(newVariable)
}

doCalculate = function(){
    myVariablesCalc.push(parseInt(myVariableCalc))
    MyVariablesCalcSum = MyVariablesCalcSum + parseInt(myVariableCalc)
    //document.write ("Введено:" + myVariableCalc + "; " + newVariableCalc + " <br>myVariablesCalc: "+ myVariablesCalc + "<br>сум:" + MyVariablesCalcSum)
    console.log ("Введено: " + myVariableCalc + "; " + newVariableCalc + " <br>myVariablesCalc: "+ myVariablesCalc + "<br>MyVariablesCalcSum:" + MyVariablesCalcSum)
    alert ("Введено:" + myVariableCalc + "; " + newVariableCalc + "  <br>myVariablesCalc: "+ myVariablesCalc + "  <br>MyVariablesCalcSum:" + MyVariablesCalcSum)
}
   
doSubmit = function(){
   let form = document.createElement('form');
   form.action = 'http://bim.nn2000.info/cgi-bin/f_submission.pl';
   form.method = 'get';
   form.innerHTML = '<input type="Hidden" name="MyVariablesCalcSum" value=' + MyVariablesCalcSum + '>';
   // the form must be in the document to submit it
   form.innerHTML +=  '<input type="Hidden" name="file_name" value="file.txt" ><input type="Hidden"  name="tmp1" value="1"><input type="Hidden" name="tmp2" value="2">'
   document.body.append(form);
   form.submit();
}
