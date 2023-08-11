
    $(window).on("load", function() {
        $('body').addClass('loaded');
    });

    $(function(){
        
        /*************** Navigation *****************/

        const tmMainNav = $("#tm-main-nav");

        $('.navbar-toggler').click(function(e) {
            e.stopPropagation();
            tmMainNav.toggleClass('show');
        });

        $("html").click(function(e) {
            $("#tm-main-nav").removeClass("show");
        });
    });
