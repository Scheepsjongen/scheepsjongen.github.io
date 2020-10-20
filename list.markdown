---
layout: page
title: Питання
permalink: /list/
---

<div class="question-pool"></div>
<style type="text/css">
    .question-pool .question .text {
        margin: 25px 0 0;
    }
    .question-pool .question .text:before {
        content: "Q: ";
    }
    .question-pool .question .answer:before {
        content: "A: ";
    }
    .question-pool .question .description {
        border: 1px solid #aaa;
        padding: 15px;
        display: none;
    }
</style>
<script src="/js/jquery-1.11.2.js"></script>
<script>
$(function () {
    var quizUrl = '/quiz/test.xml';
    $('.question-pool').load(quizUrl, function() {
        $('.question-pool > .quiz .question .answer[data-correct!="data-correct"]').remove();
        $('.question-pool .question .description').after('<a href="#" class="info">Пояснення</a>');
        $('.question-pool .question').after('<hr class="question-separator">');
        $('.question-pool .question a.info').click(function(e) {
            e.preventDefault();
            $(this).hide();
            $(this).closest('.question').children('.description').show(600);
        });
    });
});
</script>
