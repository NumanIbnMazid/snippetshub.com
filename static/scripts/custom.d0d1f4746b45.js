// ******* scroll to top *******

$(window).scroll(function() {
    if ($(this).scrollTop() > 50 ) {
        $('.top-link:hidden').stop(true, true).fadeIn();
    } else {
        $('.top-link').stop(true, true).fadeOut();
    }
});
$(function(){$(".scroll").click(function(){$("html,body").animate({scrollTop:$("#top").offset().top},"1000");return false})})