let button = document.getElementById('changeLang')
let stateLang = localStorage.getItem('lang')



if (stateLang == null){
    localStorage.setItem('lang','pt')

} else if (stateLang == 'pt') {
    setImage("url('../IMG/ICONS/english.png')")


} else if (stateLang == 'en') {
    setImage("url('../IMG/ICONS/portugues.png')")
}



function toggleLang(){
    if (stateLang == 'pt'){
        localStorage.setItem('lang','en')
        location.reload()

    } else if (stateLang == 'en'){
        localStorage.setItem('lang','pt')
        location.reload()
    }
}


function setImage(url){
    button.style.background = url
    button.style.backgroundSize = 'cover'
    button.style.backgroundRepeat = 'no-repeat'
    button.style.backgroundPosition = 'center'
}