$(document).ready(function() {
    let currentUrl = window.location.href;
    $(".nav-link").each(function() {
        if (this.href === currentUrl) {
            $(".nav-link").removeClass("active");
            $(this).addClass("active");
        }
    });
});
