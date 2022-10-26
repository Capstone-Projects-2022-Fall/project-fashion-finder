import './polyfills.jsx';
import ReactDOM from 'react-dom';
import React from 'react';
import Home from './home.jsx';

const App = () => {
  return <Home />;
}

ReactDOM.render(<App />, document.getElementById('root'));