$(document).ready(function () {
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });
    $(document).on('click', '#filter-btn', function () {
        $('#filter-form').show();
        $('#filter').show();
        $('#sort').hide();
    });

     $(document).on('click', '#sort-btn', function () {
         $('#sort-form').show();
         $('#sort').show();
         $('#filter').hide();
    });

    if (window.location.href.replace(/^(?:\/\/|[^\/]+)*\//, "") =='note/all/'){
        $(".features").show();
    }
    else{
        $(".features").hide();
    }


    var checkin = $('#dp1').datepicker().on('changeDate', function (ev) {
        if (ev.date.valueOf() > checkout.date.valueOf()) {
            var newDate = new Date(ev.date)
            newDate.setDate(newDate.getDate() + 1);
            checkout.setValue(newDate);
        }
        checkin.hide();
        $('#dp2')[0].focus();
    }).data('datepicker');
    var checkout = $('#dp2').datepicker()
        .on('changeDate', function (ev) {
        checkout.hide();
    }).data('datepicker');




    $(document).on('click', '.delete-btn', function () {
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
        jQuery(":radio").each(function () {
            $(this).attr('checked', false);
        });

        $("#notes_wrapper").load(location.href + " #notes");
    });

    $(document).on('click', '#title-filter-btn', function () {
        var value = $('.title-input').val();
        $('.note').each(function () {
            if ($(this).children('.note-title').text() != value) {
                console.log(value+1);
                console.log($(this).children('.note-title').text()+1);
                $(this).hide();
            }
            else {
                $(this).show();
            }
        })
    });

     $(document).on('click', '#date-filter-btn', function () {
         var month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
            ];

         var start = new Date($("#start-input").val());
         var finish = new Date($("#finish-input").val());
         start = month[start.getMonth()]+' '+ start.getDate()+', '+ start.getFullYear();
         finish = month[finish.getMonth()]+' '+ finish.getDate()+', '+ finish.getFullYear();
         finish = Date.parse(finish);
         start = Date.parse(start);
        $('.note').each(function () {
            var str = $(this).children('.note-date').text().replace('.','');
            var i = str.lastIndexOf(',');
            str  = str.substr(0,i);
            var date = Date.parse(str);
            if(date<=finish & date>=start){
                $(this).show();
            }
            else{
                $(this).hide();
            }

        })
    });

    $(document).on('click', '.favorite-btn', function () {
        var id = $(this).parent().attr("id").substr(4);
        $.ajax({
            type: 'POST',
            url: '/note/favorite/' + id,
            success: function (data) {
                if (data == 'True') {
                    $('#btn-img' + id).attr('src', '/static/img/favorite.png');
                }
                else {
                    $('#btn-img' + id).attr('src', '/static/img/not_favorite.png');
                    if ($("#favorite-filter-radio").prop("checked")) {
                        $("#note" + id).hide();
                    }
                }
            }
        });

    });


    $('input:radio[name="filter"]').change(
        function () {
            if ($(this).is(':checked')) {
                if ($(this).val() == 'category') {
                    $('#category-details').show();
                    $('#title-details').hide();
                    $('#date-details').hide();

                    $('input:radio[name="category"]').change(function () {
                        if ($(this).is(':checked')) {
                            var value = $(this).val();
                            $('.note').each(function () {
                                if ($(this).children('a').children('.note-category').text() != value) {
                                    $(this).hide();
                                }
                                else {
                                    $(this).show();
                                }
                            })
                        }
                    });
                }
                if ($(this).val() == 'title') {
                    $('#category-details').hide();
                    $('#title-details').show();
                    $('#date-details').hide();
                }
                if ($(this).val() == 'date') {
                    $('#category-details').hide();
                    $('#title-details').hide();
                    $('#date-details').show();


                }
                if ($(this).val() == 'favorite') {
                    $('#category-details').hide();
                    $('#title-details').hide();
                    $('#date-details').hide();
                    $('.note').each(function () {
                        if ($(this).children('.favorite-btn').children('.btn-img').attr('src') == '/static/img/not_favorite.png') {
                            $(this).hide();
                        }
                        else {
                            $(this).show();
                        }
                    })

                }
            }
        });
    $('input:radio[name="sort"]').change(function(){
        var $divs = $("div.note");
        if ($(this).is(':checked')) {
            if ($(this).val() == 'category') {
                    var orderedByCategoryDivs = $divs.sort(function (a, b) {
                        return $(a).find(".note-category").text() > $(b).find(".note-category").text();
                });
                $("#notes").html(orderedByCategoryDivs);

            }
            if ($(this).val() == 'date') {
                var str = $(this).children('.note-date').text().replace('.','');
                var i = str.lastIndexOf(',');
                str  = str.substr(0,i);
                var date = Date.parse(str);

            }
             if ($(this).val() == 'favorite') {

            }
        }
    })


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