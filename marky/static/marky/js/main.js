$(function() {
    var timer,
        $form = $('#preview-form'),
        $text = $('[name=markup]', $form),
        $area = $('#preview-area');

    // Various standalone key codes
    var TAB = 9,
        SPACE = 32;

    function postMarkup() {
        $.post($form.attr('action'), $form.serialize(), function(html) {
            $area.html(html).fadeIn(200);
        });
    }

    $text.on({
        keydown: function(event) {
            clearTimeout(timer);

            var key = event.which;

            // Insert real tab 
            if (key == TAB) {
                event.preventDefault();
                var start = this.selectionStart,
                    end = this.selectionEnd;

                var value = $text.val();
                $text.val(value.substring(0, start) + '    ' + value.substring(end));
                this.selectionStart = this.selectionEnd = start + 4;
            }

            // Ignore non-character keys: http://www.webonweboff.com/tips/js/event_key_codes.aspx 
            else if (key != SPACE && ((key > 13 && key < 46) || (key > 90 && key < 96) || (key > 111 && key < 188))) {
                return;
            }

            timer = setTimeout(function() {
                postMarkup();
            }, 500);
        }
    });

    // If the form is submitted explicitly, stop the timer and
    // submit the post the markup.
    $form.on('submit', function(event) {
        event.preventDefault();
        clearTimeout(timer);
        postMarkup();
    });

    postMarkup();
});
