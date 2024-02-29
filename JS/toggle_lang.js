let button = document.getElementById('changeLang')
let stateLang = localStorage.getItem('lang')

let textEnglish = {
    'articles':'See articles',
    'h1-main':'Welcome to my portfolio',
    'p-main':'My name is George, Im a full-stack programmer with command of <span class="emphasis-text">Python</span>, <span class="emphasis-text">PhP</span> and <span class=" emphasis-text">JavaScript</span>',
    'my-skills':'My Skills',
    'my-main-projects':'Main Projects',
    'footer-blackstudio':'<a href="https://blackstudiodev.vercel.app/" target="_blank">Get to know <span class="emphasis-text">Black Studio</span></a',
    'footer-rights':'©️ 2024 George Júnior. All rights reserved.',
    'my-others-projects':'Others Projects',
}



if (stateLang == null){
    localStorage.setItem('lang','pt')

} else if (stateLang == 'pt') {
    setImage("url('../IMG/ICONS/english.png')")


} else if (stateLang == 'en') {
    setImage("url('../IMG/ICONS/portugues.png')")
    toEnglish(textEnglish)
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


function toEnglish(textEnglish){
    let articleText = document.getElementById('article')
    let h1Main = document.getElementById('h1-main')
    let pMain = document.getElementById('p-main')
    let h1MySkills = document.getElementById('my-skills')
    let h1MyMainProjects = document.getElementById('my-main-projects')
    let footerBlackStudio = document.getElementById('footer-blackstudio')
    let rights = document.getElementById('footer-rights')
    let h1OthersProjects = document.getElementById('my-others-projects')

    articleText.textContent = textEnglish['articles']
    h1Main.innerHTML = textEnglish['h1-main']
    pMain.innerHTML = textEnglish['p-main']
    h1MySkills.innerHTML = textEnglish['my-skills']
    h1MyMainProjects.innerHTML = textEnglish['my-main-projects']
    footerBlackStudio.innerHTML = textEnglish['footer-blackstudio']
    rights.innerHTML = textEnglish['footer-rights']
    h1OthersProjects.innerHTML = textEnglish['my-others-projects']
}