
function setfilename(val) {
    filename = val.split('\\').pop().split('/').pop();
    filename = filename.substring(0, filename.lastIndexOf('.'));
    document.getElementById('wpName').innerHTML = filename + '.pdf';

}
