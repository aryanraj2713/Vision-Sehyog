import React from 'react'
import PropTypes from 'prop-types' 


export default function Navbar(props) {
  return (
    <div>
  <nav className={"navbar navbar-expand-lg navbar-dark bg-dark"}>
  <div className="container-fluid" >
    <a className="navbar-brand" href="/">{props.title}</a>
    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="true" aria-label="Toggle navigation">
      <span className="navbar-toggler-icon"></span>
    </button>
    <div className="collapse navbar-collapse" id="navbarSupportedContent">
      <ul className="navbar-nav me-auto mb-2 mb-lg-0">
        <li className="nav-item">
          <a className="nav-link active" aria-current="page" href="/"></a>
        </li>
        <li className="nav-item">
          <a className="nav-link" href="/">{props.About}</a>
        </li>
        
      </ul>

    </div>
  </div>
     </nav>
    </div>
  )
}

Navbar.propTypes = {
    title: PropTypes.string ,
    About: PropTypes.string
}