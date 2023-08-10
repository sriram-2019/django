<link rel="stylesheet" type="text/css" href="{%   static 'C:/Users/srira/OneDrive/Desktop/college/css/signup.css' %}"/>
<form method="POST">
    {% csrf_token %}
    {% if error_message %}
        <div class="error-message">{{ error_message }}</div>
        <input type="text" name="name" class="error"  placeholder="hello" value="{{ request.POST.name }}" style="border: 5px solid red;">
    {% else %}
        <input type="text" name="name" id="name" placeholder="hi">
{% endif %}
    <input type="submit" name="sub">
</form>