

<form action="/addTodoItem/" method = "post">{% csrf_token %}
    <input type="text" name="content">
    <input type="submit" value="Add Todo Item">
</form> 

<li>