/* Javascript for MyXBlock. */

function MyXBlock(runtime, element) {

    function checkAnswer(result) {
        //Отобразить новый вопрос
        //Отобразить новые баллы
        $("p.score", element).text('hi');
    }

    var handlerUrl = runtime.handlerUrl(element, 'check_answer');

    $('button.check', element).click(function(eventObject) {
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({"userAnswer": $("input.answer", element).val()}),
            success: checkAnswer
        });
    });

    $(function ($) {
    });
}
