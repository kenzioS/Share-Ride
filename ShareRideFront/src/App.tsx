import { useState } from 'react'
import './App.css'

function App() {
  const [isMenuOpen, setIsMenuOpen] = useState(true)

  return (
    <div className="page">
      <header className="site-header">
        <a className="brand" href="/">
          ShareRide
        </a>
        <nav className="nav" aria-label="Main navigation">
          <button type="button" className="nav-button">
            Profile
          </button>
        </nav>
      </header>

      <div className="page-body">
        <aside className={`side-menu${isMenuOpen ? '' : ' collapsed'}`}>
          <nav className="side-nav" aria-label="Side menu">
            <button type="button" className="side-button">
              Rides
            </button>
            <button type="button" className="side-button">
              Reviews
            </button>
          </nav>
          <button
            type="button"
            className="menu-toggle"
            aria-label={isMenuOpen ? 'Hide menu' : 'Show menu'}
            aria-expanded={isMenuOpen}
            onClick={() => setIsMenuOpen((open) => !open)}
          >
            <svg
              className="menu-toggle-icon"
              viewBox="0 0 24 24"
              width="20"
              height="20"
              aria-hidden="true"
            >
              <path
                d="M15 5 L8 12 L15 19"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
            </svg>
          </button>
        </aside>

        <main className="main-content">
          <section className="welcome">
            <div className="welcome-text">
              <h1>Welcome to ShareRide</h1>
              <p className="lead">
                ShareRide makes everyday travel simpler by connecting drivers
                with empty seats to passengers heading the same way.
              </p>
              <p>
                Post a ride you are offering or find one that fits your route,
                then arrange the details together. Share the road, split the
                costs, and travel with people going your direction.
              </p>
            </div>
          </section>
        </main>
      </div>
    </div>
  )
}

export default App
