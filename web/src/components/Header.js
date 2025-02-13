import { useState } from "react"

const Header = () => {
  const directHome = () => {
    window.location.href = "/";
  }

  return (
    <header>
      <div className="container">
        <div className="logo-container">
          <button onClick={directHome}>
            HOME
          </button>
        </div>
      </div>
    </header>
  );
}

export default Header;
