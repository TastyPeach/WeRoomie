import React from 'react';
import {render} from 'react-dom';
import {BrowserRouter as Router, Route, Link, Switch, Redirect} from 'react-router-dom'
import 'semantic-ui-css/semantic.min.css';


// Include your new Components here
import Home from './components/Home/Home.jsx';
import SearchComp from './components/SearchComp.jsx';
import GroupDetail from './components/GroupDetail.jsx';

// Include any new stylesheets here
// Note that components' stylesheets should NOT be included here.
// They should be 'require'd in their component class file.
require('./styles/main.scss');

render(
    // Define your router and replace <Home /> with it!
    <Router>
        <Home>
        </Home>
    </Router>
    ,document.getElementById('app')
);


