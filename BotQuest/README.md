<h2>Bot's Architecture</h2>
<ul>
    <li>
        <strong>config.py</strong>
        <ul></ul>
    </li>
    <li>
        <strong>bot.py</strong>
        <ul></ul>
    </li>
    <li>
        <strong>utils.py</strong>
        <ul></ul>
    </li>
    <li>
        <strong>models.py</strong>
        <ul>
            <li>class BaseModel(Model)</li>
            <li>class User(BaseModel): <i>Quest participants</i></li>
            <li>class Point(BaseModel): <i>Questions</i></li>
        </ul>
    </li>
    <li>
        <strong>views.py</strong>
        <ul>
            <li>def create_tables(): <i>used once to create database</i></li>
            <li>def signup(username): <i>used to add player to Users when /signup command comes</i></li>
            <li>def get_points(): <i>returns all data from Points to use it once game started</i><li>
        </ul>
    </li>
</ul>