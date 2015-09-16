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
        var thumbnailIndex = this.props.thumbnailIndex;
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
        $.get(this.props.sourceGet, function(result) {
            if (this.isMounted()) {
                this.setState({
                    posts: result.results
                });
            }
        }.bind(this));
    },

    handlePostDelete: function(id, e) {
        var sourceDelete = this.props.sourceDelete + '?id=' + id;
        $.ajax({
            url: sourceDelete,
            type: 'DELETE'
        });
        location.reload();
        return;
    },

    render: function() {
        // make sure no js error, instead wait
        // sort of hacky, figure out better way
        var that = this;
        try {
            var postNodes = this.state.posts.map(function(post){                
                return (
                    <div>
                        <div>
                            Title: <input type="text" value={post.title} ref="title" />
                        </div>
                        <div>
                            Content: <input type="text" value={post.body} ref="content" />
                        </div>
                        <div>
                            ID: <input type="text" value={post.id} ref="id" />
                        </div>
                        <div>
                            <input type="button" value="Delete Post" onClick={that.handlePostDelete.bind(null, post.id)}/>
                        </div>
                        <AlbumClass pictures={post.pictures} postId={post.id} thumbnailIndex={post.thumbnailIndex} />
                    </div>
                );
            });
        }
        catch(err) {
            console.log(err);
        }
        return (
            <div className="postsClass">
                {postNodes}
            </div>
        );
    }
});

React.render(
    <PostsClass sourceGet="/api/post/get" sourceDelete="/api/post/delete" />,
    document.getElementById('postsEdit')
);
