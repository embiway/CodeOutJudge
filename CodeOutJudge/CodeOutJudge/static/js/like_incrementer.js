const blog_id = {{ blog.id }}

document.getElementById('like').onClick = () => {
    fetch('http://127.0.0.1:8000/blogs/' + blog_id)
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        if(data === 'You have already liked this block')
            alert(data)
        else
            document.getElementById('like-count').innerHTML = data
    }) 
    .catch ((err) => { console.log(err) });
}