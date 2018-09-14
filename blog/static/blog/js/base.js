 window.onload = function(){
    var url = window.location.href;
    if(url.indexOf('post') != -1){
        document.getElementById("navbarLi1").classList.add("active");
    }else if(url.indexOf('comic') != -1){
        document.getElementById("navbarLi2").classList.add("active");
    }else if(url.indexOf('poem') != -1){
        document.getElementById("navbarLi3").classList.add("active");
    }else if(url.indexOf('nature') != -1){
        document.getElementById("navbarLi4").classList.add("active");
    }else if(url.indexOf('funny') != -1){
        document.getElementById("navbarLi5").classList.add("active");
    }
}