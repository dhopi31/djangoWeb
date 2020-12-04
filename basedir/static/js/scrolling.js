$(window).scroll(function(){
    var scroll=$(window).scrollTop();
    console.log(scroll)
    document.getElementById("myBody").style.marginTop=( 0 - 0.1*scroll)+ "px";
    if(scroll>=30){
        $("#myNav").addClass("bg-dark");
    }else{
        $("#myNav").removeClass("bg-dark");
    }

    if(scroll>$(".product-package").offset().top-800){
        $(".product-package .card").each(function(i){
            setTimeout(function(){
                $(".product-package .card").eq(i).addClass("show");
            }, 300* (i+1) );
        });
        console.log('ok')
    }
    
});

$(document).ready(function(){
    console.log("document ready");
    $(".hot-item").hover(
        function(){
            $(this).addClass("shadow-lg").css("cursor", "pointer");
        }, 
        function(){
            $(this).removeClass("shadow-lg");
        }
    );
});

function visiblePassword(){
    var mata= document.getElementById('inputPassword');
    if (mata.type === "password"){
        mata.type = "text";
    } 
    else{
        mata.type = "password";
    }
}