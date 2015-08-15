var posts = [
    {
        'author': {'nickname': 'John'},
        'body': 'Beautiful day in Portland!'
    },
    {
        'author': {'nickname': 'Susan'},
        'body': 'The Avengers movie was so cool!'
    }
];

var PostsClass = React.createClass({
    render: function() {
        var postNodes = this.props.data.map(function(post){
            return (
                <div>
                    <p>{post.author.nickname} says: <b>{post.body}</b></p>
                </div>
            );
        });
        return (
            <div className="postsClass">
                {postNodes}
            </div>
        );
    }
});

React.render(
    <PostsClass data={posts}/>,
    document.getElementById('posts')
);