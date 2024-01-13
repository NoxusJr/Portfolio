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