var nickname = 'Miguel';

var NameClass = React.createClass({
    render: function() {
        return (
            <div className="nameClass">
                <p>Hello, {this.props.data}</p>
            </div>
        );
    }
});

React.render(
    <NameClass data={nickname}/>,
    document.getElementById('nickname')
);