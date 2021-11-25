import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import Users from './users';
import Contact from './contact';
import { Route, Link, BrowserRouter, Routes } from 'react-router-dom';
import Notfound from './notfound';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';

const routing = (

  <div>
    <BrowserRouter>
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="collapse navbar-collapse">
          <ul className="navbar-nav mr-auto">
            <li className="nav-item">
              <Link className="nav-link" to="/">Home</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/usuarios">Users</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/contacto">Contact</Link>
            </li>
          </ul>
        </div>
      </nav>
      <Routes>
        <Route exact path="/" element={<App />} />
        < Route path="/usuarios/:id" element={<Users />} />
        <Route path="/contacto" element={<Contact />} />
        <Route path="*" element={<Notfound />} />
      </Routes>
    </BrowserRouter>
  </div>

)

ReactDOM.render(routing, document.getElementById('root'));

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
