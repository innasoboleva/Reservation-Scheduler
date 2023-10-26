function App() {

    return (
        <ReactRouterDOM.BrowserRouter>
            <ReactRouterDOM.Switch>
                <ReactRouterDOM.Route exact path="/" component={IndexPageContainer}>
                    
                </ReactRouterDOM.Route>
            </ReactRouterDOM.Switch>
        </ReactRouterDOM.BrowserRouter>
    );
}

ReactDOM.render(<App />, document.querySelector('#react-container'));