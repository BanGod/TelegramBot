<h2>Bot's Architecture</h2>
<ul>
    <li>
        <strong>config.py</strong>
    </li>
    <li>
        <strong>bot.py</strong>
        <ul>
            <li>def signup(message): <i>catches /signup command and calls reg_new_user from utils.py</i></li>
            <li>def game(message): <i>catches /game command and calls start_game from utils.py</i></li>
            <li>def process_callback(query): <i>processes answer, calls add_points from utils.py and 
                        calls give_next_question from utils.py if the quest is not over yet, 
                        otherwise calls finish_quest from utils.py</i></li>
            <li>def process_text(message): <i>processes any other messages</i></li>
        </ul>
    </li>
    <li>
        <strong>utils.py</strong>
        <ul>
            <li>def generate_markup(options): <i>returns qustion and inline-keyboard with answers</i></li>
            <li>def reg_new_user(username): <i>calls signup(username) from views.py when /signup command comes</i></li>
            <li>def start_game(): <i>calls get_points() from views.py when /game command comes;
                            creates and sends first question</i></li>
            <li>def give_next_question(): <i>creates and sends question using generate_markup</i></li>
            <li>def add_points(points): <i>adds points for the answer(if it is correct)</i></li>
            <li>def finish_quest(username): <i>once all the questions are answered prints username, 
                            his points and deletes him from User</i></li>
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
        </ul>
    </li>
</ul>