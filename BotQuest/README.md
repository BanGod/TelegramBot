<h2>Bot's Architecture</h2>
<ul>
    <li>
        <strong>config.py</strong>
    </li>
    <li>
        <strong>bot.py</strong>
        <ul>
            <li>class BaseModel(Model)</li>
            <li>class User(BaseModel): <i>Quest participants</i></li>
            <li>class Point(BaseModel): <i>Questions</i></li>
        </ul>
    </li>
    <li>
        <strong>utils.py</strong>
        <ul>
            <li>def generate_markup(options): <i>returns qustion and inline-keyboard with answers</i></li>
            <li>def reg_new_user(username): <i>calls signup(username) from views.py when /signup command comes</i></li>
            <li>def start_game(): <i>calls get_points() from views.py when /game command comes;
                             creates and sends first question</i></li>
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