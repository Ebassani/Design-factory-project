function mobile_menu() {
    document.getElementById('bar').style.transform = 'rotate(-45deg)';
    document.getElementById('bar2').style.transform = 'scaleY(0)';
    document.getElementById('bar3').style.transform = 'rotate(45deg)';
    document.getElementById('bar').style.backgroundColor = 'snow';
    document.getElementById('bar2').style.backgroundColor = 'snow';
    document.getElementById('bar3').style.backgroundColor = 'snow';
    document.getElementById('bar').style.top = '0.8rem';
    document.getElementById('bar').style.width = '1.85rem';
    document.getElementById('bar3').style.top = '0';
    document.getElementById('bar3').style.width = '1.85rem';


}