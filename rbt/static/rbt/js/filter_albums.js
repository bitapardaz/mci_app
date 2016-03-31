if (!$) {
    $ = django.jQuery;
}

$(document).ready(function () {
    $('#id_category').change(function () {
        $.getJSON('http://127.0.0.1:8000/mcirbt/filter_albums_per_cat/',{cat_id: $(this).val() , view: 'json'}, function (data) {
            var options = '<option value="">--------&nbsp;</option>';
            for (var i = 0; i < data.length; i++) {
              options += '<option value="' + data[i].id + '">' + data[i].farsi_name + '</option>';
            }
            $("#id_album").html(options);
            $("#id_album option:first").attr('selected', 'selected');
        });
        var options = '<option value="">Loading&nbsp;</option>';
        $("#id_album").html(options);
    });

});
