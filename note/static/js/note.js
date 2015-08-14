$(document).ready(function(){
        $.ajaxSetup({
     beforeSend: function(xhr, settings) {
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     }
});
    $(document).on('click','.delete-btn', function() {
        var id = $(this).parent().attr("id").substr(4);
        $.ajax({
            type: 'POST',
            url: '/note/delete/' + id,
            dataType: 'json',
            data: {'note_id': id}
        });

        $('#category-details').hide();
        $('#title-details').hide();
        $('#date-details').hide();
        jQuery( ":radio").each(function(){
            $(this).attr('checked', false);
        });

        $("#notes_wrapper").load(location.href + " #notes");
    });

    $(document).on('click','#title-filter-btn', function() {
        var value = $('.title-input').val();
        $('.note').each(function(){
            if ($(this).children('.note-title').text() != value){
                console.log(value);
                console.log($(this).children('.note-title').text());
                $(this).hide();
            }
            else{
                $(this).show();
            }
        })
    });

    $(document).on('click','.favorite-btn', function() {
        var id = $(this).parent().attr("id").substr(4);
        $.ajax({
            type: 'POST',
            url: '/note/favorite/' + id,
            success: function (data) {
                if (data == 'True') {
                    $('#btn-img' + id).attr('src','/static/img/favorite.png');
                }
                else {
                    $('#btn-img' + id).attr('src','/static/img/not_favorite.png');
                    if ($("#favorite-filter-radio").prop("checked")){
                        $("#note"+id).hide();
                    }
                }
            }
        });

    });


$('input:radio[name="filter"]').change(
    function(){
        if ($(this).is(':checked')) {
            if($(this).val() == 'category') {
                $('#category-details').show();
                $('#title-details').hide();
                $('#date-details').hide();

                $('input:radio[name="category"]').change(function () {
                    if ($(this).is(':checked')) {
                        var value = $(this).val();
                        $('.note').each(function(){
                            if ($(this).children('.note-category').text() != value){
                                $(this).hide();
                            }
                            else{
                                 $(this).show();
                            }
                        })
                    }
                });
            }
            if($(this).val() == 'title'){
                $('#category-details').hide();
                $('#title-details').show();
                $('#date-details').hide();
            }
             if($(this).val() == 'date'){
                 $('#category-details').hide();
                 $('#title-details').hide();
                 $('#date-details').show();


            }
             if($(this).val() == 'favorite'){
                 $('#category-details').hide();
                 $('#title-details').hide();
                 $('#date-details').hide();
                  $('.note').each(function(){
                      if ($(this).children('.favorite-btn').children('.btn-img').attr('src') == '/static/img/not_favorite.png'){
                          $(this).hide();
                      }
                      else{
                          $(this).show();
                      }
                  })

            }
        }
    });
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}