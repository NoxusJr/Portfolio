if (localStorage.getItem('theme') == 'dark'){
    document.documentElement.classList.toggle('dark')
}


function removeTransition(element){
    element.style.transition = ''
}


function toggleTheme(){
    let elements = document.querySelectorAll('*')

    elements.forEach((element) =>{
        element.style.transition = '0.3s'
    });

    document.documentElement.classList.toggle('dark')

    if (document.documentElement.classList == 'dark'){
        localStorage.setItem('theme','dark')
    } else {
        localStorage.setItem('theme','light')
    }

    elements.forEach((element)=>{
        setTimeout(()=>{
            removeTransition(element)
        },1000)
    })
}