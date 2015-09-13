var UrlList = React.createClass({
    getInitialState: function() {
        return {data: []};
    },
    handleUrlCommit: function(e) {
        var url = React.findDOMNode(this.refs.url).value.trim();
        var currentData = this.state.data;

        currentData.push(url);
        this.setState({data: currentData});
        React.findDOMNode(this.refs.url).value = '';
        return;
    },
    handleUrlDelete: function(urlValue, e) {
        var currentData = this.state.data;
        var index = currentData.indexOf(urlValue);
        
        currentData.splice(index, 1);
        this.setState({data: currentData});
        return;
    },
    render: function() {
        var that = this;
        var urlNodes = this.state.data.map(function(urlValue) {
            return (
                <div>
                    {urlValue}
                    <input type="button" value="Delete" onClick={that.handleUrlDelete.bind(null, urlValue)}/>
                </div>
            );
        });
        return (
            <div className="urlList">
                <div>
                    {urlNodes}
                </div>
                <div>
                    <input type="text" value={this.props.url} placeholder="URL" ref="url" />
                </div>
                <div>
                    <input type="button" value="Commit Urls" onClick={this.handleUrlCommit}/>
                </div>
            </div>
        );
    }
});

var PostForm = React.createClass({
    handleClick: function(e) {

        // gets the DOM and walks through it, builds our data we want to submit
        var node = React.findDOMNode(this.refs.urlList);
        var urlData = [];
        for(i=0; i < node.getElementsByTagName('span').length; i++) {
            urlData.push(node.getElementsByTagName("span")[i].childNodes[0].nodeValue);
        }
        

        // e.preventDefault();
        var title = React.findDOMNode(this.refs.title).value.trim();
        var content = React.findDOMNode(this.refs.content).value.trim();
        var postData = {title: title, body: content, picSource: urlData};

        console.log(postData);
        // location.reload();
        /*
        if(!title || !content || !url) {
            alert('There is a field that isn\'t filled out yet!');
            return;
        }

        $.ajax({
            url: this.props.url,
            dataType: 'json',
            type: 'POST',
            data: postData
        });*/
        return;
    },
    render: function() {
        return (
            <div className="postForm">
            <form onSubmit={this.handleSubmit}>
                <div>
                    <input type="text" placeholder="Title" ref="title" />
                </div>
                <div>
                    <input type="text" placeholder="Content" ref="content" />
                </div>
                <UrlList ref="urlList"/>
                <div>
                    <input type="button" value="Post" onClick={this.handleClick} />
                </div>
            </form>
            </div>
        );
    }
}); //<input type="submit" value="Post" />

React.render(
    <PostForm url="/api/post/post" />,
    document.getElementById('postForm')
);