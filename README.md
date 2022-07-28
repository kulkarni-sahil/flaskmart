# flaskmart

## Lecture 1

- point 1:
<pre>
set FLASK_APP=market.py
flask run
</pre>

- point 2:
<pre>set FLASK_DEBUG=1</pre>

- point 3
<pre>Dynamic Routes!!!  ==> "angular brace" username "angular brace" </pre>

## Lecture 2

- create the **templates** directory
- **render_template()** this method is used to return an html file when an endpoint is called
- make use of **bootstrap** or any similar library to style the webpages

## Leacture 3

- JINJA Syntax -> {{ item_name }}
<pre>
.py file:
return render_template('market.html', item_name='phone')

in html:
<p>{{ item_name }}</p>
</pre>

- JINJA Syntax for logical operations
<pre>
items = [
    {'id': 1, 'name': 'sam'},
    {'id': 2, 'name': 'ram'},
    {'id': 3, 'name': 'pam'},
]

{% for item in items %}
    <tr>
        <td>{{ item.id }}</td>
        <td>{{ item.name }}</td>
    </tr>
{% endfor %}


{% for _ in l %}
    {{ _ }}
    {{ _.key_name }}
{% endfor %}
</pre>