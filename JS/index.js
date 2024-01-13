// BOTÃO RETORNAR AO TOPO

const btn = document.getElementById("btnTop")

btn.addEventListener("click", function(){
    window.scrollTo(0,0)
})

document.addEventListener('scroll', ocultar)

function ocultar(){
    if(window.scrollY >10){
        btn.style.display = "flex"
    } else {
        btn.style.display = "none"
    }
}

// TROCA DE TEMA (LIGHT MODE - DARK MODE)

if (localStorage.getItem('tema') == 'dark'){
    document.documentElement.classList.toggle('dark')
}

function trocarModo(){
    return document.documentElement.classList.toggle('dark')
}

function salvarModo(){
    if (document.documentElement.classList == 'dark'){
        localStorage.setItem('tema','dark')
    } else {
        localStorage.setItem('tema','light')
    }
}