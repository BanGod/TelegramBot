<h2>Bot's Architecture</h2>
<ul>
    <li>
        <strong>config.py</strong>
    </li>
    <li>
        <strong>bot.py</strong>
    </li>
    <li>
        <strong>utils.py</strong>
        <ul>
            <li>def generate_markup(options, number): <i>returns qustion and inline-keyboard with answers</i></li>
            <li>def signup(username): <i>calls <strong>signup(username)</strong> from views.py when /signup command comes</i></li>
            <li>def start_game(): <i>calls <strong>get_points()</strong> from views.py when /game command comes;
                            calls <strong>send_question(0, chat_id)</strong></i></li>
            <li>def send_question(number, chat_id): <i>creates and sends question using generate_markup</i></li>
            <li>def process_callback(query): processes answer, calls <strong>add_points()</strong> from views.py;
                calls <strong>send_question()</strong> if the quest is not over yet, 
                otherwise calls <strong>finish_quest()</strong> from views.py
            </li>
            <li>def process_text(message): processes any other messages</li>
        </ul>
    </li>
    <li>
        <strong>models.py</strong>
        <ul>
            <li>class BaseModel(Model)</li>
            <li>class User(BaseModel): <i>quest participants</i></li>
            <li>class Point(BaseModel): <i>questions</i></li>
        </ul>
    </li>
    <li>
        <strong>views.py</strong>
        <ul>
            <li>def create_tables(): <i>used once to create database</i></li>
            <li>def signup(username): <i>used to add player to Users</i></li>
            <li>def get_points(): <i>returns all data from Points to use it once game started</i></li>
            <li>def add_points(score): <i>adds points for the answer(if it is correct)</i></li>
            <li>def finish_quest(): <i>once all the questions are answered prints username, 
                            his points and logs him out of quest</i></li>
        </ul>
    </li>
</ul>