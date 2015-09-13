var WordsClass = React.createClass({

    render: function() {
        return (
            <div className="wordsClass">
                <h1>{this.props.title}</h1>
                <p>{this.props.body}</p>
            </div>
        );
    }
});

// use this to render the album 
var AlbumClass = React.createClass({

    render: function() {
        // var thumbnailIndex = this.props.thumbnailIndex;
        var thumbnailIndex = 0; // temporary until db updates
        var thumbnailPictureSource = this.props.pictures[thumbnailIndex].source;
        var picArray = this.props.pictures;
        var postId = this.props.postId;

        picArray.splice(thumbnailIndex, 1);

        var thumbnailNode = (
            <a className="example-image-link" href={thumbnailPictureSource} data-lightbox={postId}>
                <img className="example-image" src={thumbnailPictureSource} alt="" />
            </a>
        );

        var picNodes = picArray.map(function(picture){
            return (
                <a className="example-image-link" href={picture.source} data-lightbox={postId} />
            );
        });

        return (
            <section>
                <div className="albumClass">
                    {thumbnailNode}
                    {picNodes}
                </div>
            </section>
        );
    }
});

// put it all together
var PostsClass = React.createClass({

    getInitialState: function() {
        return {
            posts: []
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
                        <WordsClass title={post.title} body={post.body} />
                        <AlbumClass pictures={post.pictures} postId={post.id} thumbNailIndex={post.thumbnailIndex} />
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
    <PostsClass source="/api/post/get" />,
    document.getElementById('posts')
);
