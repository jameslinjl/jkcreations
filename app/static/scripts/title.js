var title = 'Home';

var TitleClass = React.createClass({
    render: function() {
        return (
            <div className="titleClass">
                <h1>{this.props.data} - microblog</h1>
            </div>
        );
    }
});

React.render(
    <TitleClass data={title}/>,
    document.getElementById('title')
);