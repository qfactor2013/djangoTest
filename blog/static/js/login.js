/*
$(function(){
    $("#login").click(function(e){
        e.preventDefault();
            var href = $(e.target).attr('href');
            if (href.indexOf('#') == 0) {
                $(href).modal('open');
            } else {
                $.get(href, function(data) {
                    $('<div class="modal-content">' + data + '</div>').modal('open').appendTo('body');
                });
            }
    })
})
*/
