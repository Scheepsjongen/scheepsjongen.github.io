---
layout: page
---

<style type="text/css">
    .quiz .question:after {
        content: "Запитання № " attr(number);
        color: #828282;
    }
</style>
<script src="/js/jquery-1.11.2.js"></script>
<script src="/js/knockout-2.2.1.js"></script>
<script src="/js/bootstrap.min.js"></script>
<script src="/js/jsQuizEngine.js"></script>
<script>
    var quizEngine = null;
    var quizUrl = '/quiz/test.xml';
    $(function () {
        quizEngine = jsQuizEngine($('#jsQuizEngine'), { quizUrl: quizUrl });
    });
</script>

<section>
    <div id="jsQuizEngine">
        <section data-bind="visible: !quizStarted()">
            <div class="jumbotron">
                    <div class="banner">
                    <div class="container-text">
                        <h1>Тест судноводія</h1>
                        <p>Тест для перевірки теоретичних знань кандидатів на отримання посвідчення судноводія малого/маломірного судна (unofficial)</p>
                        <button class="btn btn-primary btn-lg" data-bind="click: startQuiz">Почати</button>
                    </div>
                    <img src="/img/lines.png" alt="ship">
                </div>
            </div>
        </section>
        <section class="container-text">
            <section class="quiz" data-bind="visible: quizStarted() &amp;&amp; !quizComplete()">
                <div>Question <span data-bind="text: currentQuestionIndex"></span> of <span data-bind="text: questionCount"></span></div>
                <div class="progress">
                    <div class="progress-bar" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" data-bind="attr: { 'aria-valuenow': currentProgress }, style: { width: currentProgress() + '%' }"></div>
                </div>
                <button class="btn btn-default" data-bind="click: movePreviousQuestion, disable: currentQuestionIsFirst">Назад</button>
                <button class="btn btn-default" data-bind="click: showCurrentQuestionHint, visible: currentQuestionHasHint()">Show Hint</button>
                <button class="btn btn-default" data-bind="click: showCurrentQuestionAnswer">Показати відповідь</button>
                <button class="btn btn-primary" data-bind="click: moveNextQuestion, disable: currentQuestionIsLast, visible: !currentQuestionIsLast()">Далі</button>
                <button class="btn btn-primary" data-bind="click: calculateScore, visible: currentQuestionIsLast">Завершити</button>
                <div class="question-pool"></div>
            </section>
            <section class="score" data-bind="visible: quizComplete">
                <p>Результат:</p>
                <h2 data-bind="text: quizTitle"></h2>
                <h3 data-bind="text: quizSubTitle"></h3>
                <div>Questions: <span data-bind="text: questionCount"></span></div>
                <div>Date: <span data-bind="text: calculatedScoreDate"></span></div>
                <div>Overall Score: <span data-bind="text: calculatedScore"></span>%</div>
                <div>Correct Questions: <span data-bind="text: totalQuestionsCorrect"></span></div>
                <div class="progress">
                    <div class="progress-bar" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" data-bind="attr: { 'aria-valuenow': calculatedScore }, style: { width: calculatedScore() + '%' }, css: { 'progress-bar-success': quizPassed, 'progress-bar-danger': !quizPassed() }"></div>
                </div>
                <div class="pass-indicator">
                    <h4 data-bind="css: { 'text-success': quizPassed, 'text-danger': !quizPassed() }">
                        <span data-bind="visible: quizPassed">PASS</span>
                        <span data-bind="visible: !quizPassed()">FAIL</span>
                    </h4>
                </div>
                <a href="#" onclick="location.reload()" class="btn btn-primary btn-lg" data-bind="click: startQuiz">Наново</a>
                <div style="margin-top: 45px;">
                    <blockquote class="blockquote">
                        <p>Перевірка теоретичних знань вважається успішною, якщо кандидат надав
                        <b>вірні відповіді на 80% запитань</b> екзаменаційного білета,.</p>
                        <p>Одне тестове завдання включає <b>30 тестових питань</b>.
                        Кожне питання передбачає три-чотири варіанти відповіді, один з яких є правильним.
                        Загальний час для проведення тестування становить 30 хвилин.</p>
                        <div class="blockquote-footer">
                            <cite title="Source Title">ПОЛОЖЕННЯ
                            про порядок видачі посвідчення судноводія малого/маломірного судна</cite>
                        </div>
                    </blockquote>
                </div>
            </section>
        </section>
        <section class="container-text" data-bind="visible: !quizStarted()">
            <div class="section-content">
                <div class="content">
                    <h4>Права на лодку</h4>
                </div>
                <div class="advertising-block">
                    <h6>Долучайтесь поліпшити тест</h6>
                    <p>Запропонуйте у коментарях можливі правки до пояснень та відповідей</p>
                    <a href="https://scheepsjongen.github.io/2020/10/20/welcome-to-scheepsjongen.html#disqus_thread" class="btn btn-primary btn-lg">Перейти</a>
                </div>
            </div>
        </section>
    </div>
</section>
