document.addEventListener('DOMContentLoaded', function(){

    const navItems = document.querySelectorAll('.nav-link');
    const blockBody = document.getElementById('blockBody');

    navItems.forEach(navlink =>{
        navlink.addEventListener('click',onNavClick);
    });


    function onNavClick(event){
        navItems.forEach(navlink => navlink.classList.remove('selected'));
        this.classList.add('selected');
    }

})