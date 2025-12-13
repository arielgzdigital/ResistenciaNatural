var header = document.getElementById('Header');

window.addEventListener('scroll', ()=> {

    var scroll = window.scrollY

    if (scroll>4) {
        header.style.backgroundColor = '#0B6640'
    } else {
        header.style.backgroundColor = 'transparent'
    }
})
