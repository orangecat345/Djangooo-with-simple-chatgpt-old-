
var markdown = document.getElementById('mdInput').value; 
var html = marked(markdown); 
document.getElementById('htmlOutput').innerHTML = html; 
