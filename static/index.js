$('document').ready(function() {

    // This function is supposed to send data to the backend and retrieve it from the front end
    $('#share').on('click', function() {
        $.getJSON($SCRIPT_ROOT + '/submit', {
            sentence: $('input[name="sent"]').val()
        }, function(data) {
            
            $('#lexicon').append('<p>' + data.word_cats.NOUN + '</p>');
        });
    });

});