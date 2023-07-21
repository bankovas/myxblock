/* Javascript for MyXBlock. */

function MyXBlock(runtime, element) {

    function checkAnswer(result) {
        if (result.isDone) {
            $("div.myxblock_block", element).html("<div>Ваш результат: " + result.score + "/" + result.maxScore + " баллов</div>")
        } else {
            $("input.answer", element).val("");
            $("p.score", element).text('Баллы: ' + result.score + '/' + result.maxScore);
            $("span.question", element).text(result.question);
        }
    }

    var handlerUrl = runtime.handlerUrl(element, 'check_answer');

    $('button.check', element).click(function (eventObject) {
        if ($('input.answer', element).val() != '') {
            $.ajax({
                type: "POST",
                url: handlerUrl,
                data: JSON.stringify({ "userAnswer": $("input.answer", element).val() }),
                success: checkAnswer
            });
        }
    });

    $(function ($) {
    });
}
