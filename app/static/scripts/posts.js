var PostsClass = React.createClass({

    getInitialState: function() {
        return {
            posts: {}
        };
    },

    componentDidMount: function() {
        $.get(this.props.source, function(result) {
            if (this.isMounted()) {
                this.setState({
                    posts: result.results
                });
            }
        }.bind(this));
    },

    render: function() {
        // make sure no js error, instead wait
        // sort of hacky, figure out better way
        try {
            var postNodes = this.state.posts.map(function(post){
                return (
                    <div>
                        <p>{post.author.nickname} says: <b>{post.body}</b></p>
                    </div>
                );
            });
        }
        catch(err) {
            console.log('waiting for ajax');
        }
        return (
            <div className="postsClass">
                {postNodes}
            </div>
        );
    }
});

React.render(
    <PostsClass source="/api" />,
    document.getElementById('posts')
);