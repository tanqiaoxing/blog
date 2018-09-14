$(function(){
    $('.moreBtn').click(function(){
        $('html,body').animate({
            scrollTop:$('.second').offset().top}, 500);
    });

    $('.fable-text li').hover(function(){
    	$(this).find("i").removeClass("fa-bell-o");
    	$(this).find("i").addClass("fa-bell");
    }, function(){
		$(this).find("i").removeClass("fa-bell");
    	$(this).find("i").addClass("fa-bell-o");
	});

	$('.poem-text li').hover(function(){
        $(this).find("i").removeClass("fa-folder-open-o");
    	$(this).find("i").addClass("fa-folder-open");
    }, function(){
		$(this).find("i").removeClass("fa-folder-open");
    	$(this).find("i").addClass("fa-folder-open-o");
	});

    $('.img-text li').hover(function(){
        $(this).find("div .mask").addClass("none");
        $(this).find("p").addClass("color-orange");
    }, function(){
        $(this).find("div .mask").removeClass("none");
        $(this).find("p").removeClass("color-orange");
    });

})