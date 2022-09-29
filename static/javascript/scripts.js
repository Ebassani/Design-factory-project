let menu = 1;

function mobile_menu() {
    if (menu % 2 !== 0) {
        openMenu();
        menu++;
    } else {
        closeMenu();
        menu--;
    }
}

function openMenu() {
    document.getElementById('bar').style.transform = 'rotate(-45deg)';
    document.getElementById('bar2').style.transform = 'scaleY(0)';
    document.getElementById('bar3').style.transform = 'rotate(45deg)';

    document.getElementById('bar').style.backgroundColor = 'snow';
    document.getElementById('bar2').style.backgroundColor = 'snow';
    document.getElementById('bar3').style.backgroundColor = 'snow';

    document.getElementById('bar').style.top = '0.8rem';
    document.getElementById('bar').style.width = '1.85rem';
    document.getElementById('bar3').style.width = '1.85rem';
    document.getElementById('bar3').style.top = '-0.1rem';

    document.getElementById('overlay').style.left = '0';
}

function closeMenu() {
    document.getElementById('bar').style.backgroundColor = 'black';
    document.getElementById('bar2').style.backgroundColor = 'black';
    document.getElementById('bar3').style.backgroundColor = 'black';

    document.getElementById('bar').style.transform = 'rotate(0)';
    document.getElementById('bar2').style.transform = 'scaleY(1)';
    document.getElementById('bar3').style.transform = 'rotate(0)';

    document.getElementById('bar').style.top = '0';
    document.getElementById('bar3').style.top = '0';
    document.getElementById('bar').style.width = '1.4rem';
    document.getElementById('bar3').style.width = '1.4rem';

    document.getElementById('overlay').style.left = '-100%';
}